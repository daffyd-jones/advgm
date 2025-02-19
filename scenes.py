
# import enums
from enums import Scenes, InvItem
from os import name
import os
import time

BEGINNING = {
    SceneProp.SCENE_MSG: """You awake feeling groggy and sore. Opening your eyes,
you look around. You appear to be in a clearing surrounded by tall
evergreens. Twenty yards to your right is a small pond, still and
surrounded by small ferns. Behind you, and beyond the forest towers a
mountain, cold and grey against the bright sky. It cast the forest and the
clearing below in shadow.""",
    SceneProp.CHOICE_MSG: """What do you want to do?\nWalk towards MOUNTAIN\nExplore FOREST\nLook at POND""",
    SceneProp.OPTIONS: {
        'MOUNTAIN': Scenes.MOUNTAIN_PATH,
        'FOREST': Scenes.ENTER_FOREST,
        'POND': Scenes.POND_APPROACH
    }
}

BEGINNING2 = {
    SceneProp.SCENE_MSG: """You stand in the center of the clearing that you awoke in""",
    SceneProp.CHOICE_MSG: """What do you want to do?\nWalk towards MOUNTAIN\nExplore FOREST\nLook at POND""",
    SceneProp.OPTIONS: {
        'MOUNTAIN': Scenes.MOUNTAIN_PATH,
        'FOREST': Scenes.ENTER_FOREST,
        'POND': Scenes.POND_APPROACH
    }
}

POND_APPROACH = {
    SceneProp.SCENE_MSG: """As you approach the pond you see a ripple of movement disturb
the smooth surface. Once on the bank you see something shimmering at the
bottom, nothing now stirrs in the clear water. You look around you. You see
a rock to your left.""",
    SceneProp.CHOICE_MSG: """What would yo like to do?\nTHROW rock into pond\nJUMP into pond\nRETURN to center of the clearing""",
    SceneProp.OPTIONS: {
        'THROW': Scenes.POND_THROWROCK,
        'JUMP': Scenes.POND_JUMP,
        'RETURN': Scenes.CLEARING
    }
}

THROWROCK = {
    SceneProp.SCENE_MSG: """You stoop to pick up the rock and raise it above your head. You
throw the rock with into the center of the pond with substantial force. It
bursts through the water with a loud splunk sound.\nYou wait for a moment.
Nothing happens.""",
    SceneProp.CHOICE_MSG: """What now?\nJUMP in pool\nRETURN to clearing""",
    SceneProp.OPTIONS: {
        'JUMP': Scenes.POND_JUMP,
        'RETURN': Scenes.CLEARING
    }
}

POND_JUMP = {
    SceneProp.SCENE_MSG: """You ready yourself for a moment befor leaping with a
heave towards the center of the pond. The world crashes around you as you
plunge into the water. Once you regain your bearings you look around you.
Below you see the glint of something shimmering, to your right a bit you
see a small opening to a cave. """,
    SceneProp.CHOICE_MSG: """What do you want to do?\nSwim DOWN\nSwim towards CAVE\nGet OUT""",
    SceneProp.OPTIONS: {
        'DOWN': Scenes.POND_DOWN,
        'CAVE': Scenes.POND_CAVE_3,
        'OUT': Scenes.POND_OUT
    }
}

POND_OUT = {
    SceneProp.SCENE_MSG: """You heave yourself out of the pond and stand on the bank dripping
with water.\nThe pond sits before you once again still.""",
    SceneProp.CHOICE_MSG: """What do you want to do?\nJUMP back into the pond\nRETURN to the center of the clearing""",
    SceneProp.OPTIONS: {
        'JUMP': Scenes.POND_JUMP,
        'RETURN': Scenes.CLEARING
    }
}

POND_DOWN = {
    SceneProp.SCENE_MSG: """As you swim downards, the glint persists and becomes clearer. As you
push aside a large pond fern you see a silver pendant lodged in the dirt.\nThe pendant seems to emit a light blue glow.""",
    SceneProp.CHOICE_MSG: """Do you grab the pendant or turn back?\nGRAB the pendant\nTurn BACK""",
    SceneProp.OPTIONS: {
        'GRAB': Scenes.GRAB_PENDANT,
        'BACK': Scenes.POND_BACK
    }
}

