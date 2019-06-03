# Implement a class to hold room information. This should have name and
# description attributes.

# need room title and description


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def travel(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        else:
            return None

    def is_item_in_room(self, item_name):
        for item in self.items:
            if item_name == item.name:
                return True
        return False

    def get_items(self, items=[]):
        if len(items) == 0:
            return self.items

        room_items_removed = []
        for item in items:
            for item in self.items:
                if item.get_name().lower() == item:
                    room_items_removed.append(self.items.pop(
                        self.items.index(item)))
                    break
        return room_items_removed

    def __str__(self):
        return f"{self.name}, {self.description}, items: {self.items}"
