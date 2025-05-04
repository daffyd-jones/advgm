# run game with gui
from enums import Scenes, SceneProp, InvItem
from textual.reactive import reactive
from state import State
from rich_pixels import Pixels
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal, Vertical, Grid, Center
from textual.widgets import Static, Footer, Header, Markdown, Rule, Button, Tabs, TabbedContent, ListView, ListItem, ContentSwitcher, TabPane

aa = '''
;lksadjf;oio weoifhwoihekl ahekjh asd asd effef  fsd.
asdf a sdffaw efawewaf wf weffweffwaefaweeffwaef..waef
awef  waef.weff wefffwef .fawef..wea .fa
.awf.waef. w.fe wffeeeefwaaefg er  ggregg erggas.
;lksadjf;oio weoifhwoihekl ahekjh asd asd effef  fsd.
asdf a sdffaw efawewaf wf weffweffwaefaweeffwaef..waef
awef  waef.weff wefffwef .fawef..wea .fa
.awf.waef. w.fe wffeeeefwaaefg er  ggregg erggas.
;lksadjf;oio weoifhwoihekl ahekjh asd asd effef  fsd.
asdf a sdffaw efawewaf wf weffweffwaefaweeffwaef..waef
awef  waef.weff wefffwef .fawef..wea .fa
.awf.waef. w.fe wffeeeefwaaefg er  ggregg erggas.
'''

bb = '''
.awf.waef. w.fe wffeeeefwaaefg er  ggregg erggas.

;lksadjf;oio weoifhwoihekl ahekjh asd asd effef  fsd.

asdf a sdffaw efawewaf wf weffweffwaefaweeffwaef..waef

asdf a sdffaw efawewaf wf weffweffwaefaweeffwaef..waef
'''

cc = """You awake feeling groggy and sore. Opening your eyes,
you look around. You appear to be in a clearing surrounded by tall
evergreens. Twenty yards to your right is a small pond, still and
surrounded by small ferns. Behind you, and beyond the forest towers a
mountain, cold and grey against the bright sky. It cast the forest and the
clearing below in shadow."""

stats = """
|Stat|Amt|
|---|---|
|Health|100|
|Money|40|
|Attack|10|
|Damage|7|
|Defence|10|
"""

TABS = [
    "Inventory",
    "Equipment",
    "Notes",
    "Experience",
]

TAB_CONT = [
    """
## Item

Description stuff here Description stuff here
this is a description about an titem
- price: 8
- health: 30

| | | | |
|---|---|---|---|
|Item|Item|Item|Item|        
|Item|Item|Item|Item|        
|Item|Item|Item|Item|        
|Item|Item|Item|Item|        
|Item|Item|Item|Item|        
|Item|Item|Item|Item|        
    """,
    """
## A thing that happened

You saw a thing or talked to someone

----

You talked to a person or saw a thing and now know more about stuff.
Or maybe you just found another mystery with more questions.

- This is a general summary
- another relevant fact
- maybe a hint

    """,
    """
## Award Item

Got this for doing a thing, or finishing a part of the game.
It could be an item that you take from a person, or a thing that is given to you.

| | | | |
|---|---|---|---|
|Award|Award|Award|Award|        
|Award|Award|Award|Award|        
|Award|Award|Award|Award|        
|Award|Award|Award|Award|        
|Award|Award|Award|Award|        
|Award|Award|Award|Award|
     """,
    """

| | | | |
|---|---|---|---|
|Award||Award|Award|        
|Award||Award|Award|        
|Award||Award|Award|        
|Award||Award|Award|        
|Award||Award|Award|        
|Award||Award|Award|
    """,
]

