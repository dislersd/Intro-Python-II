# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def travel(self, direction):
        nextRoom = self.room.travel(direction)
        if nextRoom is not None:
            self.room = nextRoom
        else:
            print('You cannot go that way')

    def add_items(self, item):
            self.items.append(item)

    def get_item(self):
        return self.items

    def get_item_names(self):
        item_names = []
        for item in self.items:
            item_names.append(item.get_name())
        return item_names

    def drop_item(self, item_name):
        dropped_items = []
        for item in item_name:
            for item in self.items:
                if item.get_name().lower() == item_name:
                    dropped_items.append(self.items.pop(
                        self.items.index(item)))
                    break
        return dropped_items

    def __str__(self):
        return f"\nName: {self.name}, Current Room: {self.room}, Items: {self.room.items}\n"
