# import os
import json
from os import name
import os
from random import random
from random import seed
from enum import Enum, auto

def remfront(st):
    remain = st[1:]
    return remain

# - Inventory Item Enum
# 
#   used to differentiate inventory item type
#
#   - used in State.in
#  
#  
class InvItem(Enum):
    HEALTH_POTION = auto()
    POWER_UP = auto()

# - Scenes Enum
# 
#   used to differentiate scene functions 
#   
#   - used in State.SceneMap as Scenes.BEGINNING: Beginning
#   - Beginning as used above refers to def Beginning(state): <- scene function
#   - def Beginning(state): is run in State.play as:
#       self.current_scene, self.scene_hold = self.sceneMap[self.current_scene](self)
#       - self.sceneMap[self.current_scene](self) == def Beginning(state):
# 
class Scenes(Enum):
    MENU = 'menu'
    INVENTORY = 'inv'

    BEGINNING = 'beginning' # -> MOUNTAIN_PATH, ENTER_FOREST, POND_APPROACH
    CLEARING = 'clearing'  # -> MOUNTAIN_PATH, ENTER_FOREST, POND_APPROACH
    # pond
    POND_APPROACH = 'pondApproach' # -> POND_THROWROCK, POND_JUMP, CLEARING
    POND_THROWROCK = 'pondThrowback' # -> POND_JUMP, CLEARING
    POND_JUMP = 'pondJump' # -> POND_DOWN, POND_CAVE_3, POND_OUT 
    POND_OUT = 'pondOut' # -> POND_JUMP, CLEARING
    POND_DOWN = 'pondDown' # -> GRAB_PENDANT, POND_BACK
    POND_BACK = 'pondBack' # -> POND_DOWN, POND_CAVE_3, POND_OUT
    GRAB_PENDANT = 'grabPendant' # -> POND_OUT
    # pond cave 
    # - may have different versions of each room for every enterance
    # - if 1 version exists per room the description of each must be 
    # - written to make sense from all directions ex. opening behind a rock
    # - as opposed to providing more organic directional 
    # - experience ex. opening to the left and ahead
    POND_CAVE_1 = 'pondCave1'  # -> 2
    POND_CAVE_2 = 'pondCave2'  # -> 1, 3, 7
    POND_CAVE_3 = 'pondCave3'  #pond entrance -> 2, 4
    POND_CAVE_4 = 'pondCave4'  # -> 3, 5, 9
    POND_CAVE_5 = 'pondCave5'  # -> 4
    POND_CAVE_6 = 'pondCave6'  # -> 7, 11
    POND_CAVE_7 = 'pondCave7'  # -> 2, 6, 8
    POND_CAVE_8 = 'pondCave8'  # -> 7, 13
    POND_CAVE_9 = 'pondCave9'  # -> 4, 10
    POND_CAVE_10 = 'pondCave10' # -> 9, 15
    POND_CAVE_11 = 'pondCave11' # -> 6, 
    POND_CAVE_12 = 'pondCave12' # -> 13, 17
    POND_CAVE_13 = 'pondCave13' # -> 8, 12, 14
    POND_CAVE_14 = 'pondCave14' # -> 13, 15, 19
    POND_CAVE_15 = 'pondCave15' # -> 10, 14
    POND_CAVE_16 = 'pondCave16' #mountain entrance -> 17
    POND_CAVE_17 = 'pondCave17' # -> 12, 16, 18
    POND_CAVE_18 = 'pondCave18' # -> 17, 
    POND_CAVE_19 = 'pondCave19' # -> 14, 20
    POND_CAVE_20 = 'pondCave20' #forest entrance -> 19
    # Forest
    # - forest entrance
    ENTER_FOREST = 'enterForest' # -> CLEARING, FOREST_PATH
    FOREST_PATH = 'forestPath' # -> LIGHT_VILLAGE
    LOST_IN_FOREST = 'lostInForest'
    # - light village
    LIGHT_VILLAGE = 'lightVillage' # -> CEREMONY_OF_LIGHT
    CEREMONY_OF_LIGHT = 'cermonyOfLight' # -> COL_ENCOUNTER
    # - ceremony of light conflict 
    COL_ENCOUNTER = 'COLConflict' # -> BACKWOODS

    # - back of forest
    BACKWOODS = 'backwoods' # -> ENTER_FOREST, FOREST_CAVE_CLEARING_IN, FOREST_PUZZLE
    # - some kind of puzzle thing
    FOREST_PUZZLE = 'forestPuzzle' # -> BACKWOODS, FOREST_MOUNTAIN_PATH
    FOREST_MOUTAIN_PATH = 'forestMountainPath' # -> FOREST_PUZZLE, MOUNTAIN_BASE
    # - forest pond cave entrance
    FOREST_CAVE_CLEARING_IN = 'forestCaveClearingIn' # -> BACKWOODS, FOREST_CAVE_ENTRANCE_IN
    FOREST_CAVE_CLEARING_OUT = 'forestCaveClearingOut' # -> BACKWOODS, FOREST_CAVE_ENTRANCE_IN
    FOREST_CAVE_ENTRANCE_IN = 'forestCaveEntranceIn' # -> POND_CAVE_20, FOREST_CAVE_CLEARING_OUT
    FOREST_CAVE_ENTRANCE_OUT = 'forestCaveEntranceOut' # -> POND_CAVE_20, FOREST_CAVE_CLEARING_OUT

    # Mountain
    # - mountain path
    MOUNTAIN_PATH = 'mountainPath' # -> CLEARING, MOUNTAIN_PATH_2
    MOUNTAIN_PATH_2 = 'mountainPath2' # -> MOUNTAIN_PATH, MOUNTAIN_BASE

    # - mountain base
    MOUNTAIN_BASE = 'mountainBase' # -> MOUNTAIN_PATH_2, MOUNTAIN_ENTRANCE, FOREST_MOUNTAIN_PATH
    MOUNTAIN_ENTRANCE = 'mountainEntrance' # -> MOUNTAIN_BASE, M_LVL1_R1
    # - mountain lvl 1
    M_LVL1_R1 = 'mLVLR1' # -> MOUNTAIN_ENTRANCE, MOUNTAIN_CAVE_ENTRANCE
    MOUNTAIN_CAVE_ENTRANCE = 'mountainCaveEntrance' # -> M_LVL1_R1, M_LVL1_STAIRS, POND_CAVE_16
    M_LVL1_STAIRS = 'mLVL1Stairs' # -> M_LVL2_R1, MOUNTAIN_CAVE_ENTRANCE
    # - mountain lvl 2
    M_LVL2_R1 = 'mLVL2R1' # -> M_LVL1_STAIRS, M_LVL2_STAIRS
    M_LVL2_STAIRS = 'mLVL2Stairs' # -> M_LVL2_R1, M_LVL3_R1
    # - mountain lvl 3
    M_LVL3_R1 = 'mLVL3R1' # -> M_LVL2_STAIRS, M_LVL3_STAIRS
    M_LVL3_STAIRS = 'mLVL3Stairs' # -> M_LVL3_R1, BOSS_AREA
    # - boss area 
    BOSS_AREA = 'bossArea' # -> M_LVL3_STAIRS

