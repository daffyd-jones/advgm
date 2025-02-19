from enum import Enum, auto

class SceneProp(Enum):
    SCENE_MSG = auto()
    CHOICE_MSG = auto()
    OPTIONS = auto()

class InvItem(Enum):
    HEALTH_POTION = auto()
    STRENGTH_POTION = auto()
    AGILITY_POTION = auto()
    DEFENCE_POTION = auto()
    BREAD_HUNK = auto()

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
    # MENU = 'menu'
    # INVENTORY = 'inv'

    BEGINNING = auto() # -> MOUNTAIN_PATH, ENTER_FOREST, POND_APPROACH
    CLEARING = auto() # -> MOUNTAIN_PATH, ENTER_FOREST, POND_APPROACH
    # pond
    POND_APPROACH = auto() # -> POND_THROWROCK, POND_JUMP, CLEARING
    POND_THROWROCK = auto() # -> POND_JUMP, CLEARING
    POND_JUMP = auto() # -> POND_DOWN, POND_CAVE_3, POND_OUT
    POND_OUT = auto() # -> POND_JUMP, CLEARING
    POND_DOWN = auto() # -> GRAB_PENDANT, POND_BACK
    POND_BACK = auto() # -> POND_DOWN, POND_CAVE_3, POND_OUT
    GRAB_PENDANT = auto() # -> POND_OUT
    # pond cave
    # - may have different versions of each room for every enterance
    # - if 1 version exists per room the description of each must be
    # - written to make sense from all directions ex. opening behind a rock
    # - as opposed to providing more organic directional
    # - experience ex. opening to the left and ahead
    POND_CAVE_1 = auto() # -> 2
    POND_CAVE_2 = auto() # -> 1, 3, 7
    POND_CAVE_3 = auto() #pond entrance -> 2, 4
    POND_CAVE_4 = auto() # -> 3, 5, 9
    POND_CAVE_5 = auto() # -> 4
    POND_CAVE_6 = auto() # -> 7, 11
    POND_CAVE_7 = auto() # -> 2, 6, 8
    POND_CAVE_8 = auto() # -> 7, 13
    POND_CAVE_9 = auto() # -> 4, 10
    POND_CAVE_10 = auto() # -> 9, 15
    POND_CAVE_11 = auto() # -> 6,
    POND_CAVE_12 = auto() # -> 13, 17
    POND_CAVE_13 = auto() # -> 8, 12, 14
    POND_CAVE_14 = auto() # -> 13, 15, 19
    POND_CAVE_15 = auto() # -> 10, 14
    POND_CAVE_16 = auto() #mountain entrance -> 17
    POND_CAVE_17 = auto() # -> 12, 16, 18
    POND_CAVE_18 = auto() # -> 17,
    POND_CAVE_19 = auto() # -> 14, 20
    POND_CAVE_20 = auto() #forest entrance -> 19
    # Forest
    # - forest entrance
    ENTER_FOREST = auto() # -> CLEARING, FOREST_PATH
    FOREST_PATH = auto() # -> LIGHT_VILLAGE
    LOST_IN_FOREST = auto() 
    # - light village
    LIGHT_VILLAGE_1 = auto() # -> CEREMONY_OF_LIGHT
    LIGHT_VILLAGE_2 = auto() # -> CEREMONY_OF_LIGHT
    LIGHT_VILLAGE_3= auto() # -> CEREMONY_OF_LIGHT

    CEREMONY_OF_LIGHT_1 = auto() # -> COL_ENCOUNTER
    CEREMONY_OF_LIGHT_2 = auto() # -> COL_ENCOUNTER
    CEREMONY_OF_LIGHT_3 = auto() # -> COL_ENCOUNTER
    # - ceremony of light conflict
    COL_ENCOUNTER = auto() # -> BACKWOODS

    # - back of forest
    BACKWOODS = auto() # -> ENTER_FOREST, FOREST_CAVE_CLEARING_IN, FOREST_PUZZLE
    # - some kind of puzzle thing
    FOREST_PUZZLE = auto() # -> BACKWOODS, FOREST_MOUNTAIN_PATH

    # FOREST_PUZZLE_CENTER = auto() 

    # FOREST_PUZZLE_ONE = auto() 
    # FOREST_PUZZLE_TWO = auto() 
    # FOREST_PUZZLE_THREE = auto() 
    # FOREST_PUZZLE_FOUR = auto() 
    # FOREST_PUZZLE_FIVE = auto() 
    # FOREST_PUZZLE_SIX = auto() 
    # FOREST_PUZZLE_SEVEN = auto() 
    # FOREST_PUZZLE_EIGHT = auto() 

    # PUZZLE_ONE_TRIGGER = auto() 
    # PUZZLE_TWO_TRIGGER = auto() 
    # PUZZLE_THREE_TRIGGER = auto() 
    # PUZZLE_FOUR_TRIGGER = auto() 
    # PUZZLE_FIVE_TRIGGER = auto() 
    # PUZZLE_SIX_TRIGGER = auto() 
    # PUZZLE_SEVEN_TRIGGER = auto() 
    # PUZZLE_EIGHT_TRIGGER = auto() 



    FOREST_MOUTAIN_PATH = auto() # -> FOREST_PUZZLE, MOUNTAIN_BASE
    # - forest pond cave entrance
    FOREST_CAVE_CLEARING_IN = auto() # -> BACKWOODS, FOREST_CAVE_ENTRANCE_IN
    FOREST_CAVE_CLEARING_OUT = auto() # -> BACKWOODS, FOREST_CAVE_ENTRANCE_IN
    FOREST_CAVE_ENTRANCE_IN = auto() # -> POND_CAVE_20, FOREST_CAVE_CLEARING_OUT
    FOREST_CAVE_ENTRANCE_OUT = auto() # -> POND_CAVE_20, FOREST_CAVE_CLEARING_OUT

    # Mountain
    # - mountain path
    MOUNTAIN_PATH_1 = auto() # -> CLEARING, MOUNTAIN_PATH_2
    MOUNTAIN_PATH_2 = auto() # -> MOUNTAIN_PATH, MOUNTAIN_BASE

    # - mountain base
    MOUNTAIN_BASE = auto() # -> MOUNTAIN_PATH_2, MOUNTAIN_ENTRANCE, FOREST_MOUNTAIN_PATH
    MOUNTAIN_ENTRANCE = auto() # -> MOUNTAIN_BASE, M_LVL1_R1
    # - mountain lvl 1
    M_LVL1_R1 = auto() # -> MOUNTAIN_ENTRANCE, MOUNTAIN_CAVE_ENTRANCE
    MOUNTAIN_CAVE_ENTRANCE = auto() # -> M_LVL1_R1, M_LVL1_STAIRS, POND_CAVE_16
    M_LVL1_STAIRS = auto() # -> M_LVL2_R1, MOUNTAIN_CAVE_ENTRANCE
    # - mountain lvl 2
    M_LVL2_R1 = auto() # -> M_LVL1_STAIRS, M_LVL2_STAIRS
    M_LVL2_STAIRS = auto() # -> M_LVL2_R1, M_LVL3_R1
    # - mountain lvl 3
    M_LVL3_R1 = auto() # -> M_LVL2_STAIRS, M_LVL3_STAIRS
    M_LVL3_STAIRS = auto() # -> M_LVL3_R1, BOSS_AREA
    # - boss area
    BOSS_AREA = auto() # -> M_LVL3_STAIRS
