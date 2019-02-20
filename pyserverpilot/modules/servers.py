from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.server import Server

ServerList = List[Server]


class Servers(Serverpilot):
    def get_servers(self) -> ServerList:
        servers = []

        for server in self._request('GET', 'servers'):
            servers.append(Server(server))

        return servers

    def get_server(self, id: str) -> Server:
        return Server(self._request('GET', 'servers/{}'.format(id)))
