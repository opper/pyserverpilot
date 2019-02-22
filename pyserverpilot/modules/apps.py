from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.app import App
from pyserverpilot.models.certificate import SSLCertificate

AppList = List[App]

APPS_BASE_ENDPOINT = 'apps'


class Apps(Serverpilot):
    def get_apps(self) -> AppList:
        apps = []

        for app in self._request('GET', APPS_BASE_ENDPOINT):
            apps.append(App(app))

        return apps

    def get_app(self, id: str) -> App:
        return App(self._request('GET', '{}/{}'.format(APPS_BASE_ENDPOINT, id)))

    def create_app(self, **params) -> App:
        for key, value in params.items():
            if key in ['name', 'sysuserid', 'runtime'] and isinstance(value, str) is False:
                raise TypeError('{} param has to be of type string'.format(key))
            elif key == 'domains' and isinstance(value, list) is False:
                raise TypeError('{} param has to be of type list'.format(key))
            elif key == 'wordpress':
                if isinstance(value, dict) is False:
                    raise TypeError('{} param has to be of type dict'.format(key))

                wp_values = value.items()

                for wp_key, wp_val in wp_values:
                    if isinstance(wp_val, str) is False:
                        raise TypeError('Wordpress {} param has to be of type string'.format(wp_key))

                wp_admin_password = wp_values['admin_password']

                if 8 < len(wp_admin_password) or len(wp_admin_password) > 200:
                    raise ValueError('Wordpress admin password can not be lower than 8 or bigger than 200 characters')

        return App(self._request('POST', APPS_BASE_ENDPOINT, params))

    def delete_app(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(APPS_BASE_ENDPOINT, id))

    def update_app(self, **params) -> App:
        for key, value in params.items():
            if key == 'runtime' and isinstance(value, str) is False:
                raise TypeError('{} param has to be of type string'.format(key))
            elif key == 'domains' and isinstance(value, list) is False:
                raise TypeError('{} param has to be of type list')

        return App(self._request('POST', '{}/{}'.format(APPS_BASE_ENDPOINT, id), params))

    def add_ssl(self, id: str, **params) -> SSLCertificate:
        for key, value in params.items():
            if isinstance(value, str) is False:
                raise TypeError('{} has to be of type string'.format(key))

        return SSLCertificate(self._request('POST', '{}/{}/ssl'.format(APPS_BASE_ENDPOINT, id), params))
