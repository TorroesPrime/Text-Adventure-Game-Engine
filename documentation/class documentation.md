# class documentation
This is a list of 
* [Interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/class%20documentation.md#interpreter)
* dungeon
* gameState
* adventure
* command
* exit
* room
* character
* item
* weapon
* skill 
* talent

---
# Interpreter
The primary means of interaction between the player and the game itself. The player enters command in a \[verb\]\[item\]\[modifier\]\[target\] syntax to the interpreter that then passes the string to the commandFactory.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_interpreter.md)

---
# dungeon
A dungeon is a collection of rooms that represents an area or location. A dungeon contains at least 1 room and has one room declared to be the ‘entry’ location. The entry is where a player starts in the dungeon when they first start the adventure.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_dungeon.md)

---
# gameState
A gameState is created when the player begins a new play through of an adventure. It contains information about the file used for the adventure, the player character, the dungeon, the player's current room, and any other differences between the adventure file and the current state of a game.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_gameState.md)

---
# adventure
An adventure is a collection of characters, items, events, and challenges that take place within a dungeon. An adventure should have at least 1 “main objective”. 
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_adventure.md)


---
# command
Commands are strings that the user types enters into the interpreter, that are then used to create the requisite commands to allow the user to interact with the game.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_command.md)

---
# exit
An exit represents a connection between two rooms, with one room being the source, and the second being a destination. Exits have a direction, a source room, a destination room, and a number.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_exit.md)

---
# room
A room represents one location in a dungeon. A room can have a “setting type”, ‘lighting’, a list of non-Player Characters, a list of items, a list of exits, a description, and a name of the room. The first time a player enters a room it, the interpreter will display the room name and the description. On subsequent visits, the interpreter will display only the room name. The player can use the ‘look’ command to view the room description.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_room.md)

---
# character
a character represents a person or animal that is comprised of a set of core characteristics, wounds, skills, talents, and an inventory. Characters can “equip” different sorts of items, such as arming themselves with a sword, or wearing a piece of clothing.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_character.md)

---
# item
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_item.md)

---
# weapon
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_weapon.md)

---
# skill
Skill objects represent a proficiency in a particular type of action that a character can perform. This is different from a core characteristic as those represent general capability where has skills are learned. A character may be very intelligent, but if they have never actually studied ciphers then they will have a great deal of trouble attempting to decipher one.
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_skill.md)

---
# talent
Talent objects represent innate abilities and physical traits that a character may have. For instance, a character may have been raised among nobility, granting them a bonus to all tests that involve a member of the nobility. 
see full documentation: [interpreter](https://github.com/TorroesPrime/Text-Adventure-Game-Engine/blob/master/documentation/doc_talent.md)

