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
        self.board = Label(text='')
        self.keypad = GridLayout(rows=3, cols=3)
        self.num_list = []
        self.signs = BoxLayout(orientation='vertical')  

        def equal_press(instance):
            try:
                self.board.text = str(eval(self.board.text))
            except Exception:
                self.board.text = "Error"

        def signs_press(instance):
            if self.board.text and self.board.text[-1] not in ['+', '-', '=', '/', '*']:
                self.board.text += instance.text

        def c_press(instance):
            self.board.text = ''

        def press(instance):
            self.board.text += instance.text

        # кнопки
        c = Button(text='C')
        c.bind(on_press=c_press)
        self.signs.add_widget(c)

        plus = Button(text='+')
        plus.bind(on_press=signs_press)
        self.signs.add_widget(plus)

        minus = Button(text='-')
        minus.bind(on_press=signs_press)
        self.signs.add_widget(minus)

        equal = Button(text='=')
        equal.bind(on_press=equal_press)
        self.signs.add_widget(equal)

        divide = Button(text='/')
        divide.bind(on_press=signs_press)
        self.signs.add_widget(divide)

        multiply = Button(text='*')
        multiply.bind(on_press=signs_press)
        self.signs.add_widget(multiply)

        nul = Button(text='0')
        nul.bind(on_press=press)
        self.signs.add_widget(nul)

        # цифры
        for i in range(1, 10):
            btn = Button(text=f"{i}")
            btn.bind(on_press=press)
            self.num_list.append(btn)

        for btn in self.num_list:
            self.keypad.add_widget(btn)

    def build(self):
        main = BoxLayout(orientation='vertical')
        top = BoxLayout(orientation='horizontal')

        top.add_widget(self.board)
        top.add_widget(self.signs)

        main.add_widget(top)
        main.add_widget(self.keypad)

        return main


if __name__ == '__main__':
    MyApp().run()
