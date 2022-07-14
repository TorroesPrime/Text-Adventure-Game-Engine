"""exit module"""
from room import Room
class Exit:
    """creates exits for use in a dungeon."""
    def __init__(self,
    direction: str = "",
    source_room: Room = "",
    destination_room: Room = ""):
        self.direction = direction
        self.source_room = source_room
        self.destination_room = destination_room
        self.source_room.add_exits([self])
       # self.source_room.add_exit(self)

    def manuel_exit(self,direction,source_room,destination_room):
        """manual constructor method used for testing and dev."""
        self.direction = direction
        self.source_room = source_room
        self.destination_room = destination_room
        self.source_room.add_exits([self])
        return self
    def get_destination(self):
        """returns the name of the of the destinaiton room"""
        return self.destination_room
    def get_direction(self):
        """returns the direction of the exit"""
        return self.direction
    def describe(self):
        """returns a string describing what room this exit leads to."""
        return f"You can go <{self.direction}> to the {self.destination_room.name}."
