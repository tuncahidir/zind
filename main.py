from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from gameMode import gameMod

class AnaMenu(FloatLayout):
    def __init__(self, **kwargs):
        self.app_ref = kwargs.pop('app_ref', None)
        super().__init__(**kwargs)
        self.game_start()

    def game_start(self):
        self.game = gameMod()
        self.add_widget(self.game)

class ZindV2(App):
    def build(self):
        return super().build()

if __name__ == '__main__':
    ZindV2().run()    