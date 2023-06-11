# import os
import json
from os import name
import os
from random import random
from random import seed
import math
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

    FOREST_PUZZLE_CENTER = 'puzzleCenter'

    FOREST_PUZZLE_ONE = 'forestPuzzleOne'
    FOREST_PUZZLE_TWO = 'forestPuzzleTwo'
    FOREST_PUZZLE_THREE = 'forestPuzzleThree'
    FOREST_PUZZLE_FOUR = 'forestPuzzleFour'
    FOREST_PUZZLE_FIVE = 'forestPuzzleFifth'
    FOREST_PUZZLE_SIX = 'forestPuzzleSixth'
    FOREST_PUZZLE_SEVEN = 'forestPuzzleSeventh'
    FOREST_PUZZLE_EIGHT = 'forestPuzzleEighth'

    PUZZLE_ONE_TRIGGER = 'puzzleTriggerOne'
    PUZZLE_TWO_TRIGGER = 'puzzleTriggerTwo'
    PUZZLE_THREE_TRIGGER = 'puzzleTriggerThree'
    PUZZLE_FOUR_TRIGGER = 'puzzleTriggerFour'
    PUZZLE_FIVE_TRIGGER = 'puzzleTriggerFive'
    PUZZLE_SIX_TRIGGER = 'puzzleTriggerSix'
    PUZZLE_SEVEN_TRIGGER = 'puzzleTriggerSeven'
    PUZZLE_EIGHT_TRIGGER = 'puzzleTriggerEight'



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
        self.init_puzzle = True
        self.reset_puzzle = True
        self.puzzle_string = ""
        self.puzzle_triggered = [False, False, False, False, False, False, False, False] 
        self.puzzle_sections = ["1", "2", "3", "4", "5", "6", "7", "8"]
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
            Scenes.FOREST_PUZZLE_CENTER: forestPuzzleCenter,
            Scenes.FOREST_PUZZLE_ONE: forestPuzzleOne,
            Scenes.FOREST_PUZZLE_TWO: forestPuzzleTwo,
            Scenes.FOREST_PUZZLE_THREE: forestPuzzleThree,
            Scenes.FOREST_PUZZLE_FOUR: forestPuzzleFour,
            Scenes.FOREST_PUZZLE_FIVE: forestPuzzleFive,
            Scenes.FOREST_PUZZLE_SIX: forestPuzzleSix,
            Scenes.FOREST_PUZZLE_SEVEN: forestPuzzleSeven,
            Scenes.FOREST_PUZZLE_EIGHT: forestPuzzleEight,
            Scenes.PUZZLE_ONE_TRIGGER: puzzleTriggerOne,
            Scenes.PUZZLE_TWO_TRIGGER: puzzleTriggerTwo,
            Scenes.PUZZLE_THREE_TRIGGER: puzzleTriggerThree,
            Scenes.PUZZLE_FOUR_TRIGGER: puzzleTriggerFour,
            Scenes.PUZZLE_FIVE_TRIGGER: puzzleTriggerFive,
            Scenes.PUZZLE_SIX_TRIGGER: puzzleTriggerSix,
            Scenes.PUZZLE_SEVEN_TRIGGER: puzzleTriggerSeven,
            Scenes.PUZZLE_EIGHT_TRIGGER: puzzleTriggerEight,
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

    def reset_board(self):
        for i in range(0,1):    
            temp_sections = self.puzzle_sections
            for i in range(len(temp_sections)):
                temp_rand = math.floor((random() * len(temp_sections) - 1))
                self.puzzle_string = f'{self.puzzle_string}{temp_sections[temp_rand]}'
                del temp_sections[temp_rand]
            if i == 0:
                self.puzzle_string = f'{self.puzzle_string}|'

    def puzzle_is_valid(self):
        triggered = self.puzzle_triggered.count(True)
        for i in range(0, triggered):
            if not self.puzzle_triggered[self.puzzle_string[self.puzzle_string[i] + 9]]:
                return False
        return True
    
    def puzzle_complete(self):
        return self.puzzle_triggered.count(True) == 8
        
    def section_number(self, section):
        parts = self.puzzle_string.split("|")
        return parts[1][int(parts[0][section])]

    def get_new_puzzle(self):
        return self.reset_puzzle

    def init_puzzle_true(self):
        self.init_puzzle = True

    def init_puzzle_false(self):
        self.init_puzzle = False

    def is_init_puzzle(self):
        return self.init_puzzle 

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
    print_msg = """You awake feeling groggy and sore. Opening your eyes,
you look around. You appear to be in a clearing surrounded by tall
evergreens. Twenty yards to your right is a small pond, still and
surrounded by small ferns. Behind you, and beyond the forest towers a
mountain, cold and grey against the bright sky. It cast the forest and the
clearing below in shadow."""
    choice_msg = """What do you want to do?\nWalk towards MOUNTAIN\nExplore FOREST\nLook at POND"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You stand in the center of the clearing that you awoke in"""
    choice_msg = """What do you want to do?\nWalk towards MOUNTAIN\nExplore FOREST\nLook at POND"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """As you approach the pond you see a ripple of movement disturb