# - State Class
# 
#   used to manage gamestate variables and functions
# 
#   - passed to scene functions for state changes
#   
#   - used in main() as:
#       state = State()
#       state.play()
# 
#   - methods:
#       play()
#       - game loop
#       - checks if self.current_scene is Scenes.INVENTORY or Scenes.MENU and 
#       runs State.use_inventory or State.use_menu respectively
#       - else the current scene function is run by:
#           self.current_scene, self.scene_hold = self.sceneMap[self.current_scene](self)
#      
#       use_menu()
#       - runs menu
#       - prints menu options
#       - in loop response is checked and run until continue or exit are selected
#       - if save or load are selected state variables are serialized or deserialized
#   
#       use_inventory()
#       - runs inventory
#       - prints inventory and asks which the user would like to use
#       - in loop response is checked and run until exit is selected
#       - if 1 (health potion) is selected 10 hp is added to self.hp 
#       - if 2 (power up) is selected 2 is added to self.hit_rate
# 
#       hp_dec(amt)
#       - decrements self.hp by amt 
#       
#       encounter(encounter_map, probOfAttack)
#       - runs enemy encounter
#       - checks if probability of encounter is 1 (100%)
#       - if not, generates random number 0-1 (num) and checks if num is less than probOfAttack  
#       - if so the function returns true, else the function is continued
#       - intro text for encounter is printed and encounter variables are instantiated
#       - coin if flipped to determine who has first move
#       - in loop check if you_turn is true or false and runs player or npc portions
# 
#       - player portion asks if player would like to ATTACK, take a HEALTH potion or a POWER up
#       - if response is HEALTH or POWER self.use_health_potion() or self.use_power_up()
#       - if ATTACK then a "die" is rolled for attack 
#       - if roll is higher than npcs defense then self.hit_rate is decremented from npcs hp
#  
#       - npc portion rolls for attack and if roll is higher than self.defense, self.hp is  
#       decremented by npcs hit rate
# 
#       - at the end of each loop self.ph and npcs hp are checked and if either are dead a message is 
#       printed and function returns True (player wins) or False (player dies)
# 
#       hp_dec(amt)
#       - decrements self.hp by amt
# 
#       change_scene(scene)
#       - changes self.current_scene to scene
# 
# 
class State:
    def __init__(self):
        self.play_bool = False
        self.hp = 50
        self.defence = 10
        self.hit_rate = 5
        self.attack = 10
        self.current_scene = Scenes.BEGINNING
        self.scene_hold = Scenes.BEGINNING
        self.inventory = Inventory()
        self.inv_prize = {
            InvItem.HEALTH_POTION: self.inventory.add_health_potion(), 
            InvItem.POWER_UP: self.inventory.add_power_up()
        }
        self.sceneMap = {
            Scenes.BEGINNING: Beginning,
            Scenes.ENTER_FOREST: enterForest,
            Scenes.CLEARING: Beginning2,
            Scenes.POND_APPROACH: PondApproach,
            Scenes.POND_THROWROCK: Throwrock,
            Scenes.POND_JUMP: pondJump,
            Scenes.POND_DOWN: pondDown,
            Scenes.GRAB_PENDANT: grabPendant,
            Scenes.POND_OUT: pondOut,
            Scenes.POND_BACK: pondBack,
            Scenes.FOREST_PATH: forPath,
            Scenes.LIGHT_VILLAGE: lightVillage,
            Scenes.CEREMONY_OF_LIGHT: ceremonyOfLight,
            Scenes.COL_ENCOUNTER: COLEncounter,
            Scenes.BACKWOODS: backwoods,
            Scenes.FOREST_PUZZLE: forestPuzzle,
            Scenes.FOREST_MOUTAIN_PATH: forestMountainPath,
            Scenes.FOREST_CAVE_ENTRANCE_IN: forestCaveEntranceIn,
            Scenes.FOREST_CAVE_ENTRANCE_OUT: forestCaveEntranceOut,
            Scenes.FOREST_CAVE_CLEARING_IN: forestCaveClearingIn,
            Scenes.FOREST_CAVE_CLEARING_OUT: forestCaveClearingOut,
            Scenes.POND_CAVE_1: pondCave1,
            Scenes.POND_CAVE_2: pondCave2,
            Scenes.POND_CAVE_3: pondCave3,
            Scenes.POND_CAVE_4: pondCave4,
            Scenes.POND_CAVE_5: pondCave5,
            Scenes.POND_CAVE_6: pondCave6,
            Scenes.POND_CAVE_7: pondCave7,
            Scenes.POND_CAVE_8: pondCave8,
            Scenes.POND_CAVE_9: pondCave9,
            Scenes.POND_CAVE_10: pondCave10,
            Scenes.POND_CAVE_11: pondCave11,
            Scenes.POND_CAVE_12: pondCave12,
            Scenes.POND_CAVE_13: pondCave13,
            Scenes.POND_CAVE_14: pondCave14,
            Scenes.POND_CAVE_15: pondCave15,
            Scenes.POND_CAVE_16: pondCave16,
            Scenes.POND_CAVE_17: pondCave17,
            Scenes.POND_CAVE_18: pondCave18,
            Scenes.POND_CAVE_19: pondCave19,
            Scenes.POND_CAVE_20: pondCave20,
            Scenes.MOUNTAIN_PATH: mountainPath1,
            Scenes.MOUNTAIN_PATH_2: mountainPath2,
            Scenes.MOUNTAIN_BASE: mountainBase,
            Scenes.MOUNTAIN_ENTRANCE: mountainEntrance,
            Scenes.M_LVL1_R1: mLvl1R1,
            Scenes.MOUNTAIN_CAVE_ENTRANCE: mountainCaveEntrance,
            Scenes.M_LVL1_STAIRS: mLvl1Stairs,
            Scenes.M_LVL2_R1: mLvl2R1,
            Scenes.M_LVL2_STAIRS: mLvl2Stairs,
            Scenes.M_LVL3_R1: mLv32R1,
            Scenes.M_LVL3_STAIRS: mLvl3Stairs,
            Scenes.BOSS_AREA: bossArea,
        }

    def __str__(self) -> str:
        return  f'\n--------'\
                f'\nhp: {self.hp}\n'\
                f"atk: {self.hit_rate}\n"\
                f'--------\n'

    def play(self):
        self.play_bool = True
        os.system('cls' if os.name == 'nt' else 'clear')
        while self.play_bool:     
            if self.current_scene == Scenes.INVENTORY:
                self.use_inventory()
            if self.current_scene == Scenes.MENU:
                self.use_menu()
            self.current_scene, self.scene_hold = self.sceneMap[self.current_scene](self)



    def use_menu(self):
        self.current_scene = self.scene_hold
        print("-- Menu --")
        print("1 - continue")
        print("2 - save")
        print("3 - load")
        print("4 - exit")
        while True:
            res = str(input(": ")).upper()
            if res == "1" or res == "CONTINUE":
                return None
            elif res == "2" or res == "SAVE":
                # serialize
                save_data = {
                    "hp": self.hp,
                    "defence": self.defence,
                    "hit_rate": self.hit_rate,
                    "attack": self.attack,
                    "current_scene": self.current_scene,
                    "inventory": [
                        self.inventory.health_potion_amt(),
                        self.inventory.power_up_amt()
                    ]
                }
                with open('file.json', 'w') as f:
                    json.dump(save_data, f, sort_keys=True, default=lambda x: x.value)
                    print("game saved")
            elif res == "3" or res == "LOAD":
                # deserialize
                with open('file.json') as f:
                    data = json.load(f)
                    self.hp = data["hp"]
                    self.defence = data["defence"]
                    self.hit_rate = data["hit_rate"]
                    self.attack = data["attack"]
                    self.current_scene = Scenes(data["current_scene"])
                    self.inventory.set_health(data["inventory"][0])
                    self.inventory.set_powerup(data["inventory"][1])
                    print("game loaded")
            elif res == "4" or res == "EXIT":
                self.play_bool = False
                return None
            else:
                print("Not a valid response")

    def level_up(self, hp, defence, attack):
        self.hp = hp
        self.defence = defence
        self.attack = attack

    def use_inventory(self):
        self.current_scene = self.scene_hold
        print(self.inventory)
        print("which would you like to use?")
        print("EXIT to close inventory")
        print("1, 2, EXIT")
        menu = True
        while menu:
            response = str(input(": ")).upper()
            if response == "1":
                if self.inventory.health_check:
                    self.hp += 10
                    print("health + 10")
                    print(f"health is now {self.hp}")
                else:
                    print("no health potions available")
            elif response == 2:
                if self.inventory.power_check:
                    self.hit_rate +=  2
                    print("hit_rate + 2")
                    print(f"hit_rate is now: {self.hit_rate}")
                else:
                    print("no power ups available")
            elif response == "EXIT":
                menu = False
            else:
                print("not a valid input")

    def hp_dec(self,amt):
        self.hp -= amt


    def encounter(self, probOfAttack, encounterMap):
        if probOfAttack != 1:
            num = random()
            if num < probOfAttack:
                return True
        intro_txt = encounterMap['intro_txt']
        fight_txt = encounterMap["fight_txt"]
        after_txt = encounterMap["after_txt"]
        print(f"Encounter with {encounterMap['name']} ")
        print(f"")
        print(f"{ intro_txt }")
        fight = True
        hp = encounterMap["hp"]
        attack = encounterMap["attack"]
        coin = random()
        you_turn = True
        if coin > 0.5:
            you_turn = False
        while fight:
            if you_turn:
                you_turn = False
            else:
                you_turn = True
            msg = random() * 10
            print(f"{fight_txt[int(msg) % len(fight_txt)]}")
            str(input(": ")).upper()
            if you_turn:
                print(f"{self}")
                print("it is your turn what will you do?")
                print(f"ATTACK {encounterMap['name']}")
                print("take HEALTH potion")
                print("take POWER up")
                pturn = True
                while pturn:
                    response = str(input(": ")).upper()
                    if response == "HEALTH":
                        pturn = False
                        # self.use_health_potion()
                        pass
                    elif response == "POWER":
                        pturn = False
                        # self.use_power_up()
                        pass
                    elif response == "ATTACK":
                        pturn = False
                        c = 0
                        acc = 0
                        while c < 3:
                            roll = int(random() * self.attack)
                            acc += roll
                            c += 1
                        print(f"your roll: {acc}")
                        if acc > encounterMap["defence"]:
                            hp -= self.hit_rate
                            print(f"attack a success! {encounterMap['name']} has lost")
                            print(f"{self.hit_rate} health an now has {hp}")
                        else:
                            print("you failed to hit target")
                    else:
                        print("Not a valid response")  
            else:
                print(f"It is {encounterMap['name']}'s turn")
                seed(random())
                c = 0
                acc = 0
                while c < 3:
                    roll = int(random() * attack)
                    acc += roll
                    c += 1
                print(f"enemy roll: {acc}")
                if acc > self.defence:
                    hr = encounterMap["hit_rate"]
                    self.hp -= hr
                    print(f"{encounterMap['name']} has successfully attacked you for {hr}")
                    print(f"your health is now {self.hp}")
                else:
                    print(f"{encounterMap['name']}'s attack missed")
            if self.hp <= 0:
                print('you have died')
                return False
            if hp <= 0:
                print(f"you beat {encounterMap['name']}")
                print(f"{after_txt}")

                return True
  
    def hp_dec(self,amt):
        self.hp += amt

    def change_scene(self, scene):
        self.current_scene = scene


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

