from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.graphics import Ellipse, Color
from kivy.clock import Clock
from kivy.properties import NumericProperty

class gameMod(Widget):
    yaricap = NumericProperty(50)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 1)
            self.circle = Ellipse()
        self.bind(center = self.redraw, size = self.redraw, yaricap = self.redraw)


    def redraw(self, *_):
        r = self.yaricap
        self.circle.pos = (self.center_x - r, self.center_y - r)
        self.circle.size = (2*r, 2*r)
