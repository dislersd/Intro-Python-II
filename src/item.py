class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def __str__(self):
        return f"\nItem: {self.name}, Description: {self.description}\n"

    def __repr__(self):
        return self.name