the smooth surface. Once on the bank you see something shimmering at the
bottom, nothing now stirrs in the clear water. You look around you. You see
a rock to your left."""
    choice_msg = """What would yo like to do?\nTHROW rock into pond\nJUMP into pond\nRETURN to center of the clearing"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You stoop to pick up the rock and raise it above your head. You
throw the rock with into the center of the pond with substantial force. It
bursts through the water with a loud splunk sound.\nYou wait for a moment.
Nothing happens."""
    choice_msg = """What now?\nJUMP in pool\nRETURN to clearing"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You ready yourself for a moment befor leaping with a
heave towards the center of the pond. The world crashes around you as you
plunge into the water. Once you regain your bearings you look around you.
Below you see the glint of something shimmering, to your right a bit you
see a small opening to a cave. """
    choice_msg = """What do you want to do?\nSwim DOWN\nSwim towards CAVE\nGet OUT"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You heave yourself out of the pond and stand on the bank dripping
with water.\nThe pond sits before you once again still."""
    choice_msg = """What do you want to do?\nJUMP back into the pond\nRETURN to the center of the clearing"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """As you swim downards, the glint persists and becomes clearer. As you
push aside a large pond fern you see a silver pendant lodged in the dirt.\nThe pendant seems to emit a light blue glow."""
    choice_msg = """Do you grab the pendant or turn back?\nGRAB the pendant\nTurn BACK"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You float just below the ponds surface. Below you you see
a glint of silver. To your right you see a small cave opening."""
    choice_msg = """What do yo want to do?\nSwim DOWN\nCheck out CAVE\nGet OUT"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You reach out for the pendant, the pressure in the water around
you seems to raise as you do so. As your hand closes around the pendant,
you hear a harsh squeaky voice behind you. 'Hey you bitch! get the fuck
away from my pendant!'. You look around you, behind you is a small creature
with blue and pink scales, large eyes and large teeth. You try not to
exhale in panic, frantically you make you best effort to hold your breath.
'Good job! Most people just drown', said the beast with a smug grin, its
voice sounded like a muffled gurgle through the water. You look around
you, you notice suddenly that the ground around you is covered in skeletons
and half decomposed bodies. 'I like you, Ill tell you what, Ill give you
the pendant if you grab me something. Deep in the forest there is a berry
that I am partial to'. 'Id get it myself of course, but I cant leave this
pond. Get me five of those berries and Ill give you this pendant'. You feel
your lungs screaming for air, you nod your head vigorously as you rocket
towards the surface desperately. The creature waves at you as you go, 'See
you later maybe!'."""
    print(print_msg)
    return Scenes.POND_OUT

