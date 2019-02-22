from pyserverpilot.models.basemodel import BaseModel


class SSLCertificate(BaseModel):
    key: str
    cert: str
    cacerts: str
    auto: bool = True
    force: bool = False
