"""skills module"""
import random
class skill:
    """defines a skill object"""
    def __init__(self,
     skill_name: str = "TEST SKILL NAME",
     advanced: bool = False,
     characteristic: str = "TEST SKILL INFO",
     descrip: str="TEST DESCRIPTION",
     skill_level: int = 0,
     dialect: str = "",
     ): 
        self.name = skill_name  
        self.advanced = advanced
        self.characteristic = characteristic
        self.descrip = descrip
        self.skill_level = skill_level
        self.dialect = dialect
    def getBonus(self):
        return self.skill_level/10
    def printInfo(self):
        print("Skill Name:",self.name,"("+self.characteristic+")")
        
    
class skillGroup(skill):
    intList = ["Archaeologist","Cryptographer","Technomat","Explorator","Linguist","Chymist","Shipwright"]
    felList = ["Soothsayer ","Trader"]
    agList = ["Voidfarer","Armourer","Astrographer"]
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.skillNameType = kwargs.get("name","SKILL GROUP")+"("
        self.skillSubject = kwargs.get("subject","SUBJECT")
        self.name = self.getSkillName()
        if self.skillSubject in skillGroup.intList:
            self.characteristic="Intelligence"
        elif self.skillSubject in skillGroup.felList:
            self.characteristic="Fellowship"
        elif self.skillSubject in skillGroup.agList:
            self.characteristic="Agility"
        elif self.skillSubject == "Remembrancer":
            self.skillSubject = random.choice("Agility","Intelligence")
    def getSkillName(self):
        if "_ship_name_" in self.skillSubject:
            subject = self.skillSubject.replace("_ship_name_","[ship]")
        else:
            subject = self.skillSubject
        return self.skillNameType+subject+")"