def pondCave1(state):
    print_msg = """pond cave 1"""
    choice_msg = """2"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 2"""
    choice_msg = """1\n3\n7"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You swim from the main area of the pond into the cave.
As you enter the cave, the water around you becomes colder. Polyps grow on
the walls and seem to reach out towards you. The walls move away from you
as you enter a larger underwater room, three passages lead out of the room
presumaby into other caverns. You notice an air pocket at the top of the
chamber. In desparation you swim towards the surface. You burst through the
surface and smack your head on the low ceiling. There is a space of about a
foot between the water and the roof of the cave. You look up at the rock
above you in annoyance, with surprise you notice a circle scratched harshly
into it. The mark looks far from natural, and looks more like a zero
sratched in by another being."""
    choice_msg = """What would you like to do?\nBACK\n2\n4"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 4"""
    choice_msg = """3\n5\n9"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 5"""
    choice_msg = """4"""
    print(print_msg)
    print(choice_msg)
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '4': Scenes.POND_CAVE_4,

        },
        "4"
    )

def pondCave6(state):
    print_msg = """pond cave 6"""
    choice_msg = """7\n11"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 7"""
    choice_msg = """2\n6\n8"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 8"""
    choice_msg = """7\n13"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 9"""
    choice_msg = """4\n10"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 10"""
    choice_msg = """9\n15"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 11"""
    choice_msg = """6"""
    print(print_msg)
    print(choice_msg)
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '6': Scenes.POND_CAVE_6,
        },
        "6"
    )

def pondCave12(state):
    print_msg = """pond cave 12"""
    choice_msg = """13\n17"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 13"""
    choice_msg = """8\n12\n14"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 14"""
    choice_msg = """enter any key to see options"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 15"""
    choice_msg = """10\n14"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 16"""
    choice_msg = """ENTERANCE\n17"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 17"""
    choice_msg = """12\n16\n18"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 18"""
    choice_msg = """17"""
    print(print_msg)
    print(choice_msg)
    print(f"| {state} |")
    return get_input(
        state.current_scene,
        {
            '17': Scenes.POND_CAVE_17,

        },
        "17"
    )

def pondCave19(state):
    print_msg = """pond cave 19"""
    choice_msg = """14\n20"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """pond cave 20"""
    choice_msg = """ENTERANCE\n19"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You leave the open clearing and enter the dense forest.
The treetops block out the sun and the air becomes noticably cooler. You
wander a bit, keeping the glow of the clearing within eyesight behind you.
You notice a couple plants that might be edible, but you decide not to
risk it. A ways in fron of you, you notice a path worn lightly into the
grass by regular use. Behind you, the glow of the clearing was diminishing,
barely in view. """
    choice_msg = """What would you like to do?\nRETURN to the clearing.\nWalk towards the PATH."""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """Leaving the clearing behind, you walk towards the path
and follow it deeper into the forest. The forest grows more and more dense,
blocking out the sun. As the forest around you becomes darker, you notice a
dull glow at the far end of the path. The glow slowly becomes brighter as
you walk towards it. Continuing down the path, you become increasingly
aware of movement in the dark off to either side. The hair on your neck
stands on end as you realise that you are surrounded by beings in the dark.
They begin to chatter amonst themselves, first as a murmer barely audible,
but growing steadily."""
    print(print_msg)
    hld = str(input(""))
    print_msg1 = """The chatter quiets as you approach the end of the path.
The trees on either side end abruptly and you find yourself in another
clearing. In the center of the clearing is a small village that seems to
emenate** a dull diffused glow, as if it was comming from the ground and
the very wood of the houses. As you stand trepidously/trepidatiously on the
edge of the clearing, you notice a figure glide towards you. His head is
adorned with branches and from these were hung leaves and berries. His arms
stretch outward in welcome as he approached you. 'Welcome you our village
traveller, may the forests glowing light bless your journeyed soul'. 'Your
arrival is most oppourtune, we are celebrating the light cycle this
evening. You will be our honoured guest'. 'My name is Gladion. If you wish
please follow me and I will see that you are fed and washed, you stink of
the world beyond the forest and must be cleansed'."""
    print(print_msg1)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.LIGHT_VILLAGE, Scenes.LIGHT_VILLAGE

