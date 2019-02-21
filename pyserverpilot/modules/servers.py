from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.server import Server

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
        for key, val in params.items():
            if key == 'plan' and isinstance(val, str) is False:
                raise TypeError('plan argument has to be of type string')
            elif key in ['firewall', 'autoupdates', 'deny_unknown_domains'] and isinstance(val, bool) is False:
                raise TypeError('{} argument has to be of type boolean'.format(key))
            else:
                raise AttributeError('Found unexpected argument: {}'.format(key))

        return Server(self._request('POST', '{}/{}'.format(SERVERS_BASE_ENDPOINT, id), params))