POND_BACK = {
    SceneProp.SCENE_MSG: """You float just below the ponds surface. Below you you see
a glint of silver. To your right you see a small cave opening.""",
    SceneProp.CHOICE_MSG: """What do yo want to do?\nSwim DOWN\nCheck out CAVE\nGet OUT""",
    SceneProp.OPTIONS: {
        'DOWN': Scenes.POND_DOWN,
        'CAVE': Scenes.POND_CAVE_3,
        'OUT': Scenes.POND_OUT
    }
}

GRAB_PENDANT = {
    SceneProp.SCENE_MSG: """You reach out for the pendant, the pressure in the water around
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
    # return Scenes.POND_OUT
}

POND_CAVE_1 = {
    SceneProp.SCENE_MSG: """pond cave 1""",
    SceneProp.CHOICE_MSG: """2""",
    SceneProp.OPTIONS: {
        '2': Scenes.POND_CAVE_2,
    }
}

POND_CAVE_2 = {
    SceneProp.SCENE_MSG: """pond cave 2""",
    SceneProp.CHOICE_MSG: """1\n3\n7""",
    SceneProp.OPTIONS: {
        '1': Scenes.POND_CAVE_1,
        '3': Scenes.POND_CAVE_3,
        '7': Scenes.POND_CAVE_7,

    }
}

POND_CAVE_3 ={
    SceneProp.SCENE_MSG: """You swim from the main area of the pond into the cave.
As you enter the cave, the water around you becomes colder. Polyps grow on
the walls and seem to reach out towards you. The walls move away from you
as you enter a larger underwater room, three passages lead out of the room
presumaby into other caverns. You notice an air pocket at the top of the
chamber. In desparation you swim towards the surface. You burst through the
surface and smack your head on the low ceiling. There is a space of about a
foot between the water and the roof of the cave. You look up at the rock
above you in annoyance, with surprise you notice a circle scratched harshly
into it. The mark looks far from natural, and looks more like a zero
sratched in by another being.""",
    SceneProp.CHOICE_MSG: """What would you like to do?\nBACK\n2\n4""",
    SceneProp.OPTIONS: {
        'BACK': Scenes.POND_BACK,
        '2': Scenes.POND_CAVE_2,
        '4': Scenes.POND_CAVE_4,
    }
}

POND_CAVE_4 = {
    SceneProp.SCENE_MSG: """pond cave 4""",
    SceneProp.CHOICE_MSG: """3\n5\n9""",
    SceneProp.OPTIONS: {
        '3': Scenes.POND_CAVE_3,
        '5': Scenes.POND_CAVE_5,
        '9': Scenes.POND_CAVE_9,
    }
}

POND_CAVE_5 = {
    SceneProp.SCENE_MSG: """pond cave 5""",
    SceneProp.CHOICE_MSG: """4""",
    SceneProp.OPTIONS: {
        '4': Scenes.POND_CAVE_4,
    }
}

POND_CAVE_6 = {
    SceneProp.SCENE_MSG: """pond cave 6""",
    SceneProp.CHOICE_MSG: """7\n11""",
    SceneProp.OPTIONS: {
        '7': Scenes.POND_CAVE_7,
        '11': Scenes.POND_CAVE_11,
    }
}

POND_CAVE_7 ={
    SceneProp.SCENE_MSG: """pond cave 7""",
    SceneProp.CHOICE_MSG: """2\n6\n8""",
    SceneProp.OPTIONS: {
        '2': Scenes.POND_CAVE_2,
        '6': Scenes.POND_CAVE_6,
        '8': Scenes.POND_CAVE_8,
    }
}

POND_CAVE_8 = {
    SceneProp.SCENE_MSG: """pond cave 8""",
    SceneProp.CHOICE_MSG: """7\n13""",
    SceneProp.OPTIONS: {
        '7': Scenes.POND_CAVE_7,
        '13': Scenes.POND_CAVE_13,
    }
}

POND_CAVE_9 = {
    SceneProp.SCENE_MSG: """pond cave 9""",
    SceneProp.CHOICE_MSG: """4\n10""",
    SceneProp.OPTIONS: {
        '4': Scenes.POND_CAVE_4,
        '10': Scenes.POND_CAVE_10,
    }
}

POND_CAVE_10 = {
    SceneProp.SCENE_MSG: """pond cave 10""",
    SceneProp.CHOICE_MSG: """9\n15""",
    SceneProp.OPTIONS: {
        '9': Scenes.POND_CAVE_9,
        '15': Scenes.POND_CAVE_15,
    }
}

POND_CAVE_11 = {
    SceneProp.SCENE_MSG: """pond cave 11""",
    SceneProp.CHOICE_MSG: """6""",
    SceneProp.OPTIONS: {
        '6': Scenes.POND_CAVE_6,
    }
}

POND_CAVE_12 = {
    SceneProp.SCENE_MSG: """pond cave 12""",
    SceneProp.CHOICE_MSG: """13\n17""",
    SceneProp.OPTIONS: {
        '13': Scenes.POND_CAVE_13,
        '17': Scenes.POND_CAVE_17,
    }
}

POND_CAVE_13 = {
    SceneProp.SCENE_MSG: """pond cave 13""",
    SceneProp.CHOICE_MSG: """8\n12\n14""",
    SceneProp.OPTIONS: {
        '8': Scenes.POND_CAVE_8,
        '12': Scenes.POND_CAVE_12,
        '14': Scenes.POND_CAVE_14,
    }
}

POND_CAVE_14 = {
    SceneProp.SCENE_MSG: """pond cave 14""",
    SceneProp.CHOICE_MSG: """enter any key to see options""",
    SceneProp.OPTIONS: {
        '13': Scenes.POND_CAVE_13,
        '15': Scenes.POND_CAVE_15,
        '19': Scenes.POND_CAVE_19,
    }
}

POND_CAVE_15 = {
    SceneProp.SCENE_MSG: """pond cave 15""",
    SceneProp.CHOICE_MSG: """10\n14""",
    SceneProp.OPTIONS: {
        '10': Scenes.POND_CAVE_10,
        '14': Scenes.POND_CAVE_14,
    }
}

POND_CAVE_16 = {
    SceneProp.SCENE_MSG: """pond cave 16""",
    SceneProp.CHOICE_MSG: """ENTERANCE\n17""",
    SceneProp.OPTIONS: {
        'ENTRANCE': Scenes.FOREST_CAVE_ENTRANCE_OUT,
        '17': Scenes.POND_CAVE_17,
    }
}

POND_CAVE_17 = {
    SceneProp.SCENE_MSG: """pond cave 17""",
    SceneProp.CHOICE_MSG: """12\n16\n18""",
    SceneProp.OPTIONS: {
        '12': Scenes.POND_CAVE_12,
        '16': Scenes.POND_CAVE_16,
        '18': Scenes.POND_CAVE_18,
    }
}

POND_CAVE_18 = {
    SceneProp.SCENE_MSG: """pond cave 18""",
    SceneProp.CHOICE_MSG: """17""",
    SceneProp.OPTIONS: {
        '17': Scenes.POND_CAVE_17,
    }
}

POND_CAVE_19 = {
    SceneProp.SCENE_MSG: """pond cave 19""",
    SceneProp.CHOICE_MSG: """14\n20""",
    SceneProp.OPTIONS: {
        '14': Scenes.POND_CAVE_14,
        '20': Scenes.POND_CAVE_20,
    }
}

POND_CAVE_20 = {
    SceneProp.SCENE_MSG: """pond cave 20""",
    SceneProp.CHOICE_MSG: """ENTERANCE\n19""",
    SceneProp.OPTIONS: {
        'ENTRANCE': Scenes.MOUNTAIN_CAVE_ENTRANCE,
        '19': Scenes.POND_CAVE_19,

    }
}

ENTER_FOREST = {
    SceneProp.SCENE_MSG: """You leave the open clearing and enter the dense forest.
The treetops block out the sun and the air becomes noticably cooler. You
wander a bit, keeping the glow of the clearing within eyesight behind you.
You notice a couple plants that might be edible, but you decide not to
risk it. A ways in fron of you, you notice a path worn lightly into the
grass by regular use. Behind you, the glow of the clearing was diminishing,
barely in view. """,
    SceneProp.CHOICE_MSG: """What would you like to do?\nRETURN to the clearing.\nWalk towards the PATH.""",
    SceneProp.OPTIONS: {
        'RETURN': Scenes.CLEARING,
        'PATH': Scenes.FOREST_PATH
    }
}

FOR_PATH = {
    SceneProp.SCENE_MSG: """Leaving the clearing behind, you walk towards the path
and follow it deeper into the forest. The forest grows more and more dense,
blocking out the sun. As the forest around you becomes darker, you notice a
dull glow at the far end of the path. The glow slowly becomes brighter as
you walk towards it. Continuing down the path, you become increasingly
aware of movement in the dark off to either side. The hair on your neck
stands on end as you realise that you are surrounded by beings in the dark.
They begin to chatter amonst themselves, first as a murmer barely audible,
but growing steadily.

The chatter quiets as you approach the end of the path.
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
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.LIGHT_VILLAGE,
    }
}

