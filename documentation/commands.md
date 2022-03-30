# Commands

These are the commands that will be availible to players. This document is intended to serve as a disammbiguation source regarding individal commands.

## look
allows the player to view the full description of the room they are currently standing in.

Example: 
```
>>> look
>>> Sturdy glass panels depicting stellar bodies alternate with ancient cogitators and sensorium reporters. Every luminator is held aloft by a lifelike statue, and the eye can travel no more than a few centimetres without encountering some surface inlaid with precious stone or metal. The command throne sits recessed in the rear wall with an arch of cherubs carved above it.
```

## observe
allows the player to perform an ‘awareness’ check on the room they are currently standing. 
Example: 
```
>>> observe
>>> You see nothing of note in the room. People shuffle about tending to their own concerns and wares.
```

## examine
Allows the player to examine a particular item or character. 
Example: 
```
>>> examine John Doe
>>> John seems highly determined to go about business tending to his own cencerns and needs. Your trained eye notices that they are very speccifically attempting to not look in your direction... as if they were worried that you would notice something they would rather you not see if you were to see their face.
```

## take \[item\]
Allows the player to remove an item from the rooms inventory and place into their player character’s inventory.  Can also use the ‘all’ target to attempt to take all items in the rooms inventory.
Example: 
```
>>> take apple
>>> you place an apple in your bag.
>>> take door knob
>>> there is no 'door knob' in the room.
>>> take all
>>> you place an apple, sword, shield, lemon pie and fine mail shirt into your bag.
```
## drop \[item\]
allows the player to remove an item from their inventory and place it into the current rooms inventory. Can also use the ‘all’ target to empty their entire inventory into the rooms inventory
Example: 
```
>>> drop apple
>>> you remove an apple from your bag.
>>> drop door knob
>>> You do not have a 'door knob' in your bag.
>>> drop all
>>> you drop an apple, sword, shield, lemon pie, leather trousers, well made boots, hat and fine mail shirt to the floor of the room.
```

## talk/ talk to
Allows the player to interact with a non-player character by conversing. The command can use the ‘to’ modifier or not, so long as a character name is supplied. If no character name is supplied, the system askes the player who they wish to speak to. The command can also use a ‘about’ modifier to supply a topic to the non-player character.
Example:
Using the ‘to’ modifier
```
>>> talk to John Doe
```

Without the ‘to’ modifier
```
>>> talk John Doe
>>> talk to John Doe about the weather
```

## move
command that allows a player to move from one room to another room via an exit by suppling a direction that corresponds to an exit
Example:
```
>>> move w
```

## throw \[item\]
one means of removing an indicated item from the player inventory.
Example:
```
>>> throw coin
>>> you hurl one coin against the wall. It clatters to the floor.
```

## quit
Allows the player to quit the game. If entered during play, returns the player to the main menu. If entered at the menu menu, closes the program.

## view \[stats\] \ view stats\ view stats for \[character name\]
command to view a character sheet or a specific stat. If ‘view stats’ is entered, it displayers the player character’s stat sheet. If “for” is supplied, it looks for another character with the following name in the room and if it finds one, will view that character’s stat sheet. If ‘view health’ is entered, it displays the health for the indicated character. 

