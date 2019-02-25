from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.app import App
from pyserverpilot.models.certificate import SSLCertificate
from pyserverpilot.schemas.app import CreateAppSchema, UpdateAppSchema

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
        # validate the parameters before posting to serverpilot
        CreateAppSchema().load(params)

        return App(self._request('POST', APPS_BASE_ENDPOINT, params))

    def delete_app(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(APPS_BASE_ENDPOINT, id))

    def update_app(self, **params) -> App:
        # validate the parameters before posting to serverpilot
        UpdateAppSchema().load(params)

        return App(self._request('POST', '{}/{}'.format(APPS_BASE_ENDPOINT, id), params))

    def add_ssl(self, id: str, **params) -> SSLCertificate:
        for key, value in params.items():
            if isinstance(value, str) is False:
                raise TypeError('{} param has to be of type string'.format(key))

        return SSLCertificate(self._request('POST', '{}/{}/ssl'.format(APPS_BASE_ENDPOINT, id), params))

    def enable_auto_ssl(self, id: str) -> SSLCertificate:
        params = {
            'auto': True,
        }

        return SSLCertificate(self._request('POST', '{}/{}/ssl'.format(APPS_BASE_ENDPOINT, id), params))

    def delete_ssl(self, id: str) -> None:
        self._request('DELETE', '{}/{}/ssl'.format(APPS_BASE_ENDPOINT, id))

    def set_force_ssl(self, id: str, **params) -> SSLCertificate:
        if isinstance(params['force'], bool) is False:
            raise TypeError('force param has to be of type boolean')

        return SSLCertificate(self._request('POST', '{}/{}/ssl'.format(APPS_BASE_ENDPOINT, id), params))
