# Character

A character represents a person or animal that is comprised of a set of core characteristics, wounds, skills, talents, and an inventory. Characters can “equip” different sorts of items, such as arming themselves with a sword, or wearing a piece of clothing.

Broadly speaking, there are two 'types' of character.

## Player Character

A single character that is designated as the “Player Character”. This is the character that the player controls in the game.

## Non-player Character

A character object that the player does not control but may interact with.

The only "real" difference between a Non-player character and a player character is that the player character is the character object that has been supplied as the [gameState](doc_gameState.md)'s player character attribute.

## Core Characteristics

The core characteristics are a series of 9 numbers, each ranging from 0 to 99 that represent a character’s general capacity in those areas. The core characteristics are stored in a dictionary where the name of the respective skill is the key and the value is the integer. These characrerists are the numbers which most challenges to and by the character will be made again. The core characteristics are:

1. weapon skill
    * The character's general profincency with melee weapons.
    * key name: "weapon_skill"
2. ballistic skill
    * The character's general profincency with ranged attacks.
    * key name: "ballistic_skill"
3. strength
    * The character's physical strength.
    * key name: "strength"
4. toughness
    * The character's ability to resist taking damage when they are attacked or hit.
    * key name: "toughness"
5. agility
    * The character's general speed of motion/reaction.
    * key name: "agility"
6. intelligence
    * The character's intelligence.
    * key name: "intelligence"
7. perception
    * How good the character is at 'seeing' things.
    * key name: "perception"
8. will power
    * The character's general ability to maintain a mental focus/resist mental attacks/mind clouding drugs etc.
    * key name: "will_power"
9. fellowship
    * The character's general likability on a personal level.
    * key name: "fellowship"

## The 'character class'

A character object has the following fields:

### fields

  1. first_name
      * A string representing the character's first name
  2. last_name
      * A string representing the character's last name
  3. characteristics
      * A dictionary of Ints that represents the character stats, which most challenges to and by the character will be made against.
  4. charClass
      * A string representing the type of character this character is. Examples include “Rogue Trader” “Dreg” “Crew Sheneshall” “Warrior” “City Marshal”.
  5. skills
      * a list of [skill](doc_skill.md) objects.
  6. total_wounds
      * An int representing how “tough” the character is, that is how many wounds the character can suffer before being killed.</dd>
  7. current_wounds
      * An int representing how many wounds the character presently have.
  8. fatique
      * An int how tired the character is.
  9. body_parts
      * A dictionary of body part objects, where the name of the body part is the key.
  10. experiencePoints  
      * A int that represents the amount of experience this character has accrued
  11. bonuses
      * a list of strings containing the names of bonuses conveyed by items, weapons, skills, talents or traits.
  12. experience_to_spend
      * When the character levels up, this value represents how much experience that they have left to spend on upgrades and new skills during this level up.
  13. affinity
      * A dictionary where the keys are the names of characters the character has performed an interaction with. The value is an integer that represents how inclined toward the person the character is. A positive integer represents a positive affinity for them, while a negative integer is the opposite.
  14. age
      * An int representing the characters age in years.
  15. appearance  
      * a dictionary whose values are descriptions of physical attributes.

### Methods

  1. addSkills –
      * adds a series of skill objects to the characters skills list.
  2. addItems –
      * adds a series of to the players inventory, unless adding that item will take their players total carry weight above their maximum carry weight.
  3. listSkills –
      * creates a list of ‘basic’ and ‘advanced’ skills that will be used by the generateSkillSection() to list out a character’s skills.
  4. assembleSkills –
      * assembled a list of skills. By default assembles a list of basic skills, but can be set to assemble list of advanced skills instead.
  5. generateCharacteristic–
      * generates 1 core characteristic, an int between 0 and 20 and applies any supplied bonus.
  6. degreeReport–
      * Determines the degree of success/failure of a given test or skill challenge.
  7. charTest–
      * Conducts a characteristics test against the supplied characteristic that is modified by the supplied mod value. Returns a dictionary including the result of the test, and the degree of success or failure.
  8. determineCarryWeight –
      * determines a character’s maximum carry weight.
