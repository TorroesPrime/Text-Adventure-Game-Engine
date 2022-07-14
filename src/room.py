#from interpreter import gameStateInstance as gsi
#from library import *
#import inspect
""" Room module that contains all the material for creating a room object. Last update: 6/30/2022"""
#import character

class Room:
    """Creates a 'room' object that is made up of a room and at least 1 'exit' \
        leading to another room."""
    def __init__(self,
    name: str = "TEST NAME",
    desc: str = "TEST DESCRIPTION",
    ):
        self.been_here = False
        self.name = name
        self.desc = desc
        self.exits = []
        self.inventory = []
        self.non_player_characters = []
    def add_non_player_character(self,chars):
        '''if chars is a single character add to the rooms NonPlayerCharacters
         list. if it's a list call addNonPlayerCharacters'''
        if str(type(chars)) != "<class 'character.character'>":
            self.non_player_characters.append(chars)
        else:
            self.add_non_player_characters(chars)
    def add_non_player_characters(self,chars):
        """Adds a list of characters."""
        for entry in chars:
            self.non_player_characters.append(entry)
    def add_exits(self, exits):
        """takes a list of exits and adds each one to the room's exits list"""
        for entry in exits:
            if entry.source_room.name == self.name:
                self.exits.append(entry)
    def get_character(self,name):
        """returns a character called by name"""
        for character in self.non_player_characters:
            character_name = character.get_full_name().lower()
            if character_name == name.lower():
                return character
            return None
    def store_state(self,save_file,game_state):
        """Stores the current state of this room to the filename passed to it."""
        pass

    def restore_state(self, state):
        """retores the state of the room from a .sav file."""
        pass
    def describe(self):
        """returns a string describing the room that may include the exits from the room."""
        description = ""
        if self.been_here is True:
            description = self.name
        else:
            description = self.name+"\n"+self.desc+"\n"
        for entry in self.exits:
            description = description + "\n"+entry.describe()
        self.been_here = True
        return description
    def full_describe(self):
        """returns a string describing the room, the name of the room, the exits in the room and \
            the contents of the room."""
        description = self.name+"\n"+self.desc+"\n"
        exits = ""
        chars = ""
        if len(self.non_player_characters) != 0:
            chars = "The following characters are in the room: \n"
            for char in self.non_player_characters:
                print(char.get_full_name())
                #chars = chars + char.getFullName()+"\n"
        else:
            chars = "There is no one else in the room."
        if len(self.inventory) != 0:
            items = "the room contains: "+self.list_items()+"."
        #for entry in self.exits:
        #    description = description + "\n"+entry.describe()
        else:
            items = ""
        for entry in self.exits:
            exits=exits+entry.describe()+"\n"
        description = description+items+"\n"+chars+"\n"+exits+"\n"
        print(description)
    def list_items(self):
        """returns a list of the items in the room."""
        items =""
        for item in self.inventory:
            items = items + "\n-"+item.name
        return items
    def leave_by(self, direction):
        """allows the player to move from the current room to an adjascent room by supplying a \
            direction."""
        for room_exit in self.exits:
            #if gameState.test_value:
            #    print(f"source room:{e.source_room.name}")
            #    print(f"destination room:{e.destination_room.name}")
            if room_exit.get_direction() == direction:
                dest = room_exit.get_destination()
                break
            else:
                dest = None
        return dest
    def list_exits(self):
        """lists the availible exits from a given room."""
        for room_exit in self.exits:
            print(f"Source room: {room_exit.get_source().name}")
            print(f"Direction: {room_exit.get_direction()}")
            print(f"Destination room: {room_exit.get_destination().name}")
    def add_item(self,item):
        """adds an item to the room's inventory"""
        self.inventory.append(item)
       # if gameState.test_value:
       #     print("Added "+item.name)
    def remove_item(self, item_name):
        """removes an item from the room's inventory by supplying the name of the time to be \
            removed."""
        room_inventory_names = []
        item = ""
        for item in self.inventory:
            if item_name == item.name:
                self.inventory.remove(item)
