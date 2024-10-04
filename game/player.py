# Ideas to extend functionality:
# Add health & resource management:
# - add health attribute
# - health decreases when you pass through the fire room
# - health increases when you find a health item
# - use your creativity


# Define a class for the Player
class Player:
    def __init__(self, name, current_room, rooms):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.rooms = rooms
        self.visited_rooms = {current_room}

    def move(self, direction):
        new_x, new_y = self.current_room.x, self.current_room.y
        if direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        elif direction == "up":
            new_y += 1
        elif direction == "down":
            new_y -= 1

        else:
            print("Invalid direction.")
            return

        # Find room at the new coordinates
        new_room = None  # Initialize new_room to None
        # Loop through all rooms in self.rooms
        for room in self.rooms:
            # Check if the current room's coordinates match the target coordinates
            if room.x == new_x and room.y == new_y:
                new_room = room
                break

        if new_room:
            self.current_room = new_room
            self.visited_rooms.add(new_room)
            cure_room_items = self.current_room.get_items()

            # Beginner: When the user enters any room, expand the description and print the items present in
            # the room and, make a story around it

            description_to_print: str = f"You are now in the {new_room.name}."

            print(description_to_print)

            message: str = "In deze room zijn deze items present: "
            for item in cure_room_items:
                message += f"{item}"
            print(message)
        else:
            print(f"You can't go that way")

    def pick_up(self, chosen_item_name):
        for item in self.current_room.items:
            if item.name == chosen_item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You picked up the {chosen_item_name}.")
                return
        print(f"There is no {chosen_item_name} here.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is empty.")

    def has_user_got_key(self) -> bool:
        for item in self.inventory:
            if item.name == "Key":
                return True
        return False

    def show_map(self):
        self.display_map()

    def display_map(self):
        # Determine the bounds of the map
        # Only the discovered rooms will be shown
        min_x = min(room.x for room in self.visited_rooms)
        max_x = max(room.x for room in self.visited_rooms)
        min_y = min(room.y for room in self.visited_rooms)
        max_y = max(room.y for room in self.visited_rooms)

        # Create the map grid
        # Added spaces to determinate the length of the cell
        map_grid = [
            ["      " for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)
        ]

        # Place rooms in the grid
        for room in self.visited_rooms:
            if room.items:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()}.]"
            else:
                map_grid[room.y - min_y][room.x - min_x] = f"[{room.name[:3].upper()} ]"

        # Display the map
        print("\nMap:")
        for row in map_grid:
            print("".join(row))
        print(f"\nYou are currently in the {self.current_room.name}")
