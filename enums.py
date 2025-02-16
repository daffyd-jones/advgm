from enum import Enum, auto



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