item_map = {
    "Health_Potion": InvItem.HEALTH_POTION,
    "Strength_Potion": InvItem.STRENGTH_POTION,
    "Agility_Potion": InvItem.AGILITY_POTION,
    "Defence_Potion": InvItem.DEFENCE_POTION,
    "Bread_Hunk": InvItem.BREAD_HUNK,
}


 
class AdventureGui(App):
    state = reactive(State())
    current_scene = reactive(Scenes.BEGINNING)
    scene_content = reactive({})
    
    CSS_PATH = "adv_css.tcss"

    def compose(self):
        # yield Header()
        with ContentSwitcher(initial="menu-screen", id="main-switch"):
            yield GameScreen(self.state.get_inventory(), id="game-screen")
            with Center(id="menu-screen"):
                yield Vertical(
                    Button("New Game", id="menu-new", classes="menu-btn"),
                    Button("Load Game", id="menu-load", classes="menu-btn"),
                    Button("Save Game", id="menu-save", classes="menu-btn"),
                    Button("Exit Game", id="menu-exit", classes="menu-btn"),
                    id="menu-list"
                )
        # yield Footer()

    def on_mount(self) -> None:
        start_turn = self.state.play_turn(self.current_scene)
        self.scene_content = start_turn
        self.set_scene_content()
        self.set_stats()
        self.set_scene_imgs()

    def set_scene_content(self) -> None:
        self.query_one('#md-tl').update(self.scene_content[SceneProp.SCENE_MSG])
        self.query_one('#md-bl').update(self.scene_content[SceneProp.CHOICE_MSG])
        opts = self.scene_content[SceneProp.OPTIONS]
        keys = list(opts.keys())
        kdiff = 4 - len(keys)
        pad = [" "] * kdiff
        fkeys = keys + pad
        self.query_one('#btn-a').label = fkeys[0]
        self.query_one('#btn-b').label = fkeys[1]
        self.query_one('#btn-c').label = fkeys[2]
        self.query_one('#btn-d').label = fkeys[3]
        


    def set_stats(self) -> None:
        stats = self.state.stats
        stat_str = f"""
|Stat|Amt|
|---|---|
|Health|{stats['hp']}|
|Money|{stats['money']}|
|Attack|{stats['attack']}|
|Damage|{stats['hit_rate']}|
|Defence|{stats['defence']}|
"""
        self.query_one('#ply-stat').update(stat_str)

    def set_scene_imgs(self) -> None:
        img_path = self.scene_content[SceneProp.SCENE_IMG]
        map_img = Pixels.from_image_path(img_path)
        self.query_one('#scene-img').update(map_img)
        img_path = self.scene_content[SceneProp.MAP_IMG]
        map_img = Pixels.from_image_path(img_path)
        self.query_one('#map-img').update(map_img)
        
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case 'menu-new':
                self.query_one('#main-switch').current = "game-screen"
            case 'btn-a' | 'btn-b' | 'btn-c' | 'btn-d':
                label = self.query_one(f'#{event.button.id}').label
                self.scene_content = self.state.play_turn(self.scene_content[SceneProp.OPTIONS][f'{label}'])
                self.set_scene_content()
                self.set_stats()
                self.set_scene_imgs()
            case x if 'inv-btn' in x:
                btn = event.button.label
                item = f'{btn.split(":")[0]}'
                info = self.state.inventory.get_info(item)
                self.query_one('#inv-md').update(info)
            case x if 'inv-use-btn' in x:
                use_id = event.button.id
                item = use_id.split("-")[3]
                self.query_one(Inventory).set_inventory(self.state.use_inv_item(item_map[item])) 
                self.set_stats()
              
                
