# General concepts:

The following are general descriptions of various terms and phrases that are referred to through out the documentation and planning documents for this project. It is meant to help ensure consistent terminology use and to reduce communication issues.

Adventure
> An adventure is a collection of characters, items, events, and challenges that take place within a dungeon. An adventure should have at least 1 “main objective”. 

Module
> A module is a .adv file that contains the information for all objects that are included in a given adventure.

Main objective
> An adventure should contain a “accomplish this task to win” sort of task. Such tasks could be things like “Bring the Ring of Illioe to the King under the mountain” or “Activate the flood control systems by installing a properly encoded control card into the computer.” 

Secondary objective
> Secondary objectives are tasks within an adventure that can be completed, but do not complete the adventure’s primary story. These objectives may be used to offer secondary rewards to the player, unlock additional options in the adventure, or to trigger other events in the adventure. 

Dungeon
> a dungeon is a collection of rooms that represents an area or location. A dungeon contains at least 1 room and has one room declared to be the ‘entry’ location. The entry is where a player starts in the dungeon when they first start the adventure.

Room
> A room represents one location in a dungeon. A room can have a “setting type”, ‘lighting’, a list of non-Player Characters, a list of items, a list of exits, a description, and a name of the room. The first time a player enters a room it, the interpreter will display the room name and the description. On subsequent visits, the interpreter will display only the room name. The player can use the ‘look’ command to view the room description.

The ‘setting type’ is used to determine what type of the setting the room is.  Such settings could be “formal”, “decrepit”,” Technological”, “Primitive”, “disgusting” etc.

Exit
> An exit represents a connection between two rooms, with one room being the source, and the second being a destination. Exits have a direction, a source room, a destination room, and a number.

Character
> A character represents a person or animal that is comprised of a set of core characteristics, wounds, skills, talents, and an inventory. Characters can “equip” different sorts of items, such as arming themselves with a sword, or wearing a piece of clothing.

Core Characteristics
> A series of 9 numbers, each ranging from 0 to 99 that represent a character’s general capacity in those areas. The core characteristics are: weapon skill, ballistic skill, strength, toughness, agility, intelligence, perception, will power, and fellowship.

Player Character
> A single character that is designated as the “Player Character”. This is the character that the player controls in the game.

Non-player Character:
> A character object that the player does not control but may interact with.

Crafting
> When properly trained, using the proper tools, and working with the proper materials, a player can attempt to craft, or create an item.

Item
> Items are objects that characters can carry in their inventory or can be placed in container in rooms.

Containers
> Containers are non-character objects that have an inventory.

Skills
> Skill objects represent a proficiency in a particular type of action that a character can perform. This is different from a core characteristic as those represent general capability where has skills are learned. A character may be very intelligent, but if they have never actually studied ciphers then they will have a great deal of trouble attempting to decipher one.

Talents
> Talent objects represent innate abilities and physical traits that a character may have. For instance, a character may have been raised among nobility, granting them a bonus to all tests that involve a member of the nobility. 

Test
> A test is when a character attempts to do something that has a chance of failure where the result of failure is notable enough to be communicated to the player. Such tests include characteristic tests, skill tests, and combat tests. The general process of ‘testing’ is that you first determine the difficulty of the challenge to assign a “difficulty modifier” to the test. Then determine what value will determine a “success”. This is a number ranging from 1 to 99. A random number is rolled and any bonus that the character has in their favor is subtracted from the number. This final number is then compared to the number to determine success. If the number to determine success is higher then the final number, the test is passed.

See also: Degrees of success/failure. 

Combat test
> TBD

Commands
> Commands are strings that the user types enters into the interpreter, that are then used to create the requisite commands to allow the user to interact with the game.

See also: List of Commands

Characteristic test
> A characteristic test is used when a character needs to complete a test based on one of their core characteristics.

Skill test
> A skill test is used when a character attempts to use a particular skill to accomplish a task.

Combat test
> TBD

Degrees of success/failure.
> Sometimes how well a character succeeds or fails is relevant, just barely hitting the target versus putting a shot in the dead center of a bull’s eye during a shooting competition for instance or conducting an interrogate where the better the success the more information is revealed for another. The degree of success/failure is a measure of this and is determined by taking the difference between the number needs to pass a given test, and the result of the random number used for the test and dividing it by 10. If the random number was higher this is the degrees of failure and represents how badly the test was failed. If the random number was lower, then this represents how spectacularly they succeeded. 
