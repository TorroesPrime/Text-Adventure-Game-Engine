# Command

## Overview

When the user enters a properly formatted sting into the interpreter, the interpret passes the string to the command_facorty where the string is broken down into a \[verb\]\[item\]\[modifier\]\[target\] syntax  that the command_factory will then use to determine what type of command that is needed to be implimented.

Command is a parent class that the various individual types of command inherrit from.

## The 'Command class'

### fields

  1. commandName
      * a string representing the test version of the command
  2. description
      * a string describing what the command is used for.
  3. usage
      * a string demonstrating how to use the command
  4. usageDetails
      * a string describing possible variants or alternate uses of this command.

### methods

  1. execute()
      * abstract method
  2. details(Self)
      * returns a string that is combination of the commandName, description, or a combination of the commandName, description and usageDetails attributes. Used when reading the help command for a given command.

## List of Commands

  1. look
      * allows the player to view the full description of the room they are currently standing in.
` >>> look `

  2. observe
      * allows the player to perform an ‘awareness’ check on the room they are currently standing. 
      * Example:
' >>> observe '
  3. examine
      * Allows the player to examine a particular item or character. 
Example: >>> examine John Doe
  4. take
      * Allows the player to remove an item from the rooms inventory and place into their player character’s inventory.  Can also use the ‘all’ target to attempt to take all items in the rooms inventory.
  5. drop
      * allows the player to remove an item from their inventory and place it into the current rooms inventory. Can also use the ‘all’ target to empty their entire inventory into the rooms inventory
  6. talk
      * Allows the player to interact with a non-player character by conversing. The command can use the ‘to’ modifier or not, so long as a character name is supplied. If no character name is supplied, the system askes the player who they wish to speak to. The command can also use a ‘about’ modifier to supply a topic to the non-player character.
Example:
Using the ‘to’ modifier
>>> talk to John Doe
Without the ‘to’ modifier
>>> talk John Doe

>>> talk to John Doe about the weather
>>> talk 

  1. move
      * command that allows a player to move from one room to another room via an exit by suppling a direction that corresponds to an exit
Example:
`>>> move w`
  1. throw
      * one means of removing an indicated item from the player inventory.
