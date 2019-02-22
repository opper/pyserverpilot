from pyserverpilot.models.basemodel import BaseModel


class AutoSSL(BaseModel):
    available: bool
    domains: list
