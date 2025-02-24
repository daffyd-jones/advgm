# run game with gui
from enums import Scenes, SceneProp, InvItem
from textual.reactive import reactive
from state import State
from rich_pixels import Pixels
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal, Vertical, Grid, Center
from textual.widgets import Static, Footer, Header, Markdown, Rule, Button, Tabs, Tab, ListView, ListItem, ContentSwitcher

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
    "Notes",
    "Awards",
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


 
class AdventureGui(App):
    state = reactive(State())
    current_scene = reactive(Scenes.BEGINNING)
    scene_content = reactive({})
    
    CSS_PATH = "adv_css.tcss"

    def compose(self):
        # yield Header()
        with ContentSwitcher(initial="menu-screen"):
            yield GameScreen(id="game-screen")
            with Center(id="menu-screen"):
                yield Vertical(
                    # Markdown(id='mdbug'),
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
        self.set_stats()


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

    def set_scene_img(self) -> None:
        
        scene_render = self.query_one('#scene-img')
        
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case 'menu-new':
                self.query_one(ContentSwitcher).current = "game-screen"
            case 'btn-a' | 'btn-b' | 'btn-c' | 'btn-d':
                label = self.query_one(f'#{event.button.id}').label
                self.scene_content = self.state.play_turn(self.scene_content[SceneProp.OPTIONS][f'{label}'])
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
                self.set_stats()
  

class GameScreen(Static):

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
                    yield Markdown("", id="tab-content")

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        tab_content = self.query_one("#tab-content")
        tab_idx = TABS.index(f'{event.tab.label}')
        tab_content.update(TAB_CONT[tab_idx])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        pass
  
class MapRender(Static):

    def on_mount(self) -> None:
        map_img = Pixels.from_image_path("imgs/maps/map_clearing_32.png")
        self.update(map_img)

class SceneRender(Static):

    def on_mount(self) -> None:
        map_img = Pixels.from_image_path("imgs/scenes/clearing_32.png")
        self.update(map_img)











if __name__ == "__main__":
    app = AdventureGui()
    app.run()
