# run game with gui

from state import State
from rich_pixels import Pixels
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal, Vertical, Grid, Center
from textual.widgets import Static, Footer, Header, Markdown, Rule, Button, Tabs, Tab

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
    state = (State())

    CSS_PATH = "adv_css.tcss"

    def compose(self):
        yield Header()
        with Horizontal(id="top-horz"):
            with Vertical(id="lvert"):
                with Container():
                    with Horizontal(id="scene-horz"):
                        yield Markdown(cc, id="md-tl")
                        with Vertical():
                            with Static(id="simg-cont"):
                                yield SceneRender(id="scene-img")
                            yield Markdown(stats, id="ply-stat")
                    yield Rule()
                    with Horizontal(id="opt-hor"):
                        yield Markdown(bb, id="md-bl")
                        with Container(id="button-grid"):
                            yield Button()
                            yield Button()
                            yield Button()
                            yield Button()
            with Vertical(id="rvert"):
                with Container():
                    # yield Markdown(map_img, id="md-tr")
                    with Static(id="map-cont"):
                        yield MapRender(id="map-img")
                        # yield Static("Hello World", id="map-img")
                    yield Rule()
                    # yield Markdown(id="md-br")
                    yield Tabs(TABS[0], TABS[1], TABS[2], TABS[3])
                    yield Markdown("", id="tab-content")
        yield Footer()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        tab_content = self.query_one("#tab-content")
        tab_idx = TABS.index(f'{event.tab.label}')
        tab_content.update(TAB_CONT[tab_idx])

class MapRender(Static):

    def on_mount(self) -> None:
        map_img = Pixels.from_image_path("map32.png")
        self.update(map_img)

class SceneRender(Static):

    def on_mount(self) -> None:
        map_img = Pixels.from_image_path("profile32.png")
        self.update(map_img)

if __name__ == "__main__":
    app = AdventureGui()
    app.run()