def lightVillage(state):
    print_msg = """Hesitantly you walk into the clearing and follow Gladion
towards the center of the village. Others join you and trail behind, 
watching you curiously. 'Go, be cleansed of outside impurities, I will see
you when you are ready for tonights festivities'. Somewhat statrlinglly,
four of the villagers appear by your side. They guide you to one of the
houses, next to ths house you see a garden with various fruits and
vegetables. They seem to be organized in a series of concentric rings,
rather than that rows to which you are familiar. Amongst the garden around
the middle are a number of shrubs with large red berries."""
    print(print_msg)
    hld = str(input(""))
    print_msg1 = """Inside the hut is a low wide metal basin of warm water
and some boxes of nice smelling powders. Climbing into the basin, you feel
the warm water wash away your stress and the grime that had built up on
your skin. It occurs to you that this is the first time since you awoke in
the clearing that you have had a moment of pause. Why are you here? How did
you get here? In a panic it dawned on you, this might be it. You might be
stuck here for good."""
    print(print_msg1)
    hld = str(input(""))
    print_msg2 = """As you bask in the water with your eyes closed, you hear
some movement behind you. Clumsily in the water, you turn to see whos
there. One of the villagers is watching you from accross the room, a
curious look on their face. After a moment of eye contact they smile kindly
and speak. 'Do you not wish to use our cleansing powders?' They gesture to
the boxes of powder next to the basin. You realize that you hadnt thought
of using the powders, or at least had been intimidated in your ingnorance 
of their purpose."""
    print(print_msg2)
    hld = str(input(""))
    print_msg3 = """You give them a sheepish grimmace, attempting to hide your
nude body in the shallow basin. 'I wasnt sure how to use them, or what they
were and didnt want to risk it.' They smile as they walk to the boxes and
pull out a ladle, stooping they scoop some of the powder out of one of the
boxes and walk toward you. In a wide arc they toss the powder into the
basin and it immediately begins to fizz and foam. 'Now rub the foam on your
skin, it will wash away your impurities.' As you begin to do so, the
villager walks to the far side of the room and sits on the floor."""
    print(print_msg3)
    hld = str(input(""))
    print_msg4 = """'It really is quite fortuitous that you arrived today of
all days'. 'She the Seer spoke of the arrival of one from beyond. I couldnt
dream of doubting her word, but it seemed too wonderous to be true'. You
look at them from over the rim of the basin, 'Who is the seer? She knew I
was coming?' The villager smiled snarkly, 'Well she didnt know you were
comming, but that someone was. Or something at least.' 'Is she like a
psychic or something?' You bask in the warm water, letting yourself get
soggy."""
    print(print_msg4)
    hld = str(input(""))
    print_msg5 = """'She the Seer is the counterpart to Gladion, as he is to her.'
Raising from the floor they grab a folded cloth from a shelf and hand it to
you. 'Together they represent the all, male to female, tangible and
formless, here to the beyond and all that is between.' The villager's eyes
glaze over while saying this, as if reverting to somewhere deep in their
conciousness. Returning to the present, they look at you and smile. 'You'll
meet her later probably, during the ceremony.'"""
    print(print_msg5)
    hld = str(input(""))
    print_msg6 = """Once you had stepped out of the basin you dryed youself off,
the villager politely turns their back, though for some reason you feel at
ease nude in their presence. They hand you some clothes and sandles, look
you over and smile coyly, 'You really are quite similar to us though you
come from so far.' You detect a playfulness in their voice as they drift
towards the door. 'Tis a shame, maybe in another life perhaps.' In the
doorway they turn on their heel and face you. 'Ill see you in a bit, come
outside when you are done.' You call to them as they turn to leave, 'Wait,
what's your name?' They turn to you and smile, looking you over again."""
    print(print_msg6)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.CEREMONY_OF_LIGHT, Scenes.CEREMONY_OF_LIGHT