LIGHT_VILLAGE_1 = {
    SceneProp.SCENE_MSG: """Hesitantly you walk into the clearing and follow Gladion
towards the center of the village. Others join you and trail behind,
watching you curiously. 'Go, be cleansed of outside impurities, I will see
you when you are ready for tonights festivities'. Somewhat statrlinglly,
four of the villagers appear by your side. They guide you to one of the
houses, next to ths house you see a garden with various fruits and
vegetables. They seem to be organized in a series of concentric rings,
rather than that rows to which you are familiar. Amongst the garden around
the middle are a number of shrubs with large red berries.

Inside the hut is a low wide metal basin of warm water
and some boxes of nice smelling powders. Climbing into the basin, you feel
the warm water wash away your stress and the grime that had built up on
your skin. It occurs to you that this is the first time since you awoke in
the clearing that you have had a moment of pause. Why are you here? How did
you get here? In a panic it dawned on you, this might be it. You might be
stuck here for good.""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.LIGHT_VILLAGE_2,
    }
}

LIGHT_VILLAGE_2 = {
    SceneProp.SCENE_MSG: """As you bask in the water with your eyes closed, you hear
some movement behind you. Clumsily in the water, you turn to see whos
there. One of the villagers is watching you from accross the room, a
curious look on their face. After a moment of eye contact they smile kindly
and speak. 'Do you not wish to use our cleansing powders?' They gesture to
the boxes of powder next to the basin. You realize that you hadnt thought
of using the powders, or at least had been intimidated in your ingnorance
of their purpose.

You give them a sheepish grimmace, attempting to hide your
body in the shallow basin. 'I wasnt sure how to use them, or what they
were and didnt want to risk it.' They smile as they walk to the boxes and
pull out a ladle, stooping they scoop some of the powder out of one of the
boxes and walk toward you. In a wide arc they toss the powder into the
basin and it immediately begins to fizz and foam. 'Now rub the foam on your
skin, it will wash away your impurities.' As you begin to do so, the
villager walks to the far side of the room and sits on the floor.""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.LIGHT_VILLAGE_3,
    }
}

