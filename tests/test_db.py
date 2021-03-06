from unittest.mock import patch

import pytest
from marshmallow import ValidationError

from pyserverpilot import Serverpilot
from pyserverpilot.modules.dbs import Dbs as DbsModule
from tests.mocks.db_mock import DbMock


@pytest.fixture
def client():
    return Serverpilot.client('dbs', client_id='test_id', api_key='test_key')


@pytest.fixture(scope='module')
def shared():
    return {
        'db': None,
    }


@patch('pyserverpilot.serverpilot.requests.request')
class TestDb(object):

    def test_get_dbs(self, mock_sp, client: DbsModule):
        mock_sp.return_value = DbMock('get_dbs')

        response = client.get_dbs()

        assert len(response) == 2

    def test_create_db(self, mock_sp, client: DbsModule, shared):
        mock_sp.return_value = DbMock('get_db')
        db_data = DbMock.create_db()['data']

        response = client.create_db(**db_data)

        assert response.name == db_data['name']
        shared['db'] = response

    def test_get_db(self, mock_sp, client: DbsModule, shared):
        db = shared['db']
        mock_sp.return_value = DbMock('get_db')

        response = client.get_db(db.id)

        assert response.id == db.id
        assert response.appid == db.appid
        assert response.serverid == db.serverid

    def test_fail_create_db(self, mock_sp, client: DbsModule):
        with pytest.raises(ValidationError):
            client.create_db()  # no params error

            client.create_db(appid='app',
                             name='database!',  # name contains invalid characters
                             user={})

            client.create_db(appid='app',
                             name='database',
                             user={
                                 'name': 'superlongnameshouldbeinvalid',  # invalid username
                                 'password': 'BaOWYl3IjMc4raBe'
                             })

            client.create_db(appid='app',
                             name='database',
                             user={
                                 'name': 'username',
                                 'password': 'passwd',  # invalid password
                             })

            client.create_db(appid='app',
                             name='database',
                             user={
                                 'name': 'username',
                                 'password': 'BaOWYl3IjMc4raBe',
                                 'hello': 'extraparam'  # extra invalid param
                             })

    def test_update_db(self, mock_sp, client: DbsModule, shared):
        db = shared['db']

        with pytest.raises(ValidationError):
            client.update_db(db.id)  # no params error

            client.update_db(db.id, user={})  # invalid user schema

            client.update_db(db.id,
                             user={
                                 'name': 'superlongnameshouldbeinvalid',  # invalid username
                                 'password': 'BaOWYl3IjMc4raBe'
                             })

            client.update_db(db.id,
                             user={
                                 'name': 'username',
                                 'password': 'passw',  # invalid password
                             })

            client.update_db(db.id,
                             user={
                                 'name': 'username',
                                 'password': 'BaOWYl3IjMc4raBe',
                                 'hello': 'extraparam'  # extra invalid param
                             })

        new_user = {
            'name': 'jerry',
            'password': 'BaOWYl3IjMc4raBe'
        }

        mock_sp.return_value = DbMock('update_db')
        client.update_db(db.id, user=new_user)

        mock_sp.return_value = DbMock('update_db')

        response = client.get_db(shared['db'].id)

        assert response.user['name'] == new_user['name']