def ceremonyOfLight(state):
    print_msg = """You sit on the ground on the center of the village with
the others, the excitement in the air sizzles around you. At the middle of
the village center sits a roaring fire, its warmth bathes the village and
keeps the evening chill at bay. The villagers chatter to eachother in an
unfamiliar language, passing bowls of food and drink to one another and
laughing. You gladly take the food and try it gratefully, it has been a
long time since you had eaten last. The chatter quiets as Gladion steps
gracefully onto the stone platform next to the fire, he is garbed in red
and gold. The last of the chatter dies as he raises his hands."""
    print(print_msg)
    hld = str(input(""))
    print_msg1 = """'People of the light, we are joined this ceremony of the cycles
by a being from beyond our forest.' 'It is for his benefit that I speak in
uncommon tounge', there is chatter of recognition amonst the crowd, many
eyes land on you. 'It is as She the Seer predicted, one from beyond shall
join the people of the light for the Celebration of Cycles!!' The crowd
cheers, and as you look around you notice a tall beautiful woman walk from
the back of the crowd towards the front. She is wearing robes of white and
silver, and walkes with an alien grace."""
    print(print_msg1)
    hld = str(input(""))
    print_msg2 = """The crowds cheering grows as the woman reaches the small stage
and takes a seat on the intricately carved chair next to Gladion's.
'Welcome my love, my other half, two as one as whole is one!' The crowd
chantes after Gladion, 'Two as one whole as one!' The woman raises her hand
and waves at the crowd calmly, a serene smile on her face. Gladion chuckles
lightly and waves at the small village to quiet."""
    print(print_msg2)
    hld = str(input(""))
    print_msg3 = """'Here again after another seasonal cycle. It is so good to see
you all again.' He stands with his hands held held wide above his head.
'Time has passed us by as it does, and there have been times both bad and
good'. 'The rise and fall of tensions within and without has affected us
all and left us more.' 'We grow as we watch ourselves struggle through
life, learning as we do.' But the struggle leaves scars and sores that sit
deep down and ache and fester."""
    print(print_msg3)
    hld = str(input(""))
    print_msg4 = """The crowd around you has become deathly quiet, their
excitement has gone from bubbling chatter to brittle tension. 'These wounds
are too much to bear, and blind us from truth. Blind us from the light!'.
Gladion scans the crowd, shifting from eye to eye. 'And so the Celebration
of the Cycles cleanses us.' He raises his face to the sky and stares at the
sun, eyes wide. 'Through it we are cleaned of the sores we have gained,
through ones suffering we become pure!' You look around nervously, the
crowd has regained their vigor. They begin to fidget and chatter with
fervor."""
    print(print_msg4)
    hld = str(input(""))
    print_msg5 = """'And this Cycle of Cycles which has been particularly hard on us,
the light has brought us a special gift as offering.' The hair on your neck
sparks and raises sharply. You look around you, the village is looking at
you hungrily. You look up to Gladion and lock eyes with him. He holds your
gaze intensely, his peaceful smile curling at the corners. 'Thank you for
embodying our passage to purity and acting as a vessel of the light. I hope
you suffer beautifully.'"""
    print(print_msg5)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.COL_ENCOUNTER, Scenes.COL_ENCOUNTER

def COLEncounter(state):
    print_msg = """You are being surrounded by the members of the village. They close
in upon you with hungry eyes. As they close in you notice a break in the
crowd to your left. You duck and run through, pushing their hands aside.
You are now on the outskirts of the crowd, your only options for escape are
to right or to the left. """
    choice_msg = """Which would you like to do?\nLEFT run to the left\nRIGHT run to the right\nBACKWOODS for now"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACKWOODS': Scenes.BACKWOODS,
        },
        "BACKWOODS"
    )
    
def backwoods(state):
    print_msg = """Backwoods area\ngoes to puzzle area, clearing with cave entrance,
forest entrance."""
    choice_msg = """Where to go?\nto PUZZLE\nto CAVE entrance\nto forest ENTRANCE"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You enter a small clearing with a gnalred tree against a large