LIGHT_VILLAGE_3 = {
    SceneProp.SCENE_MSG: """'It really is quite fortuitous that you arrived today of
all days'. 'She the Seer spoke of the arrival of one from beyond. I couldnt
dream of doubting her word, but it seemed too wonderous to be true'. You
look at them from over the rim of the basin, 'Who is the seer? She knew I
was coming?' The villager smiled snarkly, 'Well she didnt know you were
comming, but that someone was. Or something at least.' 'Is she like a
psychic or something?' You bask in the warm water, letting yourself get
soggy.

'She the Seer is the counterpart to Gladion, as he is to her.'
Raising from the floor they grab a folded cloth from a shelf and hand it to
you. 'Together they represent the all, male to female, tangible and
formless, here to the beyond and all that is between.' The villager's eyes
glaze over while saying this, as if reverting to somewhere deep in their
conciousness. Returning to the present, they look at you and smile. 'You'll
meet her later probably, during the ceremony.'

Once you step out of the basin you dry youself off,
the villager politely turns their back, though for some reason you feel at
ease in their presence. They hand you some clothes and sandles, look
you over and smile, 'You really are quite similar to us though you
come from so far.' You detect a playfulness in their voice as they drift
towards the door. 'Tis a shame, maybe in another life perhaps.' In the
doorway they turn on their heel and face you. 'Ill see you in a bit, come
outside when you are done.' You call to them as they turn to leave, 'Wait,
what's your name?' They turn to you and smile, looking you over again.""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.CEREMONY_OF_LIGHT,
    }
}


CEREMONY_OF_LIGHT = {
    SceneProp.SCENE_MSG: """You sit on the ground on the center of the village with
the others, the excitement in the air sizzles around you. At the middle of
the village center sits a roaring fire, its warmth bathes the village and
keeps the evening chill at bay. The villagers chatter to eachother in an
unfamiliar language, passing bowls of food and drink to one another and
laughing. You gladly take the food and try it gratefully, it has been a
long time since you had eaten last. The chatter quiets as Gladion steps
gracefully onto the stone platform next to the fire, he is garbed in red
and gold. The last of the chatter dies as he raises his hands.

'People of the light, we are joined this ceremony of the cycles
by a being from beyond our forest.' 'It is for his benefit that I speak in
uncommon tounge', there is chatter of recognition amonst the crowd, many
eyes land on you. 'It is as She the Seer predicted, one from beyond shall
join the people of the light for the Celebration of Cycles!!' The crowd
cheers, and as you look around you notice a tall beautiful woman walk from
the back of the crowd towards the front. She is wearing robes of white and
silver, and walkes with an alien grace.""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.CEREMONY_OF_LIGHT_2,
    }
}

