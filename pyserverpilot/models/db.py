from pyserverpilot.models.basemodel import BaseModel


class DB(BaseModel):
    id: str
    name: str
    appid: str
    serverid: str
    user: dict