#############
# 
#   get_input(current_scene, scene_map, words)
#   - gets respone from player and returns appropriate Scene Enums
#   - if response is INV returns Scenes.INVENTORY and current scene
#   - if response is MENU returns Scenes.MENU and current scene
#   - else 
# 
def get_input(current_scene, scene_map, words):
    p = True
    out = scene_map
    while p:
        response = str(input(": ")).upper()
        response.strip()
        if response in out or response == "INV" or response == "MENU":
            if response == "INV":
                os.system('cls' if os.name == 'nt' else 'clear')
                return Scenes.INVENTORY, current_scene
            elif response == "MENU":
                os.system('cls' if os.name == 'nt' else 'clear')
                return Scenes.MENU, current_scene
            elif response in out:
                print(f"resp {response}") #Print out - delete after completion
                print(f"enum {out[response]}") #Print out - delete after completion
                os.system('cls' if os.name == 'nt' else 'clear')
                return out[response], out[response]
        else:
            print(f'Not a proper response try: {words}')


def Beginning(state):
    print("You awake feeling groggy and sore. Opening your eyes, you look around. You appear to be in a clearing surrounded by tall evergreens. Twenty yards to your right is a small pond, still and surrounded by small ferns. Behind you, and beyond the forest towers a mountain, cold and grey against the bright sky. It cast the forest and the clearing below in shadow.")
    print("What do you want to do?")
    print("Walk towards MOUNTAIN")
    print("Explore FOREST")
    print("Look at POND")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'MOUNTAIN': Scenes.MOUNTAIN_PATH,
            'FOREST': Scenes.ENTER_FOREST,
            'POND': Scenes.POND_APPROACH
        },
        'MOUNTAIN, FOREST, POND'
    )


