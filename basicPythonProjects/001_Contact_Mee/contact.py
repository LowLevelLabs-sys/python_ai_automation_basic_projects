class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def to_dict(self):
        return {"name": self.name, "number": self.number}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["number"])
