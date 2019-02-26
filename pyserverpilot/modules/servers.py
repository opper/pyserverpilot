from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.server import Server
from pyserverpilot.schemas.server import UpdateServerSchema

ServerList = List[Server]

SERVERS_BASE_ENDPOINT = 'servers'


class Servers(Serverpilot):
    def get_servers(self) -> ServerList:
        servers = []

        for server in self._request('GET', SERVERS_BASE_ENDPOINT):
            servers.append(Server(server))

        return servers

    def get_server(self, id: str) -> Server:
        return Server(self._request('GET', '{}/{}'.format(SERVERS_BASE_ENDPOINT, id)))

    def delete_server(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(SERVERS_BASE_ENDPOINT, id))

    def update_server(self, id: str, **params) -> Server:
        UpdateServerSchema().load(params)

        return Server(self._request('POST', '{}/{}'.format(SERVERS_BASE_ENDPOINT, id), params))