def Beginning2(state):
    print("You stand in the center of the clearing that you awoke in")
    print("What do you want to do?")
    print("Walk towards MOUNTAIN")
    print("Explore FOREST")
    print("Look at POND")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'MOUNTAIN': Scenes.MOUNTAIN_PATH,
            'FOREST': Scenes.ENTER_FOREST,
            'POND': Scenes.POND_APPROACH
        },
        "MOUNTAIN, FOREST, POND"
    )

def PondApproach(state):
    print("As you approach the pond you see a ripple of movement disturb the smooth surface.")
    print("Once on the bank you see something shimmering at the bottom, nothing now stirrs in the clear water")
    print("You look around you. You see a rock to your left.")
    print("What would yo like to do?")
    print("THROW rock into pond")
    print("JUMP into pond")
    print("RETURN to center of the clearing")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'THROW': Scenes.POND_THROWROCK,
            'JUMP': Scenes.POND_JUMP,
            'RETURN': Scenes.CLEARING
        },
        "THROW, JUMP, RETURN"
    )

def Throwrock(state):
    print("You stoop to pick up the rock and raise it above your head.")
    print("You throw the rock with into the center of the pond with substantial force. It bursts through the water with a loud splunk sound.")
    print("You wait for a moment.")
    print("Nothing happens.")
    print("")
    print("What now?")
    print("JUMP in pool")
    print("RETURN to clearing")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'JUMP': Scenes.POND_JUMP,
            'RETURN': Scenes.CLEARING
        },
        "JUMP, RETURN"
    )

def pondJump(state):
    print("You ready yourself for a moment befor leaping with a heave towards the center of the pond.")
    print("The world crashes around you as you plunge into the water. Once you regain your bearings you look around you.")
    print("Below you see the glint of something shimmering, to your right a bit you see a small opening to a cave.")
    print("What do you want to do?")
    print("Swim DOWN")
    print("Swim towards CAVE")
    print("Get OUT")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'DOWN': Scenes.POND_DOWN,
            'CAVE': Scenes.POND_CAVE_3,
            'OUT': Scenes.POND_OUT
        },
        "DOWN, CAVE, OUT"
    )

def pondOut(state):
    print("You heave yourself out of the pond and stand on the bank dripping with water.")
    print("The pond sits before you once again still.")
    print("What do you want to do?")
    print("JUMP back into the pond")
    print("RETURN to the center of the clearing")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'JUMP': Scenes.POND_JUMP,
            'RETURN': Scenes.CLEARING
        },
        "JUMP, RETURN"
    )

def pondDown(state):
    print("As you swim downards, the glint persists and becomes clearer.")
    print("As you push aside a large pond fern you see a silver pendant lodged in the dirt")
    print("The pendant seems to emit a light blue glow")
    print("Do you grab the pendant or turn back?")
    print("GRAB the pendant")
    print("Turn BACK")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'GRAB': Scenes.GRAB_PENDANT,
            'BACK': Scenes.POND_BACK
        },
        "GREAB, BACK"
    )

def pondBack(state):
    print("You float just below the ponds surface. Below you you see a glint of silver.")
    print("To your right you see a small cave opening")
    print("What do yo want to do?")
    print("Swim DOWN")
    print("Check out CAVE")
    print("Get OUT")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'DOWN': Scenes.POND_DOWN,
            'CAVE': Scenes.POND_CAVE_3,
            'OUT': Scenes.POND_OUT
        },
        "DOWN, CAVE, OUT"
    )
    

def grabPendant(state):
    print("You reach out for the pendant, the pressure in the water around you seems to raise as you do so.")
    print("As your hand closes around the pendant, you hear a harsh squeaky voice behind you")
    print("'Hey you bitch! get the fuck away from my pendant!'")
    print("You look around you, behind you is a small creature with blue and pink scales, large eyes and large teeth")
    print("You try not to exhale in panic, frantically you make you best effort to hold your breath")
    print("'Good job! Most people just drown', said the beast with a smug grin, its voice sounded like a muffled gurgle through the water")
    print("You look around you, you notice suddenly that the ground around you is covered in skeletons and half decomposed bodies")
    print("'I like you, Ill tell you what, Ill give you the pendant if you grab me something. Deep in the forest there is a berry that I am partial to'")
    print("'Id get it myself of course, but I cant leave this pond. Get me five of those berries and Ill give you this pendant'")
    print("You feel your lungs screaming for air, you nod your head vigorously as you rocket towards the surface desperately")
    print("The creature waves at you as you go, 'See you later maybe!'")
    return Scenes.POND_OUT

def pondCave1(state):
    print("pond cave 1")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '2': Scenes.POND_CAVE_2,
        },
        "2"
    )

def pondCave2(state):
    print("pond cave 2")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '1': Scenes.POND_CAVE_1,
            '3': Scenes.POND_CAVE_3,
            '7': Scenes.POND_CAVE_7,

        },
        "1, 3, 7"
    )

