from character import Character
from skill import *
from item import *
from skills import skill_library
from rich import inspect, print as RP
from prettytable import PrettyTable
from room import *
from exit import *

r1 = Room("Room One","Just a place holder string describing the first room")
r2 = Room("Room Two","Just a place holder string describing room two")
r3 = Room("Room Three","Just a place holder string describing the Room Three")
r4 = Room("Room Four","Just a place holder string describing the Room four")
e102 = Exit("w",r1,r2)
e103 = Exit("n",r1,r3)
e201 = Exit("e",r2,r1)
e204 = Exit("n",r2,r4)
e302 = Exit("s",r3,r1)
e304 = Exit("e",r3,r4)
e403 = Exit("w",r4,r3)
e402 = Exit("s",r4,r2)
def getCharacter(characterName):
    global characters_list
    for charEntry in characters_list:
        if charEntry.get_full_name() == characterName:
            return charEntry

characters_list =[]
character_data = [
    ["Naj","Amaradi",17,17,26,30,14,17,31,27,14,22,"Rogue Trader"],
    ["Aristide","Anzaforr",30,17,18,26,32,29,14,30,16,17,"Nova Marine"],
    ["Charlabelle","Armelan",22,20,15,17,17,15,20,24,25,15,"Nightmare Ghost"],
    ["Jeremiah","Armengarde",28,31,16,16,26,16,26,27,26,16,"Legionare"],
    ["Valerius","Bastille",	14,32,18,31,23,30,22,25,17,17,"storm bringer"],
    ["Kinker","Blitz",	22,21,18,16,24,28,32,16,27,17,"storm bringer"],
    ["Salgut","Borodin",19,28,31,22,27,19,15,23,19,25,"Explorator"],
    ["Krawkin","Chorda",30,31,17,14,29,32,31,28,27,17,"Explorator"],
    ["Aoife","Dallactarius",18,15,32,32,20,27,21,22,25,26,"Explorator"],
    ["Aspyce","Drub",19,19,25,24,27,29,25,16,28,22,"Explorator"],
    ["Sun","Falk",28,30,26,20,29,14,19,17,32,22,"Explorator"],
    ["Hesiah","Feckward",19,29,20,16,27,29,19,18,26,19,"Explorator"],
    ["Aada","Alfit",15,19,30,31,31,18,22,31,15,25,"Explorator"],
    ["Aallotar","Errit",19,21,18,26,24,25,18,14,27,17,"Explorator"],
    ["Diaz","Lan",38,52,35,41,44,52,43,39,47,17,"Rogue Trader"]
]
diaz_lan_skills_list =["Awareness", "Carouse","Charm","Command","Common Lore(Imperium)",\
    "Common Lore(Rogue Trader)", "Deceive","Dodge","Evaluate","Forbidden Lore(Xenos)",\
    "Literacy","Pilot(space craft)","Scholastic Lore(Astromancy)","Scrutiny",\
    "Speak Language(Low Gothic)","Speak Language(High Gothic)","Speak Language(Eldar)",\
    "Tech-Use"]
skillData = []
for entry in skill_library.values():
    if len(entry) == 4:
        skillData.append(skill(entry[0],entry[1],entry[2],entry[3]))
    elif len(entry)==5:
        skillData.append(skill(entry[0],entry[1],entry[2],entry[3],entry[4]))
#for skillItem in skillData:
#    print(skillItem.name)
for entry in character_data:
    fName = entry[0]
    lName = entry[1]
    WS = entry[2]
    BS = entry[3]
    Strength = entry[4]
    Toughness = entry[5]
    Agility = entry[6]
    Intelligence = entry[7]
    Perception = entry[8]
    WP = entry[9]
    Fell = entry[10]
    charClass = entry[11]
    tWounds = entry[12]
    characters_list.append(Character(fName,lName,WS,BS,Strength,Toughness,\
        Agility,Intelligence,Perception,WP,Fell,tWounds,charClass))

test_char = getCharacter("Diaz Lan")
for skillEntry in diaz_lan_skills_list:
    name = skill_library[skillEntry][0]
    characteristic = skill_library[skillEntry][1]
    advanced = skill_library[skillEntry][2]
    descrip = skill_library[skillEntry][3]
    test_char.add_skill([skill(name,advanced,characteristic,descrip=descrip)])

charData = getCharacter("Diaz Lan")
skillsList =[]
count = 0   
for item in charData.skills:
    skillsList.append(item.name)

listOfSkillNames = [
    ['Awareness','Carouse','Charm','Command',],
    ['Common Lore(Imperium)','Common Lore(Rogue Trader)','Deceive','Dodge'],
    ['Evaluate','Forbidden Lore(Xenos)','Literacy','Pilot(space craft)'],
    ['Scholastic Lore(Astromancy)','Scrutiny','Speak Language(Low Gothic)','Speak Language(High Gothic)'],
    ['Speak Language(Eldar)','Tech-Use','','']
]
section = PrettyTable()
section.field_names=["Skills"]

#section.add_row(tableContents)
min = 0
name = ""
for entry in skillData:
    if len(entry.name) > min:
        min = len(entry.name)
        name = entry.name

print("longest name: "+name)
print("length: ",min)
tableContents = PrettyTable()
tableContents.title = "Skills"
tableContents.header = False
for row in listOfSkillNames:
    tableContents.add_row(row)


RP(tableContents)

inspect(r1)