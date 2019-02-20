class App:
    id: str
    datecreated: int
    name: str
    sysuserid: str
    domains: list
    ssl: dict
    serverid: str
    runtime: str

    def __init__(self, attrs) -> None:
        for attribute, value in attrs.items():
            setattr(self, attribute, value)
