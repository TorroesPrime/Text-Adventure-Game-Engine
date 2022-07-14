"""takes string input and constructs command output based on it"""
from rich import inspect
from commands import LookCommand, MovementCommand
MOVEMENT_COMMANDS = "nsweud"

class commandFactory:
    """defines a command"""
    def __init__(self,gameState):
        self.gameState = gameState
    def assembleName(ListEntry):
        '''Assebles a name out of parts of a list.'''
        name = ""
        for item in ListEntry:
            name = name + " " +item
        name = name[:-1]
        return name
    def executeCommand(self,commandString,):
        """command action"""
        command_string = commandString.lower().split(" ")
        if self.gameState.test_value:
            inspect(command_string)
            print("Displaying parts of the commandString")
            for item in command_string:
                print(item)
        #command = blankCommand(self.gameState)
        if command_string[0] == "move" or commandString[0] in MOVEMENT_COMMANDS:
            if command_string[0] == "move":
                if (command_string[1] in MOVEMENT_COMMANDS) == False:
                    print(command_string[1]+" is not a recognized direction. If \
                    you need information about using the 'move' command, type \
                    'help move'.")
                    command = BlankCommand(self.gameState)
                else:
                    command = MovementCommand(self.gameState,command_string[1])
            else:
                command = MovementCommand(command_string[0],self.gameState)
        elif command_string[0] == "look":
            if self.gameState.test_value:
                inspect(self.gameState)
            command = LookCommand(self.gameState)
        elif command_string[0] == "view" and command_string[1] == "stats":
            if self.gameState:
                print("view player line 32")
            if len(command_string)==2:
                if self.gameState:
                    print("view line 35")
                character = self.gameState.player_character
            elif command_string[2] == "for":
                charNameToSeek = ""
                charNameToSeek = commandFactory.assembleName(command_string[3:])
                print("seeking:"+charNameToSeek)
                for character in self.gameState.adventurersCurrentRoom.NonPlayerCharacters:
                    if self.gameState.test_value:
                        print("view line 40")
                        print("NonPlayerCharacter list lenght:"+\
                            str(len(self.gameState.adventurersCurrentRoom.\
                                NonPlayerCharacters)))
                        print("character name: "+character.getFullName()\
                            +":"+command_string[3]+" "+command_string[4])
                        checkName = character.getFullName().lower()
                        print("check name:"+character.getFullName().lower())
                        if checkName == charNameToSeek:
                            if self.gameState:
                                print("view line 43")
                            characcharToFind = self.gameState.adventurersCurrentRoom.getCharacter(checkName)
                            command = view_stats(self.gameState,characcharToFind)
        else:
            command = unknownCommand(commandString)
        return command