import re
from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.db import DB

BASE_DB_ENDPOINT = 'dbs'

DB_List = List[DB]


class Db(Serverpilot):
    def get_dbs(self) -> DB_List:
        dbs = []

        for db in self._request('GET', BASE_DB_ENDPOINT):
            dbs.append(db)

        return dbs

    def create_db(self, **params) -> DB:
        for key, value in params.items():
            if key == 'appid' or key == 'name' and isinstance(value, str) is False:
                raise TypeError('{} param must be of type string'.format(key))

            if key == 'name' and re.match(re.compile(r'^[-a-zA-Z0-9]+$'), value) is False:
                raise ValueError('Name contains invalid characters')

            if key == 'user':
                db_user = value['name']
                db_pass = value['password']

                if len(db_user) > 16:
                    raise ValueError('db name has to be less than 16 characters long')

                if len(db_pass) < 8 or len(db_pass) > 200:
                    raise ValueError('db password has to be between 8 and 200 characters long')

        return DB(self._request('POST', BASE_DB_ENDPOINT, params))

    def get_db(self, id: str) -> DB:
        return DB(self._request('GET', '{}/{}'.format(BASE_DB_ENDPOINT, id)))

    def delete_db(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(BASE_DB_ENDPOINT, id))

    def update_db(self, id: str, **params) -> DB:
        if 'user' not in params:
            raise AttributeError('missing required attribute user')

        user = params.get('user')
        db_pass = user['password']

        if len(db_pass) < 8 or len(db_pass) > 200:
            raise ValueError('db password has to be between 8 and 200 characters long')

        return DB(self._request('POST', '{}/{}'.format(BASE_DB_ENDPOINT, id), params))
