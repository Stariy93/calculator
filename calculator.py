from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

Window.size = (300, 500)
Window.clearcolor = (100/255, 50/255, 200/255, 1)
Window.title = ('Calculator')

class MyApp(App):
    def num():
        
        
    def build(self):
        calc = BoxLayout(orientation = 'vertical')
        board = Label(text = '')
        calc.add_widget(board)
        keypad = GridLayout(rows = 3, cols = 3)
        for i in range(1, 10):
            btn = Button(text = f"{i}")
            keypad.add_widget(btn)
        calc.add_widget(keypad)
        return calc
        
        

if __name__ == '__main__':
    MyApp().run()