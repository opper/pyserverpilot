from pyserverpilot.models.basemodel import BaseModel


class Sysuser(BaseModel):
    id: str
    name: str
    serverid: str
