from kivy.uix.relativelayout import RelativeLayout 
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.animation import Animation

class pencere4(RelativeLayout):
    bg_color = ObjectProperty([60/255,60/255,60/255,1])
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.arka_plan_anime, 5)
    def arka_plan_anime(self,*args):
        anim =Animation(bg_color=[60/255,60/255,60/255,1],t='in_quad',duration=2.5) + Animation(bg_color=[22/255,22/255,22/255,1],t='in_quad',duration=2.5)
        anim.start(self)