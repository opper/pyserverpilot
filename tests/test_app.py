from unittest.mock import patch

import pytest
from marshmallow import ValidationError

from pyserverpilot import Serverpilot
from pyserverpilot.modules import Apps as AppsModule
from .mock_service import MockSP


@pytest.fixture
def client():
    return Serverpilot.client('apps', client_id='test_id', api_key='test_key')


@pytest.fixture(scope='module')
def shared():
    return {
        'app': None,
    }


@patch('pyserverpilot.serverpilot.requests.request')
class TestApp(object):

    def test_create_app(self, mock_sp, client: AppsModule, shared):
        mock_sp.return_value = MockSP('get_app')
        app_data = MockSP.create_app()['data']

        response = client.create_app(**app_data)
        assert response.name == app_data['name']
        shared['app'] = response

    def test_get_app(self, mock_sp, client: AppsModule, shared):
        mock_sp.return_value = MockSP('get_app')

        response = client.get_app(shared['app'].id)
        assert response.id == shared['app'].id

    def test_app_validation(self, mock_sp, client: AppsModule):
        with pytest.raises(ValidationError):
            client.create_app()  # no parameters

            client.create_app(**MockSP.create_app(), unknown_param='should trigger error')  # unknown parameters

            client.create_app(name='app',
                              sysuserid='userid',
                              runtime='php7.1',
                              domains='should trigger error')  # invalid parameter type

            client.create_app(name='app',
                              sysuserid='userid',
                              runtime='php7.1',
                              domains=['website.com', 'www.website.com'],
                              wordpress={})  # invalid worpdress fields

        mock_sp.return_value = MockSP('')
        client.create_app(name='app',
                          sysuserid='userid',
                          runtime='php7.1',
                          domains=['website.com', 'www.website.com'],
                          wordpress={
                              'site_title': 'Awesome site',
                              'admin_user': 'admin',
                              'admin_password': 'shouldnotfail',
                              'admin_email': 'admin@website.com'
                          })
