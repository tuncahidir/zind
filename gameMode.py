from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

from kivy.graphics import Ellipse, Color, Line, Rectangle
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty

BUYUME_HIZI  = 120.0
KUCULME_HIZI = 120.0
MIN_R        = 20.0
MAX_R        = 140.0


class gameMod(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.daire = CircleWidget(size_hint=(1,1))
        self.add_widget(self.daire)

        self.right_push = False
        self.left_push = False
        self._daire_down = False

        Clock.schedule_interval(self.update, 1/60)

    def fit(self, *args):
        self.daire.size = self.size
        self.daire.pos = self.pos
    
    def on_touch_down(self, touch):
        
        if self._is_on_circle(*touch.pos):
            self._daire_down = True
            return True
        
        if touch.x >= self.width /2:
            self.right_push = True
        else:
            self.left_push = True
        return True
    
    def on_touch_up(self, touch):
        self.right_push = False
        self.left_push = False

        if self._daire_down and self.daire.collide_point(*touch.pos):
          self.daire.halka = not self.daire.halka
        self._daire_down = False
        return True
    
    def update(self, dt):
        r = self.daire.yaricap
        if self.right_push:
            r += BUYUME_HIZI * dt
        if self.left_push:
            r -= KUCULME_HIZI * dt

        r = max(MIN_R, min(MAX_R, r))

        if r != self.daire.yaricap:
            self.daire.yaricap = r

    def _is_on_circle(self, x, y):
        dx = x - self.daire.center_x
        dy = y - self.daire.center_y
        return (dx*dx + dy*dy) <= (self.daire.yaricap * self.daire.yaricap)

       

class CircleWidget(Widget):
    yaricap = NumericProperty(50)
    halka = BooleanProperty(False)
    HALKA_KALINLIK = 8.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)
            self._shape = Ellipse(pos=(0,0), size = (0,0))
        self._mod = 'solid'
        self.bind(pos = self.redraw, size = self.redraw, yaricap = self.redraw, halka = self.redraw)

    def on_parent(self, *args):
        Clock.schedule_once(lambda dt: self.redraw(), 0)

    def redraw(self, *args):
        print("redraw r=", self.yaricap, "center=", self.center, "size=", self.size, "mod=", getattr(self, "_mod", None), "halka=", self.halka)
        r = self.yaricap
        cx, cy = self.center
        hedef_mod = 'ring' if self.halka else 'solid'

        if self._mod != hedef_mod:
            self.canvas.clear()
            from kivy.graphics import Color, Ellipse, Line
            Color(1,1,1,1)
            
            if  hedef_mod == 'ring':
                self._shape = Line(circle=(cx, cy, r), width=self.HALKA_KALINLIK)    
            else:
                self._shape = Ellipse(pos=(cx - r, cy - r), size=(2*r, 2*r))
            self._mod = hedef_mod
            return

        if self._mod == 'ring':
            self._shape.circle = (cx, cy, r)
        else:
            self._shape.pos = (cx - r, cy - r)
            self._shape.size = (2*r, 2*r)