CEREMONY_OF_LIGHT_2 = {
    SceneProp.SCENE_MSG: """The crowds cheering grows as the woman reaches the small stage
and takes a seat on the intricately carved chair next to Gladion's.
'Welcome my love, my other half, two as one as whole is one!' The crowd
chantes after Gladion, 'Two as one whole as one!' The woman raises her hand
and waves at the crowd calmly, a serene smile on her face. Gladion chuckles
lightly and waves at the small village to quiet.

'Here again after another seasonal cycle. It is so good to see
you all again.' He stands with his hands held held wide above his head.
'Time has passed us by as it does, and there have been times both bad and
good'. 'The rise and fall of tensions within and without has affected us
all and left us more.' 'We grow as we watch ourselves struggle through
life, learning as we do.' But the struggle leaves scars and sores that sit
deep down and ache and fester.""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.LIGHT_VILLAGE_3,
    }
}

CEREMONY_OF_LIGHT_3 = {
    SceneProp.SCENE_MSG: """The crowd around you has become deathly quiet, their
excitement has gone from bubbling chatter to brittle tension. 'These wounds
are too much to bear, and blind us from truth. Blind us from the light!'.
Gladion scans the crowd, shifting from eye to eye. 'And so the Celebration
of the Cycles cleanses us.' He raises his face to the sky and stares at the
sun, eyes wide. 'Through it we are cleaned of the sores we have gained,
through ones suffering we become pure!' You look around nervously, the
crowd has regained their vigor. They begin to fidget and chatter with
fervor.

'And this Cycle of Cycles which has been particularly hard on us,
the light has brought us a special gift as offering.' The hair on your neck
sparks and raises sharply. You look around you, the village is looking at
you hungrily. You look up to Gladion and lock eyes with him. He holds your
gaze intensely, his peaceful smile curling at the corners. 'Thank you for
embodying our passage to purity and acting as a vessel of the light. I hope
you suffer beautifully.'""",
    SceneProp.CHOICE_MSG: "CONTINUE",
    SceneProp.OPTIONS: {
        'CONTINUE': Scenes.COL_ENCOUNTER,
    }
}

COL_ENCOUNTER = {
    SceneProp.SCENE_MSG: """You are being surrounded by the members of the village. They close
in upon you with hungry eyes. As they close in you notice a break in the
crowd to your left. You duck and run through, pushing their hands aside.
You are now on the outskirts of the crowd, your only options for escape are
to right or to the left. """,
    SceneProp.CHOICE_MSG: """Which would you like to do?\nLEFT run to the left\nRIGHT run to the right\nBACKWOODS for now""",
    SceneProp.OPTIONS: {
        'BACKWOODS': Scenes.BACKWOODS,
    }
}
    
