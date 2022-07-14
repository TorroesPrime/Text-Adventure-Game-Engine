"""Module to create needed commands for the game"""
class Command():
    """command super class definition"""
    def __init__(self,game_state,command_name="command name",description="",\
        usage ="",usage_details=""):
        self.command_name = command_name
        self.description =description
        self.usage =usage
        self.usage_details =usage_details
        self.game_state= game_state
        self.command_string = ""
    def get_str(self):
        """returns the example of using the command"""
        return self.command_string
    def execute(self):
        """what the command does"""
        print("This is the ",self.command_name,"class")
    def details(self,details):
        """contains information about the command to be used when the help \
        command is called for this command."""
        if details is not True:
            response = " - "+self.command_name+": "+self.description
        else:
            response =  " - "+self.command_name+": "+self.description+"\nUsage \
            Example: "+self.usage_details
        return response

class BlankCommand(Command):
    """Blank command"""
    def execute(self):
        return ""

class LookCommand(Command):
    """command to allow the user to view the contents and description of the \
        room they current occupy."""
    def __init__(self,game_state):
        super().__init__(game_state,command_name = "Look Command",\
            description = "Allows the user to view the full description of the room they currently\
             occupy.",
            usage = "> look\n [full description of the room]",
            usage_details = "",)

    def execute(self):
        """returns the adventurers current room's description"""
        return self.game_state.adventurers_current_room.full_describe()

class MovementCommand(Command):
    """movement command"""
    commandString = ""
    MOVEMENT_COMMANDS = "nsweud"
    def __init__(self,game_state,direction):
        super().__init__(game_state,command_name = "move Command",\
        description = "Allows the user to move from one room to another by \
        supplying an intended direction to move.",
        usage = "> move n\n [move from the current room to the joining room \
        via the north door, if such a door exist.]",
        usage_details = "")
        self.direction = direction
    def execute(self):
        nextRoom = self.game_state.adventurers_current_room.leave_by(self.direction)
        if nextRoom != None:
            self.game_state.adventurers_current_room=nextRoom
            print(self.game_state.adventurers_current_room.describe())
            self.game_state.adventurers_current_room.been_here = True
        else:
            print(f"Sorry, you can't go {self.direction} from \
{self.game_state.adventurers_current_room.name}.")
