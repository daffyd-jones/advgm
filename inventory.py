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
        self.power_up = 0

    def __str__(self) -> str:
        return  f"1 - health potions: {self.health_potion}\n" \
                f"2 - power ups: {self.power_up}"

    def set_health(self, amt):
        self.health_potion = amt

    def set_powerup(self, amt):
        self.power_up = amt

    def health_check(self):
        if self.health_potion > 0:
            return True
        return False

    def power_check(self):
        if self.power_up > 0:
            return True
        return False

    def health_potion_amt(self):
        return self.health_potion

    def power_up_amt(self):
        return self.power_up

    def add_health_potion(self):
        self.health_potion += 1

    def use_health_potion(self):
        self.health_potion -= 1

    def add_power_up(self):
        self.power_up += 1

    def use_power_up(self):
        self.power_up -= 1
