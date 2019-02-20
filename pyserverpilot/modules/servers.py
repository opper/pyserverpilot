from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.server import Server

ServerList = List[Server]


class Servers(Serverpilot):
    def get_servers(self) -> ServerList:
        raw_servers = self._request('GET', 'servers')
        server_objects = []

        for raw_server in raw_servers:
            server_objects.append(Server(raw_server))

        return server_objects

    def get_server(self, id: str) -> Server:
        return Server(self._request('GET', 'servers/{}'.format(id)))
