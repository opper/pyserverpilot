from pyserverpilot import Serverpilot
from pyserverpilot.models.sysuser import Sysuser
from pyserverpilot.schemas.sysuser import CreateSysUserSchema, UpdateSysUserSchema

BASE_SYSUSERS_ENDPOINT = 'sysusers'


class Sysusers(Serverpilot):

    def get_sysusers(self) -> Sysuser:
        return Sysuser(self._request('GET', BASE_SYSUSERS_ENDPOINT))

    def add_sysuser(self, **params) -> Sysuser:
        CreateSysUserSchema().load(params)

        return Sysuser(self._request('POST', BASE_SYSUSERS_ENDPOINT))

    def get_sysuser(self, id: str) -> Sysuser:
        return Sysuser(self._request('GET', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id)))

    def delete_sysuser(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id))

    def update_sysuser(self, id: str, **params) -> Sysuser:
        UpdateSysUserSchema().load(params)

        return Sysuser(self._request('POST', '{}/{}'.format(BASE_SYSUSERS_ENDPOINT, id)))
