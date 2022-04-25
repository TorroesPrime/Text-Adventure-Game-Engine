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


## Interpreter
The primary means of interaction between the player and the game itself. The player enters command in a \[verb\]\[item\]\[modifier\]\[target\] syntax to the interpreter that then passes the string to the commandFactory.

* #### verb 
> this part of a command will tend to be an action of some sort. ‘talk to’ ‘take’ ‘move’ ‘examine’ etc.
* #### item
> this is the item that the verb is targeted on. So if the command ‘take apple’ is entered, ‘apple’ is the item.
* #### modifier
> for more complex commands, a modifier is used to connect an item to a target. An example of which would be: view stats for John. The verb is ‘view’ while the item is ‘stats’, but the modifier ‘for’ means we want to view the stats of something other than the player character.
*target
> the target a modified command. 

### fields
* #### commandCursor
> indicates what the character(s) that are displayed on the command line to the user.
Example:
```
>>> arm bolter
```
the `>>>` is the commandCursor.

### methods
* #### promptUser
> provides the command curser for the user

* #### interpreter
> Primary interaction method. 

## dungeon
> A dungeon is the 'map' or region that a given adventure occures in. A dungeon contains at least 1 room and a room that is designated as 'entry', where the player starts when they begin a new adventure.
### fields
* #### title
> a string representing the name of the dungeon.
* #### entry
> a room object where the player begins a new adventure.
* #### rooms
> a dictionary that uses the room name as the key and the associated room object as the value.
* #### characters
> a list of character objects that are availible in this dungeon.
* #### items
> a list of items that are in the dungeon.

### methods
* #### storeState
> writes the current state of the dungeon to a .sav file.
* #### restoreState
> reads the contents of a .sav file to restore a dungeon to the state indicated in the file.
* #### addRooms
> add the contents of a list of a rooms to the dungeon's rooms field.
* #### getRoom
> returns a room object by searching for the name in the dungeon's rooms.

## gameState
> A gameState is created when the player begins a new play through of an adventure. It contains information about the file used for the adventure, the player character, the dungeon, the player's current room, and any other differences between the adventure file and the current state of a game.

### fields
* #### saveFileVersion
> a string representing the supported version of the game engine used for this gameState.

* #### currentRoomLeader
> A string “Current room: “ that is used to record the player’s current room in a .sav file.

* #### defaultSaveFileName
> A string used as the default file name for .sav files created when this game state executes a save command.

* #### dungeon
> the dungeon object for this game.

* #### adventurersCurrentRoom
> a room object that the player's character currently occupies.

* #### testValue
> A boolean used to control whether trouble shooting functions are enabled or not.

* #### playerCharacter
> Character object that the player controls.

### methods
* #### storeState
> method to record the current gamestate to a save file.
Below is a list of the various object types in the system. Click on a given name to be taken to a brief overview of the object. 
* #### getAdventurersCurrentRoom
> returns the room that the player character currently occupies.

* #### setAdventurersCurrentRoom
> sets the adventurersCurrentRoom as the player character moves from room to room.

* #### setPlayerCharacter 
> sets the playerCharacter for this gameState.


## adventure
### fields
### methods

## command
### fields
### methods

## exit
### fields
### methods

## room
### fields
### methods

## character
### fields
### methods

## item
### fields
### methods

## weapon
### fields
### methods

## skill
### fields
### methods

## talent
### fields
### methods
