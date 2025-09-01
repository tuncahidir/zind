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
        if touch.grab_current is self:

            if self._daire_down and self.daire.collide_point(*touch.pos):
                self.daire.halka = not self.daire.halka
            self._daire_down = False
            return True
        
        self.right_push = False
        self.left_push = False
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
    HALKA_KALINLIK = 12.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._ell = None
        self._line = None
        self._init_done = False

        with self.canvas:
            self._col_solid = Color(1, 0, 0, 1)
            self._ell = Ellipse(pos=(0,0), size = (0,0))

            self._col_ring = Color(1, 0, 0, 1)
            self._line = Line(circle=(0, 0, 0), width=0)

        self._init_done = True    
    
        self.bind(pos = self.redraw, size = self.redraw, yaricap = self.redraw, halka = self.redraw)
        Clock.schedule_once(self.redraw, 0)

    def redraw(self, *args):

        if not self._init_done or self._ell is None or self._line is None:
            return

        r = self.yaricap
        cx = self.center_x
        cy = self.center_y

        if self.halka:

            self._ell.size = (0, 0)
            self._line.circle = (cx, cy, r)
            self._line.width = self.HALKA_KALINLIK
        else:
            self._ell.pos = (cx - r, cy - r)
            self._ell.size = (2*r, 2*r)
            #self._line.width = 0



