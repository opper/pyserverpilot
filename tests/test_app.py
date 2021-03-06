from unittest.mock import patch

import pytest
from marshmallow import ValidationError

from pyserverpilot import Serverpilot
from pyserverpilot.models.app import App as AppModel
from pyserverpilot.modules import Apps as AppsModule
from .mocks.app_mock import AppMock


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
        mock_sp.return_value = AppMock('get_app')
        app_data = AppMock.create_app()['data']

        response = client.create_app(**app_data)
        assert response.name == app_data['name']
        shared['app'] = response

    def test_get_app(self, mock_sp, client: AppsModule, shared):
        mock_sp.return_value = AppMock('get_app')
        app = shared['app']

        response = client.get_app(app.id)
        assert response.id == app.id

    def test_app_create_validation(self, mock_sp, client: AppsModule):
        with pytest.raises(ValidationError):
            client.create_app()  # no parameters

            client.create_app(**AppMock.create_app(), unknown_param='should trigger error')  # unknown parameters

            client.create_app(name='app',
                              sysuserid='userid',
                              runtime='php7.1',
                              domains='should trigger error')  # invalid parameter type

            client.create_app(name='app',
                              sysuserid='userid',
                              runtime='php7.1',
                              domains=['website.com', 'www.website.com'],
                              wordpress={})  # invalid worpdress fields

            client.create_app(name='app',
                              sysuserid='userid',
                              runtime='php7.1',
                              domains=['website.com', 'www.website.com'],
                              wordpress={
                                  'site_title': 'Awesome site',
                                  'admin_user': 'admin',
                                  'admin_password': 'fail',  # should fail because of invalid password
                                  'admin_email': 'admin@website.com'
                              })

        mock_sp.return_value = AppMock('')
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

    def test_update_app_validation(self, mock_sp, client: AppsModule, shared):
        app = shared['app']  # type: AppModel

        with pytest.raises(ValidationError):
            client.update_app(app.id, domains="website.com")  # invalid parameter type

        mock_sp.return_value = AppMock('update_app')
        response = client.update_app(app.id, domains=['www.myshop.com', 'myshop.com'], runtime='php7.1')

        assert response.id == app.id
        assert response.runtime == 'php7.2'

    def test_add_ssl(self, mock_sp, client: AppsModule, shared):
        app = shared['app']  # type: AppModel

        with pytest.raises(ValidationError):
            client.add_ssl(app.id)  # missing params

            client.add_ssl(app.id, key=123, cert='sslcert', cacerts='sslcacert')  # invalid parameter type

        mock_sp.return_value = AppMock('add_ssl')
        response = client.add_ssl(app.id, key='sslkey', cert='sslcert', cacerts=None)

        assert response.key == 'sslkey'
        assert response.cert == 'sslcert'

        app.ssl = response

    def test_enable_force_ssl(self, mock_sp, client: AppsModule, shared):
        app = shared['app']  # type: AppModel

        with pytest.raises(ValidationError):
            client.set_force_ssl(app.id)

            client.set_force_ssl(app.id, force="yes")  # invalid parameter type

        mock_sp.return_value = AppMock('set_force_ssl')
        response = client.set_force_ssl(app.id, force=True)

        assert response.key == app.ssl.key
        assert response.force is True
