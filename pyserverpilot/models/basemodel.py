class BaseModel:
    def __init__(self, attrs) -> None:
        for attribute, value in attrs.items():
            setattr(self, attribute, value)
