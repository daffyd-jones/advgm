import json
from os import name
import os
import time
from random import random as rand
from random import seed, choice
import math
from enum import Enum, auto

from enums import Scenes, InvItem
from scenes import *

from inventory import Inventory
# from scenes import Beginning

PUZZ_ROW = 2
PUZZ_COL = 8

def remfront(st):
    remain = st[1:]
    return remain


SCENE_MAP = {
    Scenes.BEGINNING: BEGINNING,
    Scenes.ENTER_FOREST: ENTER_FOREST,
    Scenes.CLEARING: CLEARING,
    Scenes.POND_APPROACH: POND_APPROACH,
    Scenes.POND_THROWROCK: POND_THROWROCK,
    Scenes.POND_JUMP: POND_JUMP,
    Scenes.POND_DOWN: POND_DOWN,
    Scenes.GRAB_PENDANT: GRAB_PENDANT,
    Scenes.POND_OUT: POND_OUT,
    Scenes.POND_BACK: POND_BACK,
    Scenes.FOREST_PATH: FOREST_PATH,
    Scenes.LIGHT_VILLAGE_1: LIGHT_VILLAGE_1,
    Scenes.LIGHT_VILLAGE_2: LIGHT_VILLAGE_2,
    Scenes.LIGHT_VILLAGE_3: LIGHT_VILLAGE_3,
    Scenes.CEREMONY_OF_LIGHT_1: CEREMONY_OF_LIGHT_1,
    Scenes.CEREMONY_OF_LIGHT_2: CEREMONY_OF_LIGHT_2,
    Scenes.CEREMONY_OF_LIGHT_3: CEREMONY_OF_LIGHT_3,
    Scenes.COL_ENCOUNTER: COL_ENCOUNTER,
    Scenes.BACKWOODS: BACKWOODS,
    Scenes.FOREST_PUZZLE: FOREST_PUZZLE,
    # Scenes.FOREST_PUZZLE_CENTER: FOREST_PUZZLE_CENTER,
    # Scenes.FOREST_PUZZLE_ONE: FOREST_PUZZLE_ONE,
    # Scenes.FOREST_PUZZLE_TWO: FOREST_PUZZLE_TWO,
    # Scenes.FOREST_PUZZLE_THREE: FOREST_PUZZLE_THREE,
    # Scenes.FOREST_PUZZLE_FOUR: FOREST_PUZZLE_FOUR,
    # Scenes.FOREST_PUZZLE_FIVE: FOREST_PUZZLE_FIVE,
    # Scenes.FOREST_PUZZLE_SIX: FOREST_PUZZLE_SIX,
    # Scenes.FOREST_PUZZLE_SEVEN: FOREST_PUZZLE_SEVEN,
    # Scenes.FOREST_PUZZLE_EIGHT: FOREST_PUZZLE_EIGHT,
    # Scenes.PUZZLE_ONE_TRIGGER: PUZZLE_ONE_TRIGGER,
    # Scenes.PUZZLE_TWO_TRIGGER: PUZZLE_TWO_TRIGGER,
    # Scenes.PUZZLE_THREE_TRIGGER: PUZZLE_THREE_TRIGGER,
    # Scenes.PUZZLE_FOUR_TRIGGER: PUZZLE_FOUR_TRIGGER,
    # Scenes.PUZZLE_FIVE_TRIGGER: PUZZLE_FIVE_TRIGGER,
    # Scenes.PUZZLE_SIX_TRIGGER: PUZZLE_SIX_TRIGGER,
    # Scenes.PUZZLE_SEVEN_TRIGGER: PUZZLE_SEVEN_TRIGGER,
    # Scenes.PUZZLE_EIGHT_TRIGGER: PUZZLE_EIGHT_TRIGGER,
    # Scenes.FOREST_MOUTAIN_PATH: FOREST_MOUTAIN_PATH,
    Scenes.FOREST_CAVE_ENTRANCE_IN: FOREST_CAVE_ENTRANCE_IN,
    Scenes.FOREST_CAVE_ENTRANCE_OUT: FOREST_CAVE_ENTRANCE_OUT,
    Scenes.FOREST_CAVE_CLEARING_IN: FOREST_CAVE_CLEARING_IN,
    Scenes.FOREST_CAVE_CLEARING_OUT: FOREST_CAVE_CLEARING_OUT,
    Scenes.POND_CAVE_1: POND_CAVE_1,
    Scenes.POND_CAVE_2: POND_CAVE_2,
    Scenes.POND_CAVE_3: POND_CAVE_3,
    Scenes.POND_CAVE_4: POND_CAVE_4,
    Scenes.POND_CAVE_5: POND_CAVE_5,
    Scenes.POND_CAVE_6: POND_CAVE_6,
    Scenes.POND_CAVE_7: POND_CAVE_7,
    Scenes.POND_CAVE_8: POND_CAVE_8,
    Scenes.POND_CAVE_9: POND_CAVE_9,
    Scenes.POND_CAVE_10: POND_CAVE_10,
    Scenes.POND_CAVE_11: POND_CAVE_11,
    Scenes.POND_CAVE_12: POND_CAVE_12,
    Scenes.POND_CAVE_13: POND_CAVE_13,
    Scenes.POND_CAVE_14: POND_CAVE_14,
    Scenes.POND_CAVE_15: POND_CAVE_15,
    Scenes.POND_CAVE_16: POND_CAVE_16,
    Scenes.POND_CAVE_17: POND_CAVE_17,
    Scenes.POND_CAVE_18: POND_CAVE_18,
    Scenes.POND_CAVE_19: POND_CAVE_19,
    Scenes.POND_CAVE_20: POND_CAVE_20,
    Scenes.MOUNTAIN_PATH_1: MOUNTAIN_PATH_1,
    Scenes.MOUNTAIN_PATH_2: MOUNTAIN_PATH_2,
    Scenes.MOUNTAIN_BASE: MOUNTAIN_BASE,
    Scenes.MOUNTAIN_ENTRANCE: MOUNTAIN_ENTRANCE,
    Scenes.MOUNTAIN_CAVE_ENTRANCE: MOUNTAIN_CAVE_ENTRANCE,
    Scenes.M_LVL1_R1: M_LVL1_R1,
    Scenes.M_LVL1_STAIRS: M_LVL1_STAIRS,
    Scenes.M_LVL2_R1: M_LVL2_R1,
    Scenes.M_LVL2_STAIRS: M_LVL2_STAIRS,
    Scenes.M_LVL3_R1: M_LVL3_R1,
    Scenes.M_LVL3_STAIRS: M_LVL3_STAIRS,
    Scenes.BOSS_AREA: BOSS_AREA,
}

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
        self.stats = {
            'hp': 50,
            'money': 10,
            'defence': 10,
            'hit_rate': 5,
            'attack': 10
        }
        self.current_scene = Scenes.BEGINNING
        self.scene_hold = Scenes.BEGINNING
        self.inventory = Inventory()
        self.inv_prize = {
            InvItem.HEALTH_POTION: self.inventory.add_item(InvItem.HEALTH_POTION),
            InvItem.STRENGTH_POTION: self.inventory.add_item(InvItem.STRENGTH_POTION)
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

    def __str__(self) -> str:
        return  f'\n--------'\
                f'\nhp: {self.hp}\n'\
                f"atk: {self.hit_rate}\n"\
                f'--------\n'

    def play_turn(self, current_scene):
        return SCENE_MAP[current_scene]

    def level_up(self, hp, defence, attack):
        self.stats['hp'] = hp
        self.stats['defence'] = defence
        self.stats['attack'] = attack

    def get_inventory(self):
        return self.inventory.get_inventory()

    def use_inv_item(self, itemtype):
        self.inventory.use_item(itemtype)
        match itemtype:
            case InvItem.HEALTH_POTION:
                self.stats['hp'] += 10;
            case InvItem.STRENGTH_POTION:
                self.stats['hit_rate'] += 2;
            case InvItem.AGILITY_POTION:
                self.stats['attack'] += 2;
            case InvItem.DEFENCE_POTION:
                self.stats['defence'] += 2;
            case InvItem.BREAD_HUNK:
                self.stats['hp'] += 1;
        return self.inventory.get_inventory()
                
    def hp_dec(self,amt):
        self.hp -= amt

    def change_scene(self, scene):
        self.current_scene = scene
