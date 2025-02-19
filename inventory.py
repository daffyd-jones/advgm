from enums import InvItem

#   - Inventory Class
#
#   used to manage inventory
#
#   - propery of State Class as:
#       self.inventory = Inventory()
#   - used in State.use_inventory() as
#       self.inventory.health_check and self.inventory.power_check
#
#   - methods:
#       set_health(amt)
#       - sets self.hp to amt
#       set_powerup(amt)
#       - sets self.power_up to amt
#       health_check()
#       - checks if the number of health potions is > 0
#       power_check()
#       - checks if the number of power ups is > 0
#       health_potion_amt()
#       - returns number of health potions
#       power_up_amt()
#       - returns number of power ups
#       add_health_potion()
#       - increment self.health_potion by 1
#       use_health_potion()
#       - decrements self.health_potion by 1
#       add_power_up()
#       - increment self.power_up by 1
#       use_power_up()
#       _increment self.power_up by 1
#
class Inventory:
    def __init__(self):
        self.health_potion = 0
        self.strength_potion = 0
        self.agility_potion = 0
        self.defence_potion = 0
        self.bread_hunk = 0

    def __str__(self) -> str:
        return  f"1 - health potions: {self.health_potion}\n" \
                f"2 - power ups: {self.power_up}"

    def use_item(self, item):
        match item:
            case InvItem.HEALTH_POTION:
                self.health_potion -= 1;
            case InvItem.STRENGTH_POTION:
                self.strength_potion -= 1;
            case InvItem.AGILITY_POTION:
                self.agility_potion -= 1;
            case InvItem.DEFENCE_POTION:
                self.defence_potion -= 1;
            case InvItem.BREAD_HUNK:
                self.bread_hunk -= 1;

    def get_inventory(self):
        out = []
        if self.health_potion > 0:
            out.append(f'Health Potion: {self.health_potion}')
        if self.bread_hunk > 0:
            out.append(f'Bread Hunk: {self.bread_hunk}')
        if self.stength_potion > 0:
            out.append(f'Strength Potion: {self.stength_potion}')
        if self.agility_potion > 0:
            out.append(f'Agility Potion: {self.agility_potion}')
        if self.defence_potion > 0:
            out.append(f'Defence Potion: {self.defence_potion}')
        return out

    def add_item(self, item):
        match item:
            case InvItem.HEALTH_POTION:
                self.health_potion += 1;
            case InvItem.STRENGTH_POTION:
                self.strength_potion += 1;
            case InvItem.AGILITY_POTION:
                self.agility_potion += 1;
            case InvItem.DEFENCE_POTION:
                self.defence_potion += 1;
            case InvItem.BREAD_HUNK:
                self.bread_hunk += 1;
        
