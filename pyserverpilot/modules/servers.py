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

    def delete_server(self, id: str) -> None:
        self._request('DELETE', 'servers{}'.format(id))

    def update_server(self, id: str, **params) -> Server:
        for key, val in params.items():
            if key is 'plan' and type(val) is not str:
                raise ValueError('plan argument has to be of type string')
            if (key is 'firewall' or key is 'autoupdates' or key is 'deny_unknown_domains') and val is not bool:
                raise ValueError('{} argument has to be of type boolean'.format(key))

        return Server(self._request('POST', 'servers/{}'.format(id), params))
