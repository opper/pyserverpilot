from pyserverpilot.models.basemodel import BaseModel


class Server(BaseModel):
    id: str
    name: str
    plan: str
    autoupdates: str
    firewall: str
    deny_unknown_domains: str
    available_runtimes: list
    lastaddress: str
    lastconn: int
    datecreated: int