def pondCave3(state):
    print("You swim from the main area of the pond into the cave")
    print("As you enter the cave, the water around you becomes colder")
    print("Polyps grow on the walls and seem to reach out towards you.")
    print("The walls move away from you as you enter a larger underwater room, three passages lead out of the room presumaby into other caverns")
    print("You notice an air pocket at the top of the chamber.")
    print("In desparation you swim towards the surface.")
    print("you burst through the surface and smack your head on the low ceiling*")
    print("There is a space of about a foot between the water and the roof of the cave.")
    print("You look up at the rock above you in annoyance, with surprise you notice a circle scratched harshly into it")
    print("The mark looks far from natural, and looks more like a zero sratched in by another being.")
    print("What would you like to do?")
    print("BACK")
    print("2")
    print("4")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.POND_BACK,
            '2': Scenes.POND_CAVE_2,
            '4': Scenes.POND_CAVE_4,
        },
        "BACK, 2, 4"
    )

def pondCave4(state):
    print("pond cave 4")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '3': Scenes.POND_CAVE_3,
            '5': Scenes.POND_CAVE_5,
            '9': Scenes.POND_CAVE_9,
        },
        "3, 5, 9"
    )

def pondCave5(state):
    print("pond cave 5")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '4': Scenes.POND_CAVE_4,

        },
        "4"
    )

def pondCave6(state):
    print("pond cave 6")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '7': Scenes.POND_CAVE_7,
            '11': Scenes.POND_CAVE_11,
        },
        "7, 11"
    )

def pondCave7(state):
    print("pond cave 7")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '2': Scenes.POND_CAVE_2,
            '6': Scenes.POND_CAVE_6,
            '8': Scenes.POND_CAVE_8,
        },
        "2, 6, 8"
    )

def pondCave8(state):
    print("pond cave 8")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '7': Scenes.POND_CAVE_7,
            '13': Scenes.POND_CAVE_13,
        },
        "7, 13"
    )

def pondCave9(state):
    print("pond cave 9")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '4': Scenes.POND_CAVE_4,
            '10': Scenes.POND_CAVE_10,
        },
        "4, 10"
    )

def pondCave10(state):
    print("pond cave 10")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '9': Scenes.POND_CAVE_9,
            '15': Scenes.POND_CAVE_15,
        },
        "9, 15"
    )

def pondCave11(state):
    print("pond cave 11")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '6': Scenes.POND_CAVE_6,
        },
        "6"
    )

def pondCave12(state):
    print("pond cave 12")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '13': Scenes.POND_CAVE_13,
            '17': Scenes.POND_CAVE_17,
        },
        "13, 17"
    )

def pondCave13(state):
    print("pond cave 13")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '8': Scenes.POND_CAVE_8,
            '12': Scenes.POND_CAVE_12,
            '14': Scenes.POND_CAVE_14,
        },
        "8, 12, 14"
    )

def pondCave14(state):
    print("pond cave 14")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '13': Scenes.POND_CAVE_13,
            '15': Scenes.POND_CAVE_15,
            '19': Scenes.POND_CAVE_19,
        },
        "13, 15, 19"
    )

def pondCave15(state):
    print("pond cave 15")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '10': Scenes.POND_CAVE_10,
            '14': Scenes.POND_CAVE_14,
        },
        "10, 14"
    )

def pondCave16(state):
    print("pond cave 16")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'ENTRANCE': Scenes.FOREST_CAVE_ENTRANCE_OUT,
            '17': Scenes.POND_CAVE_17,
        },
        "ENTRANCE, 17"
    )

def pondCave17(state):
    print("pond cave 17")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '12': Scenes.POND_CAVE_12,
            '16': Scenes.POND_CAVE_16,
            '18': Scenes.POND_CAVE_18,
        },
        "12, 16, 18"
    )

def pondCave18(state):
    print("pond cave 18")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '17': Scenes.POND_CAVE_17,

        },
        "17"
    )

def pondCave19(state):
    print("pond cave 19")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '14': Scenes.POND_CAVE_14,
            '20': Scenes.POND_CAVE_20,
        },
        "14, 20"
    )

def pondCave20(state):
    print("pond cave 20")
    print("enter any key to see options")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'ENTRANCE': Scenes.MOUNTAIN_CAVE_ENTRANCE,
            '19': Scenes.POND_CAVE_19,

        },
        "ENTRANCE, 19"
    )

def enterForest(state):
    print("You leave the open clearing and enter the dense forest")
    print("The treetops block out the sun and the air becomes noticably cooler")
    print("You wander a bit, keeping the glow of the clearing within eyesight behind you")
    print("You notice a couple plants that might be edible, but you decide not to risk it")
    print("A ways in fron of you, you notice a path worn lightly into the grass by regular use")
    print("Behind you, the glow of the clearing was diminishing, barely in view")
    print("What would you like to do?")
    print("RETURN to the clearing")
    print("Walk towards the PATH")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'RETURN': Scenes.CLEARING,
            'PATH': Scenes.FOREST_PATH
        },
        "RETURN, PATH"
    )

def forPath(state):
    print("Leaving the clearing behind, you walk towards the path and follow it")
    print("deeper into the forest. The forest grows more and more dense, blocking out the sun.")
    print("As the forest around you becomes darker, you notice a dull glow at the far end of the path.")
    print("The glow slowly becomes brighter as you walk towards it. Continuing down the path, you become increasingly aware of movement in the dark off to either side.")
    print("The hair on your neck stands on end as you realise that you are surrounded by beings in the dark.")
    print("They begin to chatter amonst themselves, first as a murmer barely audible, but growing steadily.")
    hld = str(input(""))
    print("The chatter quiets as you approach the end of the path. The trees on either side end abruptly and you find yourself in another clearing.")
    print("In the center of the clearing is a small village that seems to emenate** a dull diffused glow, as if it was comming from the ground and the very wood of the houses.")
    print("As you stand trepidously/trepidatiously on the edge of the clearing, you notice a figure glide towards you. His head is adorned with branches and from these were hung leaves and berries.")
    print("His arms stretch outward in welcome as he approached you. 'Welcome you our village traveller, may the forests glowing light bless your journeyed soul'")
    print("'Your arrival is most oppourtune, we are celebrating the light cycle this evening. You will be our honoured guest'")
    print("'My name is Gladion. If you wish please follow me and I will see that you are fed and washed, you stink of the world beyond the forest and must be cleansed'")
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.LIGHT_VILLAGE, Scenes.LIGHT_VILLAGE