Example:
```
>>> view stats
+----+----+-----+-----+----+-----+-----+----+-----+
| WS | BS | Str | Tgh | Ag | Int | Per | WP | Chr |
+----+----+-----+-----+----+-----+-----+----+-----+
| 99 | 99 |  99 |  99 | 99 |  99 |  99 | 99 |  99 |
+----+----+-----+-----+----+-----+-----+----+-----+

>>> view wounds
+-------------------+---------------------------+
| Total Wounds: 999 | Current Wounds: 999       |
+-------------------+---------------------------+

>>> view damage
+------------------------------------------------------------+
| Present Damage:                                            |
+------+-------+----------+-----------+----------+-----------+
| Head | Torso | Left Arm | Right Arm | Left Leg | Right Leg |
|  0   |   0   |     0    |     0     |     0    |     0     |
+------+-------+----------+-----------+----------+-----------+


>>> view inventory
+-------------------------------------------------------------------------------------+-----------+
| Qty | Item Name                                                                     |  Weight   |
+-------------------------------------------------------------------------------------+-----------+
|  1  | Finely Woven Trader Cloak                                                     | .1 Lbs    |
|  1  | Master Woven Riders left Glove                                                | .01 Lbs   |
|  1  | Master Woven Riders Right Glove                                               | .01 Lbs   |
|  1  | Master Woven Finely detailed trosers                                          | 1.25 Lbs  |
|  1  | Master Woven Finely detailed Tunic                                            | 1.25 Lbs  |
|  5  | Gold Ring                                                                     | .02 Lbs   |
|  1  | Fine Golden Chain                                                             | .02 Lbs   |
|  1  | Castellan's Wraith (Bolt Pistol)                                              | 4.25 Lbs  |
|  1  | Master Crafted Artificer Rapier Sword                                         | 2.25 Lbs  |
|  1  | Some example of a large and heavy item that has a long name longer then re... | 45.99 Lbs |
| 251 | Superb Quality Tracer Bolter Rounds                                           | 6.28 Lbs  |
+-------------------------------------------------------------------------------------+-----------+

>>> view talents
+-------------------------------------------------------------------------------------------------+
| Talents:                                                                                        |
+-------------------------------------------------------------------------------------------------+
| Basic Weapon Training(Prim...   Basic Weapon Training(Prim...   Basic Weapon Training(Prim...   |
| Bastion of Iron Will            Battle Rage                     Ambidextrous                    |
| Binary Chatter                  Armour of Contempt              BladeMaster                     |
| Assassin Strike                                                                                 |
+-------------------------------------------------------------------------------------------------+

>>> view advanced skills
+-------------------------------------------------------------------------------------------------+
| Advanced Skills:                                                                                |
+-----------------------+-----------------------+-----------------------+-------------------------+
| Trade(gems)             Trade(Food)             Trade(Fraud)            Tech-use(Cogitators)    |
| Secret Tongue(Auru...   Secret Tongue(Void...                                                   |
+-------------------------------------------------------------------------------------------------+

>>> view basic skills
+-------------------------------------------------------------------------------------------------+
| Basic Skills:                                                                                   |
+-----------------------+-----------------------+-----------------------+-------------------------+
| Trade(gems)             Trade(Food)             Trade(Fraud)            Tech-use(Cogitators)    |
| Secret Tongue(Auru...   Secret Tongue(Void...                                                   |
+-------------------------------------------------------------------------------------------------+

>>> view skills
+-------------------------------------------------------------------------------------------------+
| Basic Skills:                                                                                   |
+-----------------------+-----------------------+-----------------------+-------------------------+
| Trade(gems)             Trade(Food)             Trade(Fraud)            Tech-use(Cogitators)    |
| Secret Tongue(Auru...   Secret Tongue(Void...                                                   |
+-------------------------------------------------------------------------------------------------+
| Advanced Skills:                                                                                |
+-----------------------+-----------------------+-----------------------+-------------------------+
| Trade(gems)             Trade(Food)             Trade(Fraud)            Tech-use(Cogitators)    |
| Secret Tongue(Auru...   Secret Tongue(Void...                                                   |
+-------------------------------------------------------------------------------------------------+
```


## save
Allows the player to save their game, so they can resume it later.

## rest
Allows the player to rest for a set number of cycles. The cycles are calculated as 10 cycles per hour, with 1 cycle being equivalent to 1 move command or 10 other commands. When the player executes the rest command, prompt will show up asking the player how many in game hours they wish to rest for.
```
>>> rest
How many hours in game should you rest for? 9
after sleeping for 9 hours you awake feeling well rested. The rest allowed you to  heal 1 wound.
```
## craft \[item\]
allows the player to utilized items and materials stored in their inventory to create or attempt to create an item.

## Breakdown \[item\]
allows the player to attempt to break down indicated item into its components materials.

## attack \[target\]
Allows the player to initiate "combat" against a selected target.

## arm \[weapon\]
Command to allow the player arm their character with an indicated weapon
Example:
```
>>> arm bolter
```

## disarm
Command to allow the player to disarm their characters.

## equip \[item\]
Command to allow the player to equip a clothing or armor type item.
Example:
```
>>> equip Gilded Cuirass
You strap the gilded cuirass on.
>>> equip dlog tunic
You do not have any clothing or armor item named 'dlog tunic'
```

## unequip \[item\]
Command to allow the player to unequip a clothing or armor type item.
Example:
```
>>> unequip Gilded Cuirass
You remove the gilded cuirass.
>>> unequip dlog tunic
You are not anything named 'dlog tunic'
```

## help / help \[command\]
Command to allow the player to use the help menu, or view the help info for a supplied command.