# Defined a class for Items
# Expand items with superpower actions
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} {self.description}"
