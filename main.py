from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from gameMode import gameMod

class AnaMenu(Screen):
    pass
    # def __init__(self, **kwargs):
    #     self.app_ref = kwargs.pop('app_ref', None)
    #     super().__init__(**kwargs)
    #     self.game_start()

    # def game_start(self):
    #     self.game = CircleWidget()
    #     self.add_widget(self.game)

class ZindV2(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AnaMenu(name = "menu"))
        sm.add_widget(gameMod(name = "oyun"))
        sm.current = "oyun"
        return sm

if __name__ == '__main__':
    ZindV2().run()    