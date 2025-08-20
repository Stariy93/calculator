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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = Label(text = '')
        self.keypad = GridLayout(rows = 3, cols = 3)
        self.num_list = []
        def press(instance):
            self.board.text += instance.text
        for i in range(1, 10):
            btn = Button(text = f"{i}")
            btn.bind(on_press=press)
            self.num_list.append(btn)
        for btn in self.num_list:
            self.keypad.add_widget(btn)


        
    def build(self):
        calc = BoxLayout(orientation = 'vertical')  
        calc.add_widget(self.board)
        
        calc.add_widget(self.keypad)
        return calc
        
        

if __name__ == '__main__':
    MyApp().run()