def lightVillage(state):
    print("Hesitantly you walk into the clearing and follow Gladion towards the center of the village")
    print("Others join you and trail behind, watching you curiously.")
    print("'Go, be cleansed of outside impurities, I will see you when you are ready for tonights festivities.'")
    print("Somewhat statrlinglly, four of the villagers appear by your side.")
    print("They guide you to one of the houses, next to ths house you see a garden with various fruits and vegetables.")
    print("They seem to be organized in a series of concentric rings, rather than that rows to which you are familiar")
    print("Amongst the garden around the middle are a number of shrubs with large red berries.")
    hld = str(input(""))
    print("Inside the hut is a low wide metal basin of warm water and some boxes of nice smelling powders")
    print("Climbing into the basin, you feel the warm water wash away your stress and the grime that had built up on your skin.")
    print("It occurs to you that this is the first time since you awoke in the clearing that you have had a moment of pause.")
    print("Why are you here? How did you get here? In a panic it dawned on you, this might be it. You might be stuck here for good.")
    hld = str(input(""))
    print("As you bask in the water with your eyes closed, you hear some movement behind you. Clumsily in the water, you turn to see whos there.")
    print("One of the villagers is watching you from accross the room, a curious look on their face.")
    print("After a moment of eye contact they smile kindly and speak.")
    print("'Do you not wish to use our cleansing powders?' They gesture to the boxes of powder next to the basin.")
    print("You realize that you hadnt thought of using the powders, or at least had been intimidated in your ingnorance of their purpose.")
    hld = str(input(""))
    print("You give them a sheepish grimmace, attempting to hide your nude body in the shallow basin.")
    print("'I wasnt sure how to use them, or what they were and didnt want to risk it.'")
    print("They smile as they walk to the boxes and pull out a ladle, stooping they scoop some of the powder out of one of the boxes and walk toward you.")
    print("In a wide arc they toss the powder into the basin and it immediately begins to fizz and foam")
    print("'Now rub the foam on your skin, it will wash away your impurities.'")
    print("As you begin to do so, the villager walks to the far side of the room and sits on the floor.")
    hld = str(input(""))
    print("'It really is quite fortuitous that you arrived today of all days.'")
    print("'She the Seer spoke of the arrival of one from beyond. I couldnt dream of doubting her word, but it seemed too wonderous to be true'")
    print("You look at them from over the rim of the basin, 'Who is the seer? She knew I was comming?'")
    print("The villager smiled snarkly, 'Well she didnt know you were comming, but that someone was. Or something at least.'")
    print("'Is she like a psychic os something?' You bask in the warm water, letting yourself get soggy.")
    hld = str(input(""))
    print("'She the Seer is the counterpart to Gladion, as he is to her.' Raising from the floor they grab a folded cloth from a shelf and hand it to you.")
    print("'Together they represent the all, male to female, tangible and formless, here to the beyond and all that is between.'")
    print("The villager's eyes glaze over while saying this, as if reverting to somewhere deep in their conciousness.")
    print("Returning to the present, they look at you and smile. 'You'll meet her later probably, during the ceremony.'")
    hld = str(input(""))
    print("Once you had stepped out of the basin you dryed youself off, the vilager politely turne tsheir back, though for some reason you feel at ease nude in their presence.")
    print("They hand you some clothes and sandles, look you over and smile coyly, 'You really are quite similar to us though you come from so far.'")
    print("You detect a playfulness in their voice as they drift towards the door. 'Tis a shame, maybe in another life perhaps.'")
    print("In the doorway they turn on their heel and face you. 'Ill see you in a bit, come outside when you are done.'")
    print("You call to them as they turn to leave, 'Wait, what's your name?'")
    print("They turn to you and smile, looking you over again, ")
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.CEREMONY_OF_LIGHT, Scenes.CEREMONY_OF_LIGHT



def ceremonyOfLight(state):
    print("You sit on the ground on the center of the village with the others, the excitement in the air sizzles around you.")
    print("At the middle of the village center sits a roaring fire, its warmth bathes the village and keeps the evening chill at bay.")
    print("The villagers chatter to eachother in an unfamiliar language, passing bowls of food and drink to one another and laughing")
    print("You gladly take the food and try it gratefully, it has been a long time since you had eaten last.")
    print("The chatter quiets as Gladion steps gracefully onto the stone platform next to the fire, he is garbed in red and gold.")
    print("The last of the chatter dies as he raises his hands.")
    hld = str(input(""))
    print("'People of the light, we are joined this ceremony of the cycles by a being from beyond our forest.'")
    print("'It is for his benefit that I speak in uncommon tounge', there is chatter of recognition amonst the crowd, many eyes land on you.")
    print("'It is as She the Seer predicted, one from beyond shall join the people of the light for the Celebration of Cycles!!'")
    print("The crowd cheers, and as you look around you notice a tall beautiful woman walk from the back of the crowd towards the front.")
    print("She is wearing robes of white and silver, and walkes with an alien grace.")
    hld = str(input(""))
    print("The crowds cheering grows as the woman reaches the small stage and takes a seat on the intricately carved chair next to Gladion's.")
    print("'Welcome my love, my other half, two as one as whole is one!'")
    print("The crowd chantes after Gladion, 'Two as one whole as one!'")
    print("The woman raises her hand and waves at the crowd calmly, a serene smile on her face.")
    print("Gladion chuckles lightly and waves at the small village to quiet.")
    hld = str(input(""))
    print("'Here again after another seasonal cycle. It is so good to see you all again.' He stands with his hands held held wide above his head.")
    print("'Time has passed us by as it does, and there have been times both bad and good.'")
    print("'The rise and fall of tensions within and without has affected us all and left us more.'")
    print("'We grow as we watch ourselves struggle through life, learning as we do.'")
    print("But the struggle leaves scars and sores that sit deep down and ache and fester.")
    hld = str(input(""))
    print("The crowd around you has become deathly quiet, their excitement has gone from bubbling chatter to brittle tension.")
    print("'These wounds are too much to bear, and blind us from truth. Blind us from the light!'. Gladion scans the crowd, shifting from eye to eye.")
    print("'And so the Celebration of the Cycles cleanses us.' He raises his face to the sky and stares at the sun, eyes wide.")
    print("'Through it we are cleaned of the sores we have gained, through ones suffering we become pure!'")
    print("You look around nervously, the crowd has regained their vigor. They begin to fidget and chatter with fervor.")
    hld = str(input(""))
    print("'And this Cycle of Cycles which has been particularly hard on us, the light has brought us a special gift as offering.'")
    print("The hair on your neck sparks and raises sharply. You look around you, the village is looking at you hungrily.")
    print("You look up to Gladion and lock eyes with him. He holds your gaze intensely, his peaceful smile curling at the corners.")
    print("'Thank you for embodying our passage to purity and acting as a vessel of the light. I hope you suffer beautifully.'")
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.COL_ENCOUNTER, Scenes.COL_ENCOUNTER

