"""rudimentary data base system for handling characters."""
from character import Character
class characters_list():
    """primary database system uses a dicitonary with ID numbers as the key."""
    lastest_id = 0
    def __init__(self):
        self.database = {}
    
    def generate_id(self):
        global latest_id 
        latest_id =+1 

    def add_character(self,character):
        character_full_name = character.get_full_name()
        if character_fill_name
         if 