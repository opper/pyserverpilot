import re
import string

from pyserverpilot import Serverpilot
from pyserverpilot.models.sysuser import Sysuser

BASE_SYSUSERS_ENDPOINT = 'sysusers'


class Sysusers(Serverpilot):

    def get_sysusers(self) -> Sysuser:
        return Sysuser(self._request('GET', BASE_SYSUSERS_ENDPOINT))

    def add_sysuser(self, **params) -> Sysuser:
        for key, value in params.items():
            if isinstance(value, str) is False:
                raise TypeError('{} param must be of type string'.format(key))

            if key == 'password' and (len(value) < 8 or len(value) > 200):
                raise ValueError('Password has to be between 8 and 200 characters long')

            if key == 'name':
                if len(value) < 3 or len(value) > 32:
                    raise ValueError('Name has to be between 3 and 32 characters long')

                if value[0] not in string.ascii_lowercase:
                    raise ValueError('Name has to start with a lowercase ascii letter')

                if re.match(re.compile(r'^[-a-zA-Z0-9]+$'), value) is False:
                    raise ValueError('Name contains invalid characters')

        required_params = ['serverid', 'name']

        for param in required_params:
            if param not in params:
                raise AttributeError('Missing required attribute: {}'.format(param))

        return Sysuser(self._request('POST', BASE_SYSUSERS_ENDPOINT))

    def get_sysuser(self, id: str) -> Sysuser:
        return Sysuser(self._request('GET', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id)))

    def delete_sysuser(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id))

    def update_sysuser(self, id: str, **params) -> Sysuser:
        if 'password' not in params:
            raise AttributeError('password argument is required')

        password = params.get('password')

        if len(password) < 8 or len(password) > 200:
            raise ValueError('Password has to be between 8 and 200 characters long')

        return Sysuser(self._request('POST', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id)))
