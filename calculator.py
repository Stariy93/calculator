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
        def equal_press(instance):
            self.board.text = str(eval(self.board.text))
        def signs_press(instance):
            if self.board.text and self.board.text[-1] not in ['+', '-', '=']:
                self.board.text += instance.text
        plas = Button(text = '+')
        plas.bind(on_press = signs_press)
        self.signs = BoxLayout(orientation = 'vertical')
        self.signs.add_widget(plas)
        minus = Button(text = '-')
        minus.bind(on_press = signs_press)
        self.signs.add_widget(minus)
        equal = Button(text = '=')
        equal.bind(on_press = equal_press)
        self.signs.add_widget(equal)
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
        left = BoxLayout(orientation = 'horizontal')
        calc.add_widget(self.board)
        left.add_widget(calc)
        left.add_widget(self.signs)
        
        calc.add_widget(self.keypad)
        return left
        
        
        

if __name__ == '__main__':
    MyApp().run()