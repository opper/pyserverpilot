from typing import List

from pyserverpilot import Serverpilot
from pyserverpilot.models.db import DB
from pyserverpilot.schemas.db import CreateDBSchema, UpdateDBSchema

BASE_DB_ENDPOINT = 'dbs'

DB_List = List[DB]


class Dbs(Serverpilot):
    def get_dbs(self) -> DB_List:
        dbs = []

        for db in self._request('GET', BASE_DB_ENDPOINT):
            dbs.append(db)

        return dbs

    def create_db(self, **params) -> DB:
        CreateDBSchema().load(params)

        return DB(self._request('POST', BASE_DB_ENDPOINT, params))

    def get_db(self, id: str) -> DB:
        return DB(self._request('GET', '{}/{}'.format(BASE_DB_ENDPOINT, id)))

    def delete_db(self, id: str) -> None:
        self._request('DELETE', '{}/{}'.format(BASE_DB_ENDPOINT, id))

    def update_db(self, id: str, **params) -> DB:
        UpdateDBSchema().load(params)

        return DB(self._request('POST', '{}/{}'.format(BASE_DB_ENDPOINT, id), params))
