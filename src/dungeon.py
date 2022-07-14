"""dungeon module"""
from room import Room
class Dungeon:
    """dungeon class"""
    def __init__(self,entry = None,
    filname: str = "TEST FILE NAME",
    title: str = "TEST DUNGEON TITLE",
    
    ):
        self.filename= filname
        self.title = title
        self.entry = entry
        self.rooms = {}
        self.characters = []
        self.player_character =""
        self.items = []

    def get_room(self,room_name):
        """returns a list of the rooms in this dungeon"""
        return self.rooms[room_name]

    def set_player_character(self,character):
        """sets this dungeon's player character"""
        self.player_character = character

    def add_rooms(self,rooms):
        """adds a series of rooms to the dungeon"""
        for room in rooms:
            self.rooms.update({room.name:room})
    def store_state(self,filename):
        '''method to store the current state of the dungeon in a .sav file'''
        print("dungeon().store_state()")
    def restore_state(self,filename):
        '''method to read from a .save file and re-instantiate the dungeon'''
        print("dungeon().restore_state()")
    def dungeon_manual(self,title, entry):
        """manual dungeon instantiation method"""
        Dungeon().__init__()
        self.title = title
        self.entry = entry
        self.rooms = {}

    def dungeon_read(self,filename):
        """Read from the .zork filename passed, and instantiate a Dungeon object based on it."""
        super().__init__()
        self.filename = filename
        fileReader = open(filename,'r')
        self.title = fileReader.readline()
