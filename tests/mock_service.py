class MockSP:
    status_code = 200
    to_call = ''

    def __init__(self, method: str = ''):
        self.to_call = method

    def json(self):
        return getattr(self, self.to_call)()

    def get_app(self):
        return {
            "data": {
                "id": "c77JD4gZooGjrF8K",
                "datecreated": 1403139066,
                "name": "blog",
                "sysuserid": "RvnwAIfuENyjUVnl",
                "domains": ["www.myblog.com", "blog.com"],
                "ssl": None,
                "serverid": "4zGDDO2xg30yEeum",
                "runtime": "php7.0"
            }
        }

    def get_apps(self):
        return {
            "data": [{
                "id": "c77JD4gZooGjrF8K",
                "datecreated": 1403139066,
                "name": "blog",
                "sysuserid": "RvnwAIfuENyjUVnl",
                "domains": ["www.myblog.com", "blog.com"],
                "ssl": None,
                "serverid": "4zGDDO2xg30yEeum",
                "runtime": "php7.0"
            }, {
                "id": "B1w7yc1tfUPQLIKS",
                "datecreated": 1403143012,
                "name": "store",
                "sysuserid": "RvnwAIfuENyjUVnl",
                "domains": ["www.mystore.com", "mystore.com"],
                "ssl": {
                    "key": "-----BEGIN PRIVATE KEY----- ...",
                    "cert": "-----BEGIN CERTIFICATE----- ...",
                    "cacerts": "-----BEGIN CERTIFICATE----- ...",
                    "auto": False,
                    "force": False
                },
                "serverid": "4zGDDO2xg30yEeum",
                "runtime": "php7.0"
            }],
        }
