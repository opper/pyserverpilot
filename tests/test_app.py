from unittest.mock import patch

from pyserverpilot import Serverpilot
from .mock_service import MockSP


class TestApp(object):

    @patch('pyserverpilot.serverpilot.requests.request')
    def test_get_apps(self, mock_sp):
        mock_sp.return_value = MockSP('get_apps')

        cl = Serverpilot.client('apps', client_id='test_id', api_key='test_key')
        r = cl.get_apps()
        assert r[0].id == 'c77JD4gZooGjrF8K'