def COLEncounter(state):
    print("")
    print("-")
    print("-")
    print("BACKWOODS to go to backwoods area")
    print("go to backwoods?")
    print("BACKWOODS to go to backwoods area")
    print("BACKWOODS to go to backwoods area")
    return get_input(
        state.current_scene,
        {
            'BACKWOODS': Scenes.BACKWOODS,
        },
        "BACKWOODS"
    )
    
def backwoods(state):
    print("Backwoods area")
    print("goes to puzzle area, clearing with cave entrance, forest entrance")
    print("-")
    print("-")
    print("Where to go?")
    print("to PUZZLE")
    print("to CAVE entrance")
    print("to forest ENTRANCE")
    return get_input(
        state.current_scene,
        {
            'PUZZLE': Scenes.FOREST_PUZZLE,
            'CAVE': Scenes.FOREST_CAVE_CLEARING_IN,
            'ENTRANCE': Scenes.ENTER_FOREST
        },
        "PUZZLE, CAVE, ENTRANCE"
    )

def forestCaveClearingIn(state):
    print("You enter a small clearing with a gnalred tree against a large rock")
    print("As you approach the tree you see a gap between the roots and the rock,")
    print("it seems to extend under the rock and from a certatin angle it almost")
    print("looks like the opening widenes further down.")
    print("Do you want to go down?")
    print("go down into the HOLE")
    print("Go BACK the way you came")
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.BACKWOODS,
            'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
        },
        "BACK, HOLE"
    )

def forestCaveClearingOut(state):
    print("You crawl out of the tight hole, using roots to pull yourself up")
    print("You are in a clearing")
    print("-")
    print("-")
    print("where to go?")
    print("go into forest FOREST")
    print("Go back into HOLE")
    return get_input(
        state.current_scene,
        {
            'FOREST': Scenes.BACKWOODS,
            'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
        },
        "FOREST, HOLE"
    )


def forestCaveEntranceIn(state):
    print("Going feet first you lower yourself into the opening.") 
    print("Using the roots of the tree you lower yourself")
    print("into an underground chamber. Light peeks in from cracks in the rock and the")
    print("hole you just climbed through. The light reflects off of crystals on the")
    print("floor and walls, shimmering slits cut accross one another and provide a dim glow.")
    print("The sharp refractions of the crystals are sofened by a dim swirling wash.")
    print("You notice a wetness to the echo of the chamber and move deeper in.")
    print("In the center is a round pool that seems to continue down forever.")
    print("On closer inspection you find that the walls of the pool end afer about 10 feet")
    print("and give way to open water. In the dim light of the cave you cant see much.")
    print("What would you like to do?")
    print("JUMP in the pool")
    print("go BACK out to the clearing")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'JUMP': Scenes.POND_CAVE_20,
            'BACK': Scenes.FOREST_CAVE_CLEARING_OUT
        },
        "JUMP, BACK"
    )

def forestCaveEntranceOut(state):
    print("Pull yourself out of pool.") 
    print("crystal cavern")
    print("Pool behind you, hole that lights coming in through")
    print("-")
    print("-")
    print("-")
    print("What would you like to do?")
    print("JUMP in the pool")
    print("climb out of the HOLE")
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            'JUMP': Scenes.POND_CAVE_20,
            'HOLE': Scenes.FOREST_CAVE_CLEARING_OUT
        },
        "JUMP, HOLE"
    )


def forestPuzzle(state):
    print("Theres gonna be a puzzle here of some sort")
    print("for now connects straight to forest mountain path")
    print("Can also go to ")
    print("-")
    print("where to go?")
    print("go back to BACKWOODS")
    print("go to forest mountain PATH")
    return get_input(
        state.current_scene,
        {
            'BACKWOODS': Scenes.BACKWOODS,
            'PATH': Scenes.FOREST_MOUTAIN_PATH
        },
        "BACKWOODS, PATH"
    )

def forestMountainPath(state):
    print("Forest mountain path")
    print("connects forest puzzle to the mountain base")
    print("-")
    print("-")
    print("where to go?")
    print("forest PUZZLE")
    print("mountain BASE")
    return get_input(
        state.current_scene,
        {
            'PUZZLE': Scenes.FOREST_PUZZLE,
            'BASE': Scenes.MOUNTAIN_BASE
        },
        "PUZZLE, BASE"
    )

def mountainPath1(state):
    print("Mountain path 1 ")
    print("connects CLEARING to mountain path 2")
    print("-")
    print("-")
    print("where to go?")
    print("back to CLEARING")
    print("to mountian PATH")
    return get_input(
        state.current_scene,
        {
            'CLEARING': Scenes.CLEARING,
            'PATH': Scenes.MOUNTAIN_PATH_2,
        },
        "CLEARING, PATH"
    )

def mountainPath2(state):
    win = state.encounter(
        probOfAttack = 0.6,
        encounterMap = {
            'name': 'racoon man',
            'hp': 20,
            'defence': 10,
            'hit_rate': 2,
            'attack': 10,
            'prize': InvItem.HEALTH_POTION,
            'intro_txt': 'there is a guy in the road that blocks your way. he has racoons on him. he says:  hey i dont like you so im gonna stab ya.',
            'fight_txt': [
                'you fuck off',
                'gonna fight ya',
                'knife fight',
            ],
            'after_txt': 'ok you win ouch. have a health potion',
        },
    )
    print("mountain path 2")
    print("connects mountain path 1 to mountain base")
    print("should have encounter here")
    print("-")
    print("where to go?")
    print("go to mountain PATH")
    print("mountain ENTRANCE")
    return get_input(
        state.current_scene,
        {
            'PATH': Scenes.MOUNTAIN_PATH,
            'ENTRANCE': Scenes.MOUNTAIN_BASE,
        },
        "ENTRANCE, PATH"
    )

def mountainBase(state):
    print("Base of the mountain")
    print("Some people here to talk to")
    print("maybe sell some stuff")
    print("also connects to forest mountain path")
    print("where to go?")
    print("BACK to mountain path")
    print("mountain ENTRANCE")
    print("forest mountain PATH")
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.MOUNTAIN_PATH_2,
            'ENTRANCE': Scenes.MOUNTAIN_ENTRANCE,
            'PATH': Scenes.FOREST_MOUTAIN_PATH
        },
        "BACK, ENTRANCE, PATH"
    )

