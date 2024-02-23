#asdf

# import enums
from enums import Scenes, InvItem
from os import name
import os

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


def beginning(state):
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


def beginning2(state):
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

def pond_approach(state):
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

def throwrock(state):
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

def pond_jump(state):
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

def pond_out(state):
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

def pond_down(state):
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

def pond_back(state):
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


def grab_pendant(state):
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

def pond_cave_1(state):
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

def pond_cave_2(state):
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

def pond_cave_3(state):
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

def pond_cave_4(state):
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

def pond_cave_5(state):
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

def pond_cave_6(state):
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

def pond_cave_7(state):
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

def pond_cave_8(state):
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

def pond_cave_9(state):
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

def pond_cave_10(state):
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

def pond_cave_11(state):
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

def pond_cave_12(state):
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

def pond_cave_13(state):
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

def pond_cave_14(state):
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

def pond_cave_15(state):
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

def pond_cave_16(state):
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

def pond_cave_17(state):
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

def pond_cave_18(state):
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

def pond_cave_19(state):
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

def pond_cave_20(state):
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

def enter_forest(state):
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

def for_path(state):
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

def light_village(state):
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
body in the shallow basin. 'I wasnt sure how to use them, or what they
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
    print_msg6 = """Once you step out of the basin you dry youself off,
the villager politely turns their back, though for some reason you feel at
ease in their presence. They hand you some clothes and sandles, look
you over and smile, 'You really are quite similar to us though you
come from so far.' You detect a playfulness in their voice as they drift
towards the door. 'Tis a shame, maybe in another life perhaps.' In the
doorway they turn on their heel and face you. 'Ill see you in a bit, come
outside when you are done.' You call to them as they turn to leave, 'Wait,
what's your name?' They turn to you and smile, looking you over again."""
    print(print_msg6)
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Scenes.CEREMONY_OF_LIGHT, Scenes.CEREMONY_OF_LIGHT



def ceremony_of_light(state):
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

def col_encounter(state):
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

def forest_cave_clearing_in(state):
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

def forest_cave_clearing_out(state):
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


def forest_cave_entrance_in(state):
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

def forest_cave_entrance_out(state):
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


def forest_puzzle(state):
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

def forest_puzzle_center(state):
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
        state.reset_board()
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

def forest_puzzle_one(state):
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

def forest_puzzle_two(state):
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

def forest_puzzle_three(state):
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

def forest_puzzle_four(state):
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

def forest_puzzle_five(state):
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

def forest_puzzle_six(state):
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

def forest_puzzle_seven(state):
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

def forest_puzzle_eight(state):
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

def puzzle_trigger_one(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[0] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_two(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[1] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_three(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[2] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_four(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[3] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_five(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[4] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_six(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[5] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_seven(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[6] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def puzzle_trigger_eight(state):
    print_msg = """You reach forward and grab the lever. There is a slight rumble and a click
at the base. You you wait a second in silence before returning to the
center section"""
    print(print_msg)
    state.puzzle_triggered[7] = True;
    hld = str(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    return state.current_scene, Scenes.FOREST_PUZZLE_CENTER

def forest_mountain_path(state):
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

def mountain_path_1(state):
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

def mountain_path_2(state):
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
            'BASE': Scenes.MOUNTAIN_BASE,
        },
        "BASE, PATH"
    )

def mountain_base(state):
    print_msg = """Base of the mountain\nSome people here to talk to\nmaybe sell some stuff\nalso connects to forest mountain path"""
    choice_msg = """where to go?\nBACK to mountain path\nmountain ENTRANCE\nforest mountain path"""
    print(print_msg)
    print(choice_msg)
    return get_input(
        state.current_scene,
        {
            'BACK': Scenes.MOUNTAIN_PATH_2,
            'ENTRANCE': Scenes.MOUNTAIN_ENTRANCE,
            'FOREST': Scenes.FOREST_MOUTAIN_PATH
        },
        "BACK, ENTRANCE, FOREST"
    )

def mountain_entrance(state):
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

def m_lvl1_r1(state):
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

def mountain_cave_entrance(state):
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

def m_lvl1_stairs(state):
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

def m_lvl2_r1(state):
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

def m_lvl2_stairs(state):
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

def m_lv3_r1(state):
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

def m_lvl3_stairs(state):
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

def boss_area(state):
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
