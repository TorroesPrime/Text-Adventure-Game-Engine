"""game state module"""
class gamestate():
    """defines game state"""
    def __init__(self,dungeon):
        self.save_file_version = "RT001"
        self.current_room_leader = "Current room: "
        self.default_save_file = "zorkSave"
        self.save_file_ext = ".sav"
        self.dungeon = dungeon
        self.adventurers_current_room = self.dungeon.entry
        self.test_value = False
        self.player_character = None
        self.characters = []
        self.actions = []

    def store_state(self, save_name):
        """method to write present gamestate to .sav file"""
        savefile = open(save_name, "w")
        savefile.write(self.save_file_version+"\n")
        self.dungeon.store_state(savefile)
        current_room_record = self.current_room_leader+self.adventurers_current_room.name
        savefile.write(current_room_record+"\n")
        savefile.close()
    def initialize(self, dungeon):
        """initialize dungeon and sets adventuers current room to entry room."""
        self.dungeon = dungeon
        self.adventurers_current_room = dungeon.entry
    def get_adventurers_current_room(self):
        """returns adventurers current room"""
        return self.adventurers_current_room

    def set_adventurers_current_soom(self, room):
        """set's adventurer's current room"""
        self.adventurers_current_room = room

    def set_player_character(self, character):
        """sets the selected character to be the player character"""
        self.player_character = character
    def add_character(self, characters):
        """adds a supplied character to dungeon's characters list."""
        for character in characters:
            self.characters.append(character)
    def set_test(self):
        """set's test status"""
        if self.testValue is True:
            self.test_value = False
        else:
            self.test_value = True