rock. As you approach the tree you see a gap between the roots and the
rock, it seems to extend under the rock and from a certatin angle it almost
looks like the opening widenes further down."""
    choice_msg = """Do you want to go down?\ngo down into the HOLE\nGo BACK the way you came"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.BACKWOODS,
            'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
        },
        "BACK, HOLE"
    )

def forestCaveClearingOut(state):
    print_msg = """You crawl out of the tight hole, using roots to pull yourself up. You are in a clearing. """
    choice_msg = """Where to go?\nGo into forest FOREST\nGo back into HOLE"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'FOREST': Scenes.BACKWOODS,
            'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
        },
        "FOREST, HOLE"
    )


def forestCaveEntranceIn(state):
    print_msg = """Going feet first you lower yourself into the opening.
Using the roots of the tree you lower yourself into an underground chamber.
Light peeks in from cracks in the rock and the hole you just climbed
through. The light reflects off of crystals on the floor and walls,
shimmering slits cut accross one another and provide a dim glow. The sharp
refractions of the crystals are sofened by a dim swirling wash. You notice
a wetness to the echo of the chamber and move deeper in. In the center is a
round pool that seems to continue down forever. On closer inspection you
find that the walls of the pool end afer about 10 feet and give way to open
water. In the dim light of the cave you cant see much."""
    choice_msg = """What would you like to do?\nJUMP in the pool\ngo BACK out to the clearing""" 
    print(print_msg) 
    print(choice_msg)
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
    print_msg = """Pull yourself out of pool.\ncrystal cavern\nPool behind you, hole 
that lights coming in through"""
    choice_msg = """What would you like to do?\nJUMP in the pool\nclimb out of the HOLE"""
    print(print_msg) 
    print(choice_msg)
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
    print_msg = """As you travel through the dark woods you notice the sun beginning
to break through the trees. Looking ahead you notice the path starting
slope upwards. As you follow it upwards you find yourself on the middle of
a bridge. Around you is what looks like a square arrangement of ruins. The
bridge ahead continues downward again until it levels with the ground."""
    choice_msg = """Where to go?\ngo back to BACKWOODS\ncontinue to PUZZLE"""
    print(print_msg)
    print(choice_msg)

    return get_input(
        state.current_scene,
        {
            'BACKWOODS': Scenes.BACKWOODS,
            'PUZZLE': Scenes.FOREST_PUZZLE_CENTER
        },
        "BACKWOODS, PUZZLE"
    )

def forestPuzzleCenter(state):
    if not state.puzzle_is_valid():
        state.reset_board()
    if state.get_new_puzzle():
        state.reset_board()
    if state.puzzle_complete():
        print_msg = """As you return to the center puzzle section you notice a change
to the region. The lanterns are all lit and there is now a hole in the ground
in the middle of the square of stones. You cautiously move forward into the 
hole"""
        print(print_msg)
        hld = str(input(""))
        os.system('cls' if os.name == 'nt' else 'clear')
        return state.current_scene, Scenes.FOREST_MOUTAIN_PATH
    if state.is_init_puzzle():
        state.init_puzzle_false()
        print_msg = f"""As you decend the far side of the bridge you find yourself in 
the middle of a clearing covered by ruins. The ruins seem to be divided into
a nine section square, you being in the center section. On the ground before
you is a square of 8 stones, 4 corners 4 sides. Each stone has a number 
carved into it and an unlit lantern above it. 
            \n{state.puzzle_string[0:1]} {state.puzzle_string[1:2]} {state.puzzle_string[2:3]}\n{state.puzzle_string[3:4]}   {state.puzzle_string[4:5]}\n{state.puzzle_string[5:6]} {state.puzzle_string[6:7]} {state.puzzle_string[7:8]}

            """
    else:
        triggered_temp = ""
        for idx, x in enumerate(state.puzzle_triggered):
            if x:
                triggered_temp = f"{triggered_temp} | {idx}"
        print_msg = f"""You return to the center square of the ruins. The square of
