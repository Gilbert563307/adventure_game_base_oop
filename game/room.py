# Define a class for Rooms
# Ways to expand:
# - Add a method to add, remove and get enemies
class Room:
    def __init__(self, name, description, x=0, y=0):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.x = x
        self.y = y

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"
