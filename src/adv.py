from room import Room
from player import Player
from item import Item

# Declare all the rooms

rock = Item('rock', 'this is a rock')
sword = Item('sword', 'this is a sword')
shield = Item('shield', 'this is a shield')
knife = Item('knife', 'this is a knife')
staff = Item('staff', 'this is a staff')


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [rock, sword]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [shield]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [knife]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [staff]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

# should initialize as none

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.\
player = Player('Dylan', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



def get_items_from_room(player_selected_itemnames, room, player):
    for player_selected_itemname in player_selected_itemnames:
        if not room.is_item_in_room(player_selected_itemname):
            print(f"Item not found: {player_selected_itemname}")
            return input(f"(Press enter to continue...)")

    player.add_items(room.get_items(player_selected_itemnames))

    print(f"{player} stores items: {player_selected_itemnames}")
    return input(f"(Press enter to continue...)")


while True:
    print(player.room.name)
    print(player.room.description)
    print(player.room.items)
    # cmd = input("What do you want to do? ")
    cmd = ' '.join(input("Enter command: ").lower().split()).split(" ")

    if cmd[0] in ['n', 'e', 's', 'w']:
        player.travel(cmd[0])
    elif "get" in cmd[0] or "take" in cmd[0]:
        get_items_from_room(cmd[1:], player.room, player)
    elif cmd[0] == 'q':
        break
    else:
        print('invalid command')