BACKWOODS = { 
    SceneProp.SCENE_MSG: """Backwoods area\ngoes to puzzle area, clearing with cave entrance,
forest entrance.""",
    SceneProp.CHOICE_MSG: """Where to go?\nto PUZZLE\nto CAVE entrance\nto forest ENTRANCE""",
    SceneProp.OPTIONS: {
        'PUZZLE': Scenes.FOREST_PUZZLE,
        'CAVE': Scenes.FOREST_CAVE_CLEARING_IN,
        'ENTRANCE': Scenes.ENTER_FOREST
    }
}

FOREST_CAVE_CLEARING_IN = { 
    SceneProp.SCENE_MSG: """You enter a small clearing with a gnalred tree against a large
rock. As you approach the tree you see a gap between the roots and the
rock, it seems to extend under the rock and from a certatin angle it almost
looks like the opening widenes further down.""",
    SceneProp.CHOICE_MSG: """Do you want to go down?\ngo down into the HOLE\nGo BACK the way you came""",
    SceneProp.OPTIONS: {
        'BACK': Scenes.BACKWOODS,
        'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
    }
}

FOREST_CAVE_CLEARING_OUT = { 
    SceneProp.SCENE_MSG: """You crawl out of the tight hole, using roots to pull yourself up. You are in a clearing. """,
    SceneProp.CHOICE_MSG: """Where to go?\nGo into forest FOREST\nGo back into HOLE""",
    SceneProp.OPTIONS: {
        'FOREST': Scenes.BACKWOODS,
        'HOLE': Scenes.FOREST_CAVE_ENTRANCE_IN,
    }
}

FOREST_CAVE_ENTERANCE_IN = { 
    SceneProp.SCENE_MSG: """Going feet first you lower yourself into the opening.
Using the roots of the tree you lower yourself into an underground chamber.
Light peeks in from cracks in the rock and the hole you just climbed
through. The light reflects off of crystals on the floor and walls,
shimmering slits cut accross one another and provide a dim glow. The sharp
refractions of the crystals are sofened by a dim swirling wash. You notice
a wetness to the echo of the chamber and move deeper in. In the center is a
round pool that seems to continue down forever. On closer inspection you
find that the walls of the pool end afer about 10 feet and give way to open
water. In the dim light of the cave you cant see much.""",
    SceneProp.CHOICE_MSG: """What would you like to do?\nJUMP in the pool\ngo BACK out to the clearing""",
    SceneProp.OPTIONS: {
        'JUMP': Scenes.POND_CAVE_20,
        'BACK': Scenes.FOREST_CAVE_CLEARING_OUT
    }
}

FOREST_CAVE_ENTERANCE_OUT = { 
    SceneProp.SCENE_MSG: """Pull yourself out of pool.\ncrystal cavern\nPool behind you, hole
that lights coming in through""",
    SceneProp.CHOICE_MSG: """What would you like to do?\nJUMP in the pool\nclimb out of the HOLE""",
    SceneProp.OPTIONS: {
        'JUMP': Scenes.POND_CAVE_20,
        'HOLE': Scenes.FOREST_CAVE_CLEARING_OUT
    }
}

FOREST_PUZZLE = { 
    SceneProp.SCENE_MSG: """As you travel through the dark woods you notice the sun beginning
to break through the trees. Looking ahead you notice the path starting
slope upwards. As you follow it upwards you find yourself on the middle of
a bridge. Around you is what looks like a square arrangement of ruins. The
bridge ahead continues downward again until it levels with the ground.""",
    SceneProp.CHOICE_MSG: """Where to go?\ngo back to BACKWOODS\ncontinue to PUZZLE""",
    SceneProp.OPTIONS: {
        'BACKWOODS': Scenes.BACKWOODS,
        'PUZZLE': Scenes.FOREST_PUZZLE_CENTER
    }
}

MOUNTAIN_PATH_1 = { 
    SceneProp.SCENE_MSG: """You walk along a path that extends from the clearing you woke up in
towards the base of the mountain. The path is bordered on both side by rough overgrowth.""",
    SceneProp.CHOICE_MSG: """Where to go?\ntowards CLEARING\nto mountian PATH""",
    SceneProp.OPTIONS: {
        'CLEARING': Scenes.CLEARING,
        'PATH': Scenes.MOUNTAIN_PATH_2,
    }
}

