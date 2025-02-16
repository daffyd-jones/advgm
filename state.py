import json
from os import name
import os
import time
from random import random as rand
from random import seed, choice
import math
from enum import Enum, auto

from enums import Scenes, InvItem
import scenes

from inventory import Inventory
# from scenes import Beginning

PUZZ_ROW = 2
PUZZ_COL = 8

def remfront(st):
    remain = st[1:]
    return remain

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
        # self.reset_puzzle = True
        self.puzzle_arr = [[0] * PUZZ_COL for _ in range(PUZZ_ROW)]
        self.puzzle_triggered = [False, False, False, False, False, False, False, False]
        self.puzzle_sections = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.puzzle_stuff = {
                'init': True,
                'win': False,
                'arr': [[0] * PUZZ_COL for _ in range(PUZZ_ROW)],
                'triggered': [False, False, False, False, False, False, False, False],
                'sections': ["1", "2", "3", "4", "5", "6", "7", "8"],
                'key': ""
            }
        self.sceneMap = {
            Scenes.BEGINNING: getattr(scenes, 'beginning'),
            Scenes.ENTER_FOREST: getattr(scenes, 'enter_forest'),
            Scenes.CLEARING: getattr(scenes, 'beginning2'),
            Scenes.POND_APPROACH: getattr(scenes, 'pond_approach'),
            Scenes.POND_THROWROCK: getattr(scenes, 'throwrock'),
            Scenes.POND_JUMP: getattr(scenes, 'pond_jump'),
            Scenes.POND_DOWN: getattr(scenes, 'pond_down'),
            Scenes.GRAB_PENDANT: getattr(scenes, 'grab_pendant'),
            Scenes.POND_OUT: getattr(scenes, 'pond_out'),
            Scenes.POND_BACK: getattr(scenes, 'pond_back'),
            Scenes.FOREST_PATH: getattr(scenes, 'for_path'),
            Scenes.LIGHT_VILLAGE: getattr(scenes, 'light_village'),
            Scenes.CEREMONY_OF_LIGHT: getattr(scenes, 'ceremony_of_light'),
            Scenes.COL_ENCOUNTER: getattr(scenes, 'col_encounter'),
            Scenes.BACKWOODS: getattr(scenes, 'backwoods'),
            Scenes.FOREST_PUZZLE: getattr(scenes, 'forest_puzzle'),
            Scenes.FOREST_PUZZLE_CENTER: getattr(scenes, 'forest_puzzle_center'),
            Scenes.FOREST_PUZZLE_ONE: getattr(scenes, 'forest_puzzle_one'),
            Scenes.FOREST_PUZZLE_TWO: getattr(scenes, 'forest_puzzle_two'),
            Scenes.FOREST_PUZZLE_THREE: getattr(scenes, 'forest_puzzle_three'),
            Scenes.FOREST_PUZZLE_FOUR: getattr(scenes, 'forest_puzzle_four'),
            Scenes.FOREST_PUZZLE_FIVE: getattr(scenes, 'forest_puzzle_five'),
            Scenes.FOREST_PUZZLE_SIX: getattr(scenes, 'forest_puzzle_six'),
            Scenes.FOREST_PUZZLE_SEVEN: getattr(scenes, 'forest_puzzle_seven'),
            Scenes.FOREST_PUZZLE_EIGHT: getattr(scenes, 'forest_puzzle_eight'),
            Scenes.PUZZLE_ONE_TRIGGER: getattr(scenes, 'puzzle_trigger_one'),
            Scenes.PUZZLE_TWO_TRIGGER: getattr(scenes, 'puzzle_trigger_two'),
            Scenes.PUZZLE_THREE_TRIGGER: getattr(scenes, 'puzzle_trigger_three'),
            Scenes.PUZZLE_FOUR_TRIGGER: getattr(scenes, 'puzzle_trigger_four'),
            Scenes.PUZZLE_FIVE_TRIGGER: getattr(scenes, 'puzzle_trigger_five'),
            Scenes.PUZZLE_SIX_TRIGGER: getattr(scenes, 'puzzle_trigger_six'),
            Scenes.PUZZLE_SEVEN_TRIGGER: getattr(scenes, 'puzzle_trigger_seven'),
            Scenes.PUZZLE_EIGHT_TRIGGER: getattr(scenes, 'puzzle_trigger_eight'),
            Scenes.FOREST_MOUTAIN_PATH: getattr(scenes, 'forest_mountain_path'),
            Scenes.FOREST_CAVE_ENTRANCE_IN: getattr(scenes, 'forest_cave_entrance_in'),
            Scenes.FOREST_CAVE_ENTRANCE_OUT: getattr(scenes, 'forest_cave_entrance_out'),
            Scenes.FOREST_CAVE_CLEARING_IN: getattr(scenes, 'forest_cave_clearing_in'),
            Scenes.FOREST_CAVE_CLEARING_OUT: getattr(scenes, 'forest_cave_clearing_out'),
            Scenes.POND_CAVE_1: getattr(scenes, 'pond_cave_1'),
            Scenes.POND_CAVE_2: getattr(scenes, 'pond_cave_2'),
            Scenes.POND_CAVE_3: getattr(scenes, 'pond_cave_3'),
            Scenes.POND_CAVE_4: getattr(scenes, 'pond_cave_4'),
            Scenes.POND_CAVE_5: getattr(scenes, 'pond_cave_5'),
            Scenes.POND_CAVE_6: getattr(scenes, 'pond_cave_6'),
            Scenes.POND_CAVE_7: getattr(scenes, 'pond_cave_7'),
            Scenes.POND_CAVE_8: getattr(scenes, 'pond_cave_8'),
            Scenes.POND_CAVE_9: getattr(scenes, 'pond_cave_9'),
            Scenes.POND_CAVE_10: getattr(scenes, 'pond_cave_10'),
            Scenes.POND_CAVE_11: getattr(scenes, 'pond_cave_11'),
            Scenes.POND_CAVE_12: getattr(scenes, 'pond_cave_12'),
            Scenes.POND_CAVE_13: getattr(scenes, 'pond_cave_13'),
            Scenes.POND_CAVE_14: getattr(scenes, 'pond_cave_14'),
            Scenes.POND_CAVE_15: getattr(scenes, 'pond_cave_15'),
            Scenes.POND_CAVE_16: getattr(scenes, 'pond_cave_16'),
            Scenes.POND_CAVE_17: getattr(scenes, 'pond_cave_17'),
            Scenes.POND_CAVE_18: getattr(scenes, 'pond_cave_18'),
            Scenes.POND_CAVE_19: getattr(scenes, 'pond_cave_19'),
            Scenes.POND_CAVE_20: getattr(scenes, 'pond_cave_20'),
            Scenes.MOUNTAIN_PATH: getattr(scenes, 'mountain_path_1'),
            Scenes.MOUNTAIN_PATH_2: getattr(scenes, 'mountain_path_2'),
            Scenes.MOUNTAIN_BASE: getattr(scenes, 'mountain_base'),
            Scenes.MOUNTAIN_ENTRANCE: getattr(scenes, 'mountain_entrance'),
            Scenes.MOUNTAIN_CAVE_ENTRANCE: getattr(scenes, 'mountain_cave_entrance'),
            Scenes.M_LVL1_R1: getattr(scenes, 'm_lvl1_r1'),
            Scenes.M_LVL1_STAIRS: getattr(scenes, 'm_lvl1_stairs'),
            Scenes.M_LVL2_R1: getattr(scenes, 'm_lvl2_r1'),
            Scenes.M_LVL2_STAIRS: getattr(scenes, 'm_lvl2_stairs'),
            Scenes.M_LVL3_R1: getattr(scenes, 'm_lv3_r1'),
            Scenes.M_LVL3_STAIRS: getattr(scenes, 'm_lvl3_stairs'),
            Scenes.BOSS_AREA: getattr(scenes, 'boss_area'),
        }

    def __str__(self) -> str:
        return  f'\n--------'\
                f'\nhp: {self.hp}\n'\
                f"atk: {self.hit_rate}\n"\
                f'--------\n'

    def play(self, start_scene):
        self.play_bool = True
        os.system('cls' if os.name == 'nt' else 'clear')
        if start_scene != None:
            key = next((scene for scene in Scenes if scene.value == start_scene), None)
            self.current_scene = key
        while self.play_bool:
            if self.current_scene == Scenes.INVENTORY:
                self.use_inventory()
            if self.current_scene == Scenes.MENU:
                self.use_menu()
            self.current_scene, self.scene_hold = self.sceneMap[self.current_scene](self)
            if self.current_scene == None:
                return None
                pass



    def play_turn(self, current_scene):
        # self.play_bool = True
        #os.system('cls' if os.name == 'nt' else 'clear')
        #if start_scene != None:
        #    key = next((scene for scene in Scenes if scene.value == start_scene), None)
        #    self.current_scene = key
        #while self.play_bool:
        # if self.current_scene == Scenes.INVENTORY:
        #     self.use_inventory()
        # if self.current_scene == Scenes.MENU:
        #     self.use_menu()
        return self.sceneMap[self.current_scene](self)
        # if self.current_scene == None:
        #     return None



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

    def get_inventory(self):
        return self.inventory.get_inventory()

    def use_inv_item(self, itemtype):
        self.inventory.use_item(itemtype)
        match itemtype:
            case "Health Potion":
                self.hp += 10;
            case "Strength Potion":
                self.hit_rate += 2;
            case "Agility Potion":
                self.attack += 2;
            case "Defence Potion":
                self.defence += 2;
            case "Bread Hunk":
                self.hp += 1;
                

    def hp_dec(self,amt):
        self.hp -= amt


    def encounter(self, probOfAttack, encounterMap):
        if probOfAttack != 1:
            num = rand()
            if num < probOfAttack:
                return True
        intro_txt = encounterMap['intro_txt']
        fight_txt = encounterMap["fight_txt"]
        after_txt = encounterMap["after_txt"]
        print(f"Encounter with {encounterMap['name']} ")
        print(f"")
        print(f"{ intro_txt }")
        # input(": ")
        fight = True
        hp = encounterMap["hp"]
        attack = encounterMap["attack"]
        coin = rand()
        you_turn = True
        if coin > 0.5:
            you_turn = False
        while fight:
            input(": ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if you_turn:
                you_turn = False
            else:
                you_turn = True
            msg = rand() * 10
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
                    print("")
                    if response == "HEALTH":
                        pturn = False
                        self.hp += 10
                        pass
                    elif response == "POWER":
                        pturn = False
                        self.hit_rate += 2
                        pass
                    elif response == "ATTACK":
                        pturn = False
                        c = 0
                        acc = 0
                        while c < 3:
                            roll = int(rand() * self.attack)
                            acc += roll
                            c += 1
                        print(f"your roll: {acc}")
                        if acc > encounterMap["defence"]:
                            hp -= self.hit_rate
                            print(f"attack a success! {encounterMap['name']} has lost")
                            print(f"{self.hit_rate} health and now has {hp}")
                        else:
                            print("you failed to hit target")
                    else:
                        print("Not a valid response")
            else:
                print(f"\nIt is {encounterMap['name']}'s turn")
                seed(rand())
                c = 0
                acc = 0
                while c < 3:
                    roll = int(rand() * attack)
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
                print('\nyou have died')
                input(": ")
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
        for i in self.puzzle_stuff['triggered']:
            i = False
        for i in range(0, 2):
            seed(time.time())
            print(f"i: {i}")
            temp_sections = list(self.puzzle_stuff['sections'])
            for l in range(len(temp_sections)):
                item = choice(temp_sections)
                self.puzzle_stuff['arr'][i][l] = item
                temp_sections.remove(item)
        print(f"puzzle: {self.puzzle_stuff['arr']}")
        temp = ''
        for i in range(1, 9):
            idx = self.puzzle_stuff['arr'][0].index(str(i))
            temp += self.puzzle_stuff['arr'][1][idx]
        self.puzzle_stuff['key'] = temp
        print(f"Key: {self.puzzle_stuff['key']}")

    def puzzle_complete(self):
        return self.puzzle_stuff['win']

    def section_number(self, section):
        return self.puzzle_stuff['arr'][1][section - 1]

    def puzzle_check_move(self, num):

        order = self.puzzle_stuff['key'].index(f'{num}')
        if order == 0:
            print("first checked")
            self.puzzle_stuff['triggered'][0] = True
            return
        t = True
        for i in range(0 , order):
            if not self.puzzle_stuff['triggered'][i]:
                t = False
        if not t:
            print("failure")
            self.reset_board()
            return
        print("pass")
        if order == 7:
            self.puzzle_stuff['win'] = True
        self.puzzle_stuff['triggered'][order] = True



    def get_new_puzzle(self):
        return self.reset_puzzle

    def init_puzzle_true(self):
        self.init_puzzle = True

    def init_puzzle_false(self):
        self.init_puzzle = False

    def is_init_puzzle(self):
        return self.init_puzzle

    def get_puzzle_stuff(self):
        return self.puzzle_stuff
