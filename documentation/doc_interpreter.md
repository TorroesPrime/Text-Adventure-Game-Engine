# Interpreter
The primary means of interaction between the player and the game itself. The player enters command in a \[verb\]\[item\]\[modifier\]\[target\] syntax to the interpreter that then passes the string to the commandFactory.

* ### verb 
> this part of a command will tend to be an action of some sort. ‘talk to’ ‘take’ ‘move’ ‘examine’ etc.
* ### item
> this is the item that the verb is targeted on. So if the command ‘take apple’ is entered, ‘apple’ is the item.
* ### modifier
> for more complex commands, a modifier is used to connect an item to a target. An example of which would be: view stats for John. The verb is ‘view’ while the item is ‘stats’, but the modifier ‘for’ means we want to view the stats of something other than the player character.
*target
> the target a modified command. 

## fields
* ### commandCursor
> indicates what the character(s) that are displayed on the command line to the user.
Example:
```
>>> arm bolter
```
the `>>>` is the commandCursor.


## methods
* #### promptUser
> provides the command curser for the user.
