#trying this using kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (ListProperty, NumericProperty, ObjectProperty, StringProperty)
from kivy.utils import platform
from kivy.core.window import Window
import random



class Block(Widget):
    colour=ListProperty([0,1,1])


class intervalTraining(FloatLayout):
    blocks=ListProperty([])
    #player=ObjectProperty([])
    #ball=ObjectProperty([])

    def setup_blocks(self):
        print("A")
        self.blocks=[]
        for y_jump in range(6):
            print(y_jump)
            block=Block(pos_hint={'x':0.05,'y':0.55+0.09*y_jump})
            #block.colour=random.choice([(0.78,0.28,0),(0.28,0.63,0.28),(0.25,0.28,0.78)])
            self.add_widget(block)
            #self.blocks.append(block)










class intervalTrainingApp(App):
    def build(self):
        g=intervalTraining()
        g.setup_blocks()
        #if platform!='android':
            #Window.bind(on_key_down=g.player.on_key_down)
            #Window.bind(on_key_up=g.player.on_key_up)
        #g.reset()
        #Clock.schedule_once(g.start,0)
        return g

intervalTrainingApp().run()
