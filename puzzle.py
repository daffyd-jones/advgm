
def forest_puzzle_center(state):
    if state.puzzle_complete():
        print_msg = """As you return to the center puzzle section you notice a change
to the region. The lanterns are all lit and there is now a hole in the ground
in the middle of the square of stones. You cautiously move forward into the
hole"""
        print(print_msg)
        hld = str(input(""))
        os.system('cls' if os.name == 'nt' else 'clear')
        return Scenes.FOREST_MOUTAIN_PATH, Scenes.FOREST_MOUTAIN_PATH
    if state.is_init_puzzle():
        state.init_puzzle_false()
        state.reset_board()
        print_msg = f"""As you decend the far side of the bridge you find yourself in
the middle of a clearing covered by ruins. The ruins seem to be divided into
a nine section square, you being in the center section. On the ground before
you is a square of 8 stones, 4 corners 4 sides. Each stone has a number
carved into it and an unlit lantern above it.
            \n{state.puzzle_stuff['arr'][0][0]} {state.puzzle_stuff['arr'][0][1]} {state.puzzle_stuff['arr'][0][2]}\n{state.puzzle_stuff['arr'][0][3]}   {state.puzzle_stuff['arr'][0][4]}\n{state.puzzle_stuff['arr'][0][5]} {state.puzzle_stuff['arr'][0][6]} {state.puzzle_stuff['arr'][0][7]}

            """
    else:
        triggered_temp = ""
        for idx, x in enumerate(state.get_puzzle_stuff()['triggered']):
            if x:
                triggered_temp += f"\n{triggered_temp} | {idx}"
        print_msg = f"""You return to the center square of the ruins. The square of
stones have the folowing aranngement
            \n{state.puzzle_stuff['arr'][0][0]} {state.puzzle_stuff['arr'][0][1]} {state.puzzle_stuff['arr'][0][2]}\n{state.puzzle_stuff['arr'][0][3]}   {state.puzzle_stuff['arr'][0][4]}\n{state.puzzle_stuff['arr'][0][5]} {state.puzzle_stuff['arr'][0][6]} {state.puzzle_stuff['arr'][0][7]}

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

def forest_puzzle_one(state):
    num = state.section_number(1)
    print_msg = f"""You enter the  first square. It is empty save for two rocks in the
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

def forest_puzzle_two(state):
    num = state.section_number(2)
    print_msg = f"""You enter the second square. It is empty save for two rocks in the
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

def forest_puzzle_three(state):
    num = state.section_number(3)
    print_msg = f"""You enter the third square. It is empty save for two rocks in the
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

def forest_puzzle_four(state):
    num = state.section_number(4)
    print_msg = f"""You enter the fourth square. It is empty save for two rocks in the
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

def forest_puzzle_five(state):
    num = state.section_number(5)
    print_msg = f"""You enter the five square. It is empty save for two rocks in the
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

def forest_puzzle_six(state):
    num = state.section_number(6)
    print_msg = f"""You enter the sixth square. It is empty save for two rocks in the
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

def forest_puzzle_seven(state):
    num = state.section_number(7)
    print_msg = f"""You enter the seventh square. It is empty save for two rocks in the
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

def forest_puzzle_eight(state):
    num = state.section_number(8)
    print_msg = f"""You enter the eighth square. It is empty save for two rocks in the
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

def puzzle_trigger_one(state):
    state.puzzle_check_move(1)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    print("hey")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("hey")
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_two(state):
    state.puzzle_check_move(2)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_three(state):
    state.puzzle_check_move(3)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_four(state):
    state.puzzle_check_move(4)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_five(state):
    state.puzzle_check_move(5)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_six(state):
    state.puzzle_check_move(6)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_seven(state):
    state.puzzle_check_move(7)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_eight(state):
    state.puzzle_check_move(8)
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.FOREST_PUZZLE_CENTER, Scenes.FOREST_PUZZLE_CENTER


# def mountain_entrance(state):
#     win = state.encounter(
#         0.1,
#         encounterMap = {
#             'name': 'racoon man',
#             'hp': 20,
#             'defence': 4,
#             'hit_rate': 2,
#             'attack': 2,
#             'prize': "health",
#             'intro_txt': 'hey i dont like you so im gonna stab ya.',
#             'fight_txt': [
#                 'you fuck off',
#                 'gonna fight ya',
#                 'knife fight',
#             ],
#             'after_txt': 'ok you win ouch. have a health potion',
#         },
#     )
#     if not win:
#         return None, None



# def forest_mountain_path(state):
#     print_msg = ""
#     if state.puzzle_complete():
#         print_msg = """You find yourself on a path that leads from the base of the mountain
# into the forest. A feild extends from the wild forest to the shadow of the
# mountain's base. The bushes and trees steadily grow more numerous as the feild
# gradually turns into a dense tangle of growth. Would you like to go towards the
# mountain base, or venture into the forest?"""
#         choice_msg = """where to go?\nenter FOREST\nmountain BASE"""
#         print(print_msg)
#         print(choice_msg)
#         return get_input(
#             state.current_scene,
#             {
#                 'PUZZLE': Scenes.FOREST_PUZZLE,
#                 'BASE': Scenes.MOUNTAIN_BASE
#             },
#             "PUZZLE, BASE"
#         )
#     else:
#         print_msg = """You find yourself on a path that leads from the base of the mountain
# into the forest. A feild extends from the wild forest to the shadow of the
# mountain's base. The bushes and trees steadily grow more numerous as the feild
# gradually turns into a dense tangle of growth. Would you like to go towards the
# mountain base, or venture into the forest?"""
#         choice_msg = """where to go?\nenter FOREST\nmountain BASE"""
#         print(print_msg)
#         print(choice_msg)
#         response = str(input(": ")).upper()
#         response.strip()
#         if response == "FOREST":
#             forest_msg = """You enter the forest and manuver your way through the trees.
# as you continue the trees and growth become overwhelming and you become lost.
# After some aimless wandering, you find that the growth begins to thin. As you
# round a large rock you look up and see the mountain. You look around, you seem
# to be in the same feild that you were in previously. It seems you cannot enter
# the forest at this time."""
#     choice_msg = """where to go?\nmountain BASE"""
#     print(forest_msg)
#     print(choice_msg)
#     return get_input(
#         state.current_scene,
#         {
#             'BASE': Scenes.MOUNTAIN_BASE
#         },
#         "BASE"
#     )


#############
#
#   get_input(current_scene, scene_map, words)
#   - gets respone from player and returns appropriate Scene Enums
#   - if response is INV returns Scenes.INVENTORY and current scene
#   - if response is MENU returns Scenes.MENU and current scene
#   - else
#
# def get_input(current_scene, scene_map, words):
#     p = True
#     out = scene_map
#     while p:
#         response = str(input(": ")).upper()
#         response.strip()
#         if response in out or response == "INV" or response == "MENU":
#             if response == "INV":
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 return Scenes.INVENTORY, current_scene
#             elif response == "MENU":
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 return Scenes.MENU, current_scene
#             elif response in out:
#                 print(f"resp {response}") #Print out - delete after completion
#                 print(f"enum {out[response]}") #Print out - delete after completion
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 return out[response], out[response]
#         else:
#             print(f'Not a proper response try: {words}')