MOUNTAIN_PATH_2 = {
    SceneProp.SCENE_MSG: """You find yourself on a path that connects the mountain path and the base
of the mountain""",
    SceneProp.CHOICE_MSG: """where to go?\ngo to mountain PATH\ngo to BASE of the mountain""",
    SceneProp.OPTIONS: {
        'PATH': Scenes.MOUNTAIN_PATH,
        'BASE': Scenes.MOUNTAIN_BASE,
    }
}

MOUNTAIN_BASE = { 
    SceneProp.SCENE_MSG: """Base of the mountain\nSome people here to talk to\nmaybe sell some stuff\nalso connects to forest mountain path""",
    SceneProp.CHOICE_MSG: """where to go?\nBACK to mountain path\nmountain ENTRANCE\nforest mountain path""",
    SceneProp.OPTIONS: {
        'BACK': Scenes.MOUNTAIN_PATH_2,
        'ENTRANCE': Scenes.MOUNTAIN_ENTRANCE,
        'FOREST': Scenes.FOREST_MOUTAIN_PATH
    }
}

MOUNTAIN_ENTERANCE = {
    """Mountain entrance\nconnects mountain base to m_LVL1_R1\nencounter here""",
    """where go?\nmountain BASE\nto LVL1""",
    {
        'BASE': Scenes.MOUNTAIN_BASE,
        'LVL1': Scenes.M_LVL1_R1
    }
}

M_LVL1_R1 = {
    """first room on the first floor\ncurrently connects to LVL1Stairs through mountain cave entrance\nalso connects to mountain entrance""",
    """where?\nmountain ENTRANCE\nto MCAVE""",
    {
        'ENTRANCE': Scenes.MOUNTAIN_ENTRANCE,
        'MCAVE': Scenes.MOUNTAIN_CAVE_ENTRANCE
    }
}

MOUNTAIN_CAVE_ENTRANCE = {
    """Mountain cave entrance\nmountain entrance to underwater cave\nalso connects LVL1 R1 and LVL1 Stairs""",
    """where?\nto LVL1\nto CAVE\nto USTAIRS lvl1 stairs""",
    {
        'LVL1': Scenes.M_LVL1_R1,
        'CAVE': Scenes.POND_CAVE_16,
        'USTAIRS': Scenes.M_LVL1_STAIRS
    }
}

M_LVL1_STAIRS = {
    """lvl1 stairs\nconnects lvl1 and lvl2\ncurrently goes from mountain cave entrance to LVL2 R1""",
    """where?\nto MCAVE\nto LVL2""",
    {
        'MCAVE': Scenes.MOUNTAIN_CAVE_ENTRANCE,
        'LVL2': Scenes.M_LVL2_R1
    }
}

M_LVL2_R1 = { 
    """mountain LVL 2\nconnects to LVL1STAIRS and LVL2Stairs"""
    """where?\ngo USTAIRS staircase to lvl3\ngo DSTAIRS staircase to lvl1"""
    {
        'DSTAIRS': Scenes.M_LVL1_STAIRS,
        'USTAIRS': Scenes.M_LVL2_STAIRS
    }
}

M_LVL2_STAIRS = {
    """mountain lvl2 stairs to lvl 3\nconnects lvl2 to lvl3"""
    """where?\nto LVL2\nto LVL3"""
    {
        'LVL2': Scenes.M_LVL2_R1,
        'LVL3': Scenes.M_LVL3_R1
    }
}

M_LVL3_R1 = {
    """mountain lvl 3\nconnects to lvl2 stairs and lvl3stairs to boss"""
    """Where?\nto DSTAIRS staircase to lvl2\nto USTAIRS staircase to lvl3"""
    {
        'DSTAIRS': Scenes.M_LVL2_STAIRS,
        'USTAIRS': Scenes.M_LVL3_STAIRS
    }
}

M_LVL3_STAIRS = { 
    """mountain lvl 3 stairs\nconnect lvl3 with boss area"""
    """where?\nto LVL3\nUP to boss area"""
    {
        'LVL3': Scenes.M_LVL3_R1,
        'UP': Scenes.BOSS_AREA
    }
}

BOSS_AREA = { 
    """Boss area\nwhere final encounter will take place\ngoes only back to LVL3 stairs"""
    """where?\nBACK down stairs"""
    {
        'BACK': Scenes.M_LVL3_STAIRS
    }
}
