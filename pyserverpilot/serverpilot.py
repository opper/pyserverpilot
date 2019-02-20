import requests
from .models.error import ServerpilotError
from requests.auth import HTTPBasicAuth
import json

from .models.server import Server


class Serverpilot:
    client_id: str
    api_key: str

    BASE_URL = 'https://api.serverpilot.io/v1/{}'

    def __init__(self, client_id: str = '', api_key: str = ''):
        if client_id is '' or api_key is '':
            raise ValueError('Client ID and API keys are required')

        self.client_id = client_id
        self.api_key = api_key

    def _request(self, method: str = '', endpoint: str = '', data: str or dict = None, headers: dict = None) -> dict:
        if data is None:
            data = {}

        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }

        response = requests.request(
            method,
            self.BASE_URL.format(endpoint),
            auth=HTTPBasicAuth(
                username=self.client_id,
                password=self.api_key
            ),
            data=json.dumps(data) if data != {} else {},
            headers=headers,
        )

        if response.status_code != 200:
            raise ServerpilotError(response.status_code, response.json()['error']['message'])

        return response.json()['data']

    def get_servers(self):
        raw_servers = self._request('GET', 'servers')
        server_objects = []

        for raw_server in raw_servers:
            server_objects.append(Server(raw_server))

        return server_objects