stones have the folowing aranngement
            \n{state.puzzle_string[0:1]} {state.puzzle_string[1:2]} {state.puzzle_string[2:3]}\n{state.puzzle_string[3:4]}   {state.puzzle_string[4:5]}\n{state.puzzle_string[5:6]} {state.puzzle_string[6:7]} {state.puzzle_string[7:8]}
            
        The following lanterns are lit:
            \n{triggered_temp}
            """
    choice_msg = """Where to go?\ngo back to BACKWOODS\nFIRST section\nSECOND section\nTHIRD section\nFOURTH section\nFIFTH section\nSIXTH section\nSEVENTH section\nEIGHTH section"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACKWOODS': Scenes.BACKWOODS,
            'FIRST': Scenes.FOREST_PUZZLE_ONE,
            'SECOND': Scenes.FOREST_PUZZLE_TWO,
            'THIRD': Scenes.FOREST_PUZZLE_THREE,
            'FOURTH': Scenes.FOREST_PUZZLE_FOUR,
            'FIFTH': Scenes.FOREST_PUZZLE_FIVE,
            'SIXTH': Scenes.FOREST_PUZZLE_SIX,
            'SEVENTH': Scenes.FOREST_PUZZLE_SEVEN,
            'EIGHTH': Scenes.FOREST_PUZZLE_EIGHT
        },
        "BACKWOODS, FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, EIGHTH"
    )

def forestPuzzleOne(state):
    num = state.section_number()
    print_msg = """You enter the  first square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """What what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_ONE_TRIGGER
        },
        "BACK, PULL"
    )

def forestPuzzleTwo(state):
    num = state.section_number()
    print_msg = """You enter the second square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
    state.current_scene,
    {
        'BACK': Scenes.FOREST_PUZZLE_CENTER,
        'PULL': Scenes.PUZZLE_TWO_TRIGGER
    },
        "BACK, PULL"
    )

def forestPuzzleThree(state):
    num = state.section_number()
    print_msg = """You enter the third square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_THREE_TRIGGER
        },
        "BACK, PULL"
    )

def forestPuzzleFour(state):
    num = state.section_number()
    print_msg = """You enter the fourth square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_FOUR_TRIGGER
        },
        "BACK, PULL"
    )

def forestPuzzleFive(state):
    num = state.section_number()
    print_msg = """You enter the five square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_FIVE_TRIGGER
        },
        "BACK, PULL"
    )

def forestPuzzleSix(state):
    num = state.section_number()
    print_msg = """You enter the sixth square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
    state.current_scene,
    {
        'BACK': Scenes.FOREST_PUZZLE_CENTER,
        'PULL': Scenes.PUZZLE_SIX_TRIGGER
    },
        "BACK, PULL"
    )

def forestPuzzleSeven(state):
    num = state.section_number()
    print_msg = """You enter the seventh square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_SEVEN_TRIGGER
        },
        "BACK, PULL"
    )

def forestPuzzleEight(state):
    num = state.section_number()
    print_msg = """You enter the eighth square. It is empty save for two rocks in the 
middle. One has the number {num} carved into it. The other has a lever
sticking out of it."""
    choice_msg = """Where what would you like to do?\ngo BACK to center square\nPULL the lever"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.FOREST_PUZZLE_CENTER,
            'PULL': Scenes.PUZZLE_EIGHT_TRIGGER
        },
        "BACK, PULL"
    )

def puzzleTriggerOne(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[0] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerTwo(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[1] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerThree(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[2] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerFour(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[3] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerFive(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[4] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerSix(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[5] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerSeven(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[6] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzleTriggerEight(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[7] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def forestMountainPath(state):
    print_msg = """You find yourself on a path that connects the forest puzzle with the
base of the mountain"""
    choice_msg = """where to go?\nforest PUZZLE\nmountain BASE"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'PUZZLE': Scenes.FOREST_PUZZLE,
            'BASE': Scenes.MOUNTAIN_BASE
        },
        "PUZZLE, BASE"
    )

