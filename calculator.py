from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (300, 500)
Window.clearcolor = (100/255, 50/255, 200/255, 1)
Window.title = ('Calculator')

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t = 1
        self.label = Label(text=str(self.t))


    def button_pressed(self, instance):
        self.t += 1
        self.label.text = str(self.t)
        
    def build(self):
        box = BoxLayout()
        button = Button(text = "+")
        button.bind(on_press = self.button_pressed)
        box.add_widget(self.label)
        box.add_widget(button)
        return box
        

if __name__ == '__main__':
    MyApp().run()