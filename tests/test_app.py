from unittest.mock import patch

import pytest

from pyserverpilot import Serverpilot
from pyserverpilot.models.app import App
from pyserverpilot.modules import Apps as AppsModule
from .mock_service import MockSP


@pytest.fixture
def client():
    yield Serverpilot.client('apps', client_id='test_id', api_key='test_key')


class TestApp(object):
    app: App  # to keep track throughout this test suite

    @patch('pyserverpilot.serverpilot.requests.request')
    def test_create_app(self, mock_sp, client: AppsModule):
        mock_sp.return_value = MockSP('get_app')
        app_data = MockSP.create_app()['data']

        response = client.create_app(**app_data)
        assert response.name == app_data['name']
        self.app = response
