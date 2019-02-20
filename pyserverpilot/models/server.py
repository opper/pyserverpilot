class Server:
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

    def __init__(self, attrs) -> None:
        for attribute, value in attrs.items():
            setattr(self, attribute, value)
