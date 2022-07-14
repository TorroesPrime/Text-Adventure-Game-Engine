"""defiens items"""
class Item:
    """"defines item"""
    def __init__(self, *,name="TEST ITEM",weight=10000,
    description=" TEST DESCRIPTION",value=999999999,
    effects=None,item_type = ""):
        self.name = name
        self.weight = weight
        self.description = description
        self.value = value
        self.effects = effects
        self.item_type = item_type

class Weapon(Item):
    """defiens weapon type items"""
    def __init__(self,**kwargs):
        super().__init__()
        self.weapon_class = kwargs.get("class","DEFAULT WEAPON CLASS")
        self.damage_type = kwargs.get("dType","DEFAULT")
        self.damage = kwargs.get("damage",0)
        self.pen = kwargs.get("pen",0)
        self.rate_of_fire = kwargs.get("rof",[False,False,False])
        self.clip = kwargs.get("clip",False)

class Effects:
    """defines effects"""
    def __init__(self,**kwargs):
        self.name = kwargs.get("name","TEST EFFECT")
        self.description = kwargs.get("description","TEST description")