def mountainPath1(state):
    print_msg = """You find yourself on a path that connects the clearing with the
mountain path."""
    choice_msg = """Where to go?\nback to CLEARING\nto mountian PATH""" 
    print(print_msg)
    print(choice_msg)
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
    print_msg = """You find yourself on a path that connects the mountain path and the base
of the mountain"""
    choice_msg = """where to go?\ngo to mountain PATH\ngo to BASE of the mountain"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'PATH': Scenes.MOUNTAIN_PATH,
            'ENTRANCE': Scenes.MOUNTAIN_BASE,
        },
        "ENTRANCE, PATH"
    )

def mountainBase(state):
    print_msg = """Base of the mountain\nSome people here to talk to\nmaybe sell some stuff\nalso connects to forest mountain path"""
    choice_msg = """where to go?\nBACK to mountain path\nmountain ENTRANCE\nforest mountain PATH"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """Mountain entrance\nconnects mountain base to m_LVL1_R1\nencounter here"""
    choice_msg = """where go?\nmountain BASE\nto LVL1"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """first room on the first floor\ncurrently connects to LVL1Stairs through mountain cave entrance\nalso connects to mountain entrance"""
    choice_msg = """where?\nmountain ENTRANCE\nto MCAVE"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """Mountain cave entrance\nmountain entrance to underwater cave\nalso connects LVL1 R1 and LVL1 Stairs"""
    choice_msg = """where?\nto LVL1\nto CAVE\nto USTAIRS lvl1 stairs"""
    print(print_msg)
    print(choice_msg)
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
    print_msg = """lvl1 stairs\nconnects lvl1 and lvl2\ncurrently goes from mountain cave entrance to LVL2 R1"""
    choice_msg = """where?\nto MCAVE\nto LVL2"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'MCAVE': Scenes.MOUNTAIN_CAVE_ENTRANCE,
            'LVL2': Scenes.M_LVL2_R1
        },
        "MCAVE, LVL2"
    )

def mLvl2R1(state):
    print_msg = """mountain LVL 2\nconnects to LVL1STAIRS and LVL2Stairs"""
    choice_msg = """where?\ngo USTAIRS staircase to lvl3\ngo DSTAIRS staircase to lvl1"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'DSTAIRS': Scenes.M_LVL1_STAIRS,
            'USTAIRS': Scenes.M_LVL2_STAIRS
        },
        "DSTAIRS, USTAIRS"
    )

def mLvl2Stairs(state):
    print_msg = """mountain lvl2 stairs to lvl 3\nconnects lvl2 to lvl3"""
    choice_msg = """where?\nto LVL2\nto LVL3"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'LVL2': Scenes.M_LVL2_R1,
            'LVL3': Scenes.M_LVL3_R1
        },
        "LVL2, LVL3"
    )

def mLv32R1(state):
    print_msg = """mountain lvl 3\nconnects to lvl2 stairs and lvl3stairs to boss"""
    choice_msg = """Where?\nto DSTAIRS staircase to lvl2\nto USTAIRS staircase to lvl3"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'DSTAIRS': Scenes.M_LVL2_STAIRS,
            'USTAIRS': Scenes.M_LVL3_STAIRS
        },
        "DSTAIRS, USTAIRS"
    )

def mLvl3Stairs(state):
    print_msg = """mountain lvl 3 stairs\nconnect lvl3 with boss area"""
    choice_msg = """where?\nto LVL3\nUP to boss area"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'LVL3': Scenes.M_LVL3_R1,
            'UP': Scenes.BOSS_AREA
        },
        "LVL3, UP"
    )

def bossArea(state):
    print_msg = """Boss area\nwhere final encounter will take place\ngoes only back to LVL3 stairs"""
    choice_msg = """where?\nBACK down stairs"""
    print(print_msg)
    print(choice_msg)
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
    print("")
    play = str(input(""))
    print("would you like to play? Y/N")
    play = str(input(": ")).upper()
    if play == "Y":
        state = State()
        state.play()
    else:
        print("Ok bye")




main()
