# Adventure

An adventure is a collection of characters, items, events, and challenges that take place within a dungeon. These materials are stored in a file with a .adv extension. Adventure files, or “Adventure modules” are stored in a first level folder designated “adv”. 
The .adv file is structured as follows:

1. Adventure Meta data: This includes the following:
    * name of the adventure
    * the Author’s name
    * any social media links/email addresses the Author has included in the module
    * a description that the author as provided for the adventure
    * the release date of the adventure
    * what version of the engine the module was written in.
2. Items: This will be a series of entries that contain the materials for all of the items that will be available in the dungeon. 
    * See items for more information
3. Characters: this section will include a series of entries that contain the information for all the characters that will be available in this adventure.
    * See character for more information.
4. Rooms: This section with include a series of entries that contain the information for all of the rooms in the dungeon. 
    * For more information see room.
5. Exits: This section contains a series of entries that contain the information for all of the exits in the dungeon. 
    * For me information, see exit.

Excluding the meta data, each of these sections will be stored as a list of dictionaries with each dictionary containing the information for one entry.

## The 'Adventure class'

### fields
<dl>
    <dt>fileName</dt>
    <dd>a string representing the file name of the adventure module. This is used to ensure continuity between play sessions that use this adv module. If the engine ever needs to compare the current gameState to what was in the original file, this ensures that it will know what file to look for.</dd>
    <dt>description</dt>
    <dd>A String that describes the adventure module. This would be provided by the adventure writer.</dd>
    <dt>name</dt>
    <dd>A string representing the name of the adventure module</dd>
    <dt>author_name</dt>
    <dd>a string representing the name of the adventure module’s writer.</dd>
    <dt>author_social_media</dt>
    <dd>A dictionary containing a series of strings that represent whatever social media information the adventure writers has chosen to provide.</dd>
    <dt>release_date</dt>
    <dd>A date object representing the date that the module was ‘published’.</dd>
    <dt>game_version</dt>
    <dd>A string representing the version of the Game Engine that the module was built under. In theory later versions of the engine will support modules built with earlier versions.</dd>
</dl>

## 