class GameScreen(Static):

    def __init__(self, inventory, id):
        self.inventory = inventory
        super().__init__(id=id)


    def compose(self):
        with Horizontal(id="top-horz"):
            with Vertical(id="lvert"):
                with Container():
                    with Horizontal(id="scene-horz"):
                        yield Markdown(id="md-tl")
                        with Vertical():
                            with Static(id="simg-cont"):
                                yield SceneRender(id="scene-img")
                            yield Markdown(stats, id="ply-stat")
                    yield Rule()
                    with Horizontal(id="opt-hor"):
                        yield Markdown(id="md-bl")
                        with Container(id="button-grid"):
                            yield Button("a", classes="opt-btn", id="btn-a")
                            yield Button("b", classes="opt-btn", id="btn-b")
                            yield Button("c", classes="opt-btn", id="btn-c")
                            yield Button("d", classes="opt-btn", id="btn-d")
            with Vertical(id="rvert"):
                with Container():
                    with Static(id="map-cont"):
                        yield MapRender(id="map-img")
                    yield Rule()
                    yield Tabs(TABS[0], TABS[1], TABS[2], TABS[3])
                    with ContentSwitcher(initial="inv-wig", id="tab-switch"):
                        yield Inventory(id="inv-wig")
                        # yield Equiptment()
                        yield Notes(id="notes-wig")
                        yield Markdown("", id="tab-content")

    def on_mount(self):
        self.query_one(Inventory).set_inventory(self.inventory)

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        match f'{event.tab.label}':
            case 'Inventory':
                self.query_one("#tab-switch").current = 'inv-wig'
            case 'Notes':
                self.query_one("#tab-switch").current = 'notes-wig'
                # tab_idx = TABS.index(f'{event.tab.label}')
                # self.query_one("#tab-content").update(TAB_CONT[tab_idx])
            case 'Awards':
                self.query_one("#tab-switch").current = 'tab-content'
                tab_idx = TABS.index(f'{event.tab.label}')
                self.query_one("#tab-content").update(TAB_CONT[tab_idx])
            case 'Experience':
                self.query_one("#tab-switch").current = 'tab-content'
                tab_idx = TABS.index(f'{event.tab.label}')
                self.query_one("#tab-content").update(TAB_CONT[tab_idx])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        pass
  
class Inventory(Static):

    inventory = reactive([])
    
    def on_mount(self):
        pass

    def compose(self):
        yield Markdown(id="inv-md")
        yield ListView(id="inv-vert", initial_index=0)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        pass

    def set_inventory(self, inventory):
        self.inventory = inventory
         
        inv_list =  self.query_one("#inv-vert")
        inv_list.clear()
        for i, item in enumerate(self.inventory):
            id_str = f'inv-btn-{i + 1}'
            class_str = 'inv-btns'
            label = item.split(":")[0].split(" ")
            use_id_str = f'inv-use-btn-{label[0]}_{label[1]}'
            use_class_str = 'inv-use-btns'
            inv_list.append(ListItem(
                    Horizontal(
                        Button(item, id=id_str, classes=class_str),
                        Button('USE', id=use_id_str, classes=use_class_str),
                        id="inv-horiz"
                    ),
                )
            )
        #----i
        
        inv_md = self.query_one('#inv-md')
        if len(self.inventory) == 0:
            inv_md.update('# no items')
        elif inv_list.index == None:
            inv_md.update('# select item')


# class Equipment


NOTE_TABS = [
    "First Task",
    "Second Task",
    "Third Task",
]

NOTES = {
    "First Task": """
# Met a person 1

You met a person who told you a thing.

These are the main notes:
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 
""",
    "Second Task": """
# Met a person 2

You met a person who told you a thing.

These are the main notes:
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 

## This is a sub section

This is a description of an event.

These are more notes:
- This is another note
- This is another note
- This is another note
- This is another note
- This is another note
- This is another note

More text
""",
    "Third Task": """
# Met a person 3

You met a person who told you a thing.

These are the main notes:
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 
- This is a point of note 
""",
}

class Notes(Static):

    def compose(self):
        yield Tabs(NOTE_TABS[0], NOTE_TABS[1], NOTE_TABS[2])
        yield Markdown(NOTES[NOTE_TABS[0]], id="notes-md")


    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        self.query_one("#notes-md").update(NOTES[f'{event.tab.label}'])

class MapRender(Static):

    def on_mount(self) -> None:
        # map_img = Pixels.from_image_path("imgs/maps/map_clearing_32.png")
        # self.update(map_img)
        pass

class SceneRender(Static):

    def on_mount(self) -> None:
        # map_img = Pixels.from_image_path("imgs/scenes/clearing_32.png")
        # self.update(map_img)
        pass











if __name__ == "__main__":
    app = AdventureGui()
    app.run()
