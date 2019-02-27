from pyserverpilot.models.autossl import AutoSSL
from pyserverpilot.models.basemodel import BaseModel
from pyserverpilot.models.certificate import SSLCertificate


class App(BaseModel):
    id: str
    datecreated: int
    name: str
    sysuserid: str
    domains: list
    ssl: SSLCertificate
    autossl: AutoSSL
    serverid: str
    runtime: str

    def __init__(self, attrs) -> None:
        super().__init__(attrs)
        for attribute, value in attrs.items():
            if attribute == 'ssl' and value is not None:
                setattr(self, attribute, SSLCertificate(value))
            elif attribute == 'autossl' and value is not None:
                setattr(self, attribute, AutoSSL(value))
            else:
                setattr(self, attribute, value)
