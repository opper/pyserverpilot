class MockSP:
    status_code: int
    to_call: str

    def __init__(self, method: str = '', status_code: int = 200):
        self.to_call = method
        self.status_code = status_code

    def json(self):
        return getattr(self, self.to_call)()

    @classmethod
    def create_app(cls):
        return {
            "data": {
                "name": "superawesome-website",
                "sysuserid": "RvnwAIfuENyjUVnl",
                "runtime": "php7.0",
                "domains": ["www.example.com", "example.com"],
            }
        }

    @classmethod
    def get_app(cls):
        return {
            "data": {
                "id": "c77JD4gZooGjrF8K",
                "datecreated": 1403139066,
                "name": "superawesome-website",
                "sysuserid": "RvnwAIfuENyjUVnl",
                "domains": ["www.myblog.com", "blog.com"],
                "ssl": None,
                "serverid": "4zGDDO2xg30yEeum",
                "runtime": "php7.0"
            }
        }

    @classmethod
    def get_apps(cls):
        return {
            "data": [{
                "id": "c77JD4gZooGjrF8K",
                "datecreated": 1403139066,
                "name": "superawesome-website",
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
