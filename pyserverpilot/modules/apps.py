from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.app import App

AppList = List[App]


class Apps(Serverpilot):
    def get_apps(self) -> AppList:
        apps = []

        for app in self._request('GET', 'apps'):
            apps.append(App(app))

        return apps

    def get_app(self, id: str) -> App:
        return App(self._request('GET', 'apps/{}'.format(id)))
