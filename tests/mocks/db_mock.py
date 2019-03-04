from tests.mocks.base import BaseMock


class DbMock(BaseMock):

    @classmethod
    def create_db(cls):
        return {
            "data": {
                "name": "shopify",
                "appid": "B1w7yc1tfUPQLIKS",
                "user": {
                    "name": "thomas",
                    "password": "krh1haMCVfYz6Alr",
                }
            }
        }

    @classmethod
    def get_dbs(cls):
        return {
            "data": [{
                "id": "hdXkAZchuj27Hm1L",
                "name": "wordpress",
                "appid": "c77JD4gZooGjrF8K",
                "serverid": "4zGDDO2xg30yEeum",
                "user": {
                    "id": "vt08Qz9kjOC3RVLr",
                    "name": "robert"
                }
            }, {
                "id": "a2SJNvzDJxSbZaMX",
                "name": "shopify",
                "appid": "B1w7yc1tfUPQLIKS",
                "serverid": "4zGDDO2xg30yEeum",
                "user": {
                    "id": "j2P1zZ9xTusGjy16",
                    "name": "thomas"
                }
            }]
        }

    @classmethod
    def get_db(cls):
        return {
            "data": {
                "id": "a2SJNvzDJxSbZaMX",
                "name": "shopify",
                "appid": "B1w7yc1tfUPQLIKS",
                "serverid": "4zGDDO2xg30yEeum",
                "user": {
                    "id": "j2P1zZ9xTusGjy16",
                    "name": "thomas"
                }
            }
        }