def mountainEntrance(state):
    win = state.encounter(
        0.6,
        encounterMap = {
            'name': 'racoon man',
            'hp': 20,
            'defence': 6,
            'hit_rate': 2,
            'attack': 6,
            'prize': "health",
            'intro_txt': 'hey i dont like you so im gonna stab ya.',
            'fight_txt': [
                'you fuck off',
                'gonna fight ya',
                'knife fight',
            ],
            'after_txt': 'ok you win ouch. have a health potion',
        },
    )
    print("Mountain entrance")
    print("connects mountain base to m_LVL1_R1")
    print("encounter here")
    print("-")
    print("where go?")
    print("mountain BASE")
    print("to LVL1")
    return get_input(
        state.current_scene,
        {
            'BASE': Scenes.MOUNTAIN_BASE,
            'LVL1': Scenes.M_LVL1_R1
        },
        "BASE, LVL1"
    )

def mLvl1R1(state):
    win = state.encounter(
        0.4,
        encounterMap = {
            'name': 'racoon man',
            'hp': 20,
            'defence': 6,
            'hit_rate': 2,
            'attack': 6,
            'prize': "health",
            'intro_txt': 'hey i dont like you so im gonna stab ya.',
            'fight_txt': [
                'you fuck off',
                'gonna fight ya',
                'knife fight',
            ],
            'after_txt': 'ok you win ouch. have a health potion',
        },
    )
    print("first room on the first floor")
    print("currently connects to LVL1Stairs through mountain cave entrance")
    print("also connects to mountain entrance")
    print("-")
    print("where?")
    print("mountain ENTRANCE")
    print("to MCAVE")
    return get_input(
        state.current_scene,
        {
            'ENTRANCE': Scenes.MOUNTAIN_ENTRANCE,
            'MCAVE': Scenes.MOUNTAIN_CAVE_ENTRANCE
        },
        "ENTRANCE, MCAVE"
    )

def mountainCaveEntrance(state):
    win = state.encounter(
        0.4,
        encounterMap = {
            'name': 'racoon man',
            'hp': 20,
            'defence': 6,
            'hit_rate': 2,
            'attack': 6,
            'prize': "health",
            'intro_txt': 'hey i dont like you so im gonna stab ya.',
            'fight_txt': [
                'you fuck off',
                'gonna fight ya',
                'knife fight',
            ],
            'after_txt': 'ok you win ouch. have a health potion',
        },
    )
    print("Mountain cave entrance")
    print("maountain entrance to underwater cave")
    print("also connects LVL1 R1 and LVL1 Stairs")
    print("-")
    print("where?")
    print("to LVL1")
    print("to CAVE")
    print("to USTAIRS lvl1 stairs")
    return get_input(
        state.current_scene,
        {
            'LVL1': Scenes.M_LVL1_R1,
            'CAVE': Scenes.POND_CAVE_16,
            'USTAIRS': Scenes.M_LVL1_STAIRS
        },
        "LVL1, CAVE, USTAIRS"
    )

def mLvl1Stairs(state):
    win = state.encounter(
        0.4,
        {
            'name': 'racoon man',
            'hp': 20,
            'defence': 6,
            'hit_rate': 2,
            'attack': 6,
            'prize': "health",
            'intro_txt': 'hey i dont like you so im gonna stab ya.',
            'fight_txt': [
                'you fuck off',
                'gonna fight ya',
                'knife fight',
            ],
            'after_txt': 'ok you win ouch. have a health potion',
        },
    )
    print("lvl1 stairs")
    print("connects lvl1 and lvl2")
    print("currently goes from mountain cave entrance to LVL2 R1")
    print("-")
    print("where?")
    print("to MCAVE")
    print("to LVL2")
    return get_input(
        state.current_scene,
        {
            'MCAVE': Scenes.MOUNTAIN_CAVE_ENTRANCE,
            'LVL2': Scenes.M_LVL2_R1
        },
        "MCAVE, LVL2"
    )

def mLvl2R1(state):
    print("mountain LVL 2")
    print("connects to LVL1STAIRS and LVL2Stairs")
    print("-")
    print("-")
    print("where?")
    print("go USTAIRS staircase to lvl3")
    print("go DSTAIRS staircase to lvl1")
    return get_input(
        state.current_scene,
        {
            'DSTAIRS': Scenes.M_LVL1_STAIRS,
            'USTAIRS': Scenes.M_LVL2_STAIRS
        },
        "DSTAIRS, USTAIRS"
    )

def mLvl2Stairs(state):
    print("mountain lvl2 stairs to lvl 3")
    print("connects lvl2 to lvl3")
    print("-")
    print("-")
    print("where?")
    print("to LVL2")
    print("to LVL3")
    return get_input(
        state.current_scene,
        {
            'LVL2': Scenes.M_LVL2_R1,
            'LVL3': Scenes.M_LVL3_R1
        },
        "LVL2, LVL3"
    )

def mLv32R1(state):
    print("mountain lvl 3")
    print("connects to lvl2 stairs and lvl3stairs to boss")
    print("-")
    print("-")
    print("Where?")
    print("to DSTAIRS staircase to lvl2")
    print("to USTAIRS staircase to lvl3")
    return get_input(
        state.current_scene,
        {
            'DSTAIRS': Scenes.M_LVL2_STAIRS,
            'USTAIRS': Scenes.M_LVL3_STAIRS
        },
        "DSTAIRS, USTAIRS"
    )

def mLvl3Stairs(state):
    print("mountain lvl 3 stairs")
    print("connect lvl3 with boss area")
    print("-")
    print("-")
    print("where?")
    print("to LVL3")
    print("UP to boss area")
    return get_input(
        state.current_scene,
        {
            'LVL3': Scenes.M_LVL3_R1,
            'UP': Scenes.BOSS_AREA
        },
        "LVL3, UP"
    )

def bossArea(state):
    print("Boss area")
    print("where final encounter will take place")
    print("goes only back to LVL3 stairs")
    print("-")
    print("where?")
    print("BACK down stairs")
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.M_LVL3_STAIRS
        },
        "BACK"
    )


def main():
    # p = Player()
    print("Welcome to VALLEY QUEST!!!")
    print("KEYWORDS displayed in CAPS are used to make decisions,")
    print("The decisions made availiable to you will be determined by your previous actions")
    play = str(input(""))
    print("would you like to play? Y/N")
    play = str(input(": ")).upper()
    if play == "Y":
        state = State()
        state.play()
    else:
        print("Ok bye")




main()
