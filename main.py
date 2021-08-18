from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
#начало screen
class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Только не ты...")
        btn.on_press = self.next
        self.add_widget(btn) # экран - это виджет, на котором могут создаваться все другие (потомки)
#next scr        
    def next(self):
        self.manager.transition.direction = 'left' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'second'
#выбор скри
class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        layout = BoxLayout()
        btn = Button(text="амогус?!")
        btn.on_press = self.next
        btnback = Button (text = "Лучше не буду.")
        btnback.on_press = self.back
        layout.add_widget(btn)
        layout.add_widget(btnback)
        self.add_widget(layout)
#back scr   
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Tri'
    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Bez'
#scr амогус
class TriScr(Screen):
    def __init__(self, name='Tri'):
        super().__init__(name=name)
        i = Image(source="AMOGIS.jpg")
        self.add_widget(i)
#next 3
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
#scr у тебя не было выбора
class BezScr(Screen):
    def __init__(self, name='Bez'):
        super().__init__(name=name)
        btn = Button(text="У тебя есть выбор?")
        btn.on_press = self.next
        self.add_widget(btn)
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'zel'
class ZelanieScr(Screen):
    def __init__(self, name='zel'):
        super().__init__(name=name)
        layout1 = BoxLayout()
        btn = Button (text = "есть")
        btn2 = Button (text = 'Нет, нету')
        btn.on_press = self.next
        btn2.on_press = self.back
        layout1.add_widget(btn)
        layout1.add_widget(btn2)
        self.add_widget(layout1)
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'Est'
    def back(self):
        self.manager.transition.direction = "right"
        self.manager.current = 'Nety'
#у тебя нету выбора ало чел
class EstScr(Screen):
    def __init__(self, name='Est'):
        super().__init__(name=name)
        btn = Button(text="Я так не думаю...")
        btn.on_press = self.next
        self.add_widget(btn)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Estnonet'
#я же говорил что нету
class EstnonnetScr(Screen):
    def __init__(self, name='Estnonet'):
        super().__init__(name=name)
        q = Image(source="AMOGIS.jpg")
        self.add_widget(q)
class NetyScr(Screen):
    def __init__(self, name='Nety'):
        super().__init__(name=name)
        btn = Button(text="Так не интерено):")
        btn.on_press = self.exit
        self.add_widget(btn)
    def exit(self):
        exit()
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(TriScr())
        sm.add_widget(BezScr())
        sm.add_widget(ZelanieScr())
        sm.add_widget(EstScr())
        sm.add_widget(EstnonnetScr())
        sm.add_widget(NetyScr())
        return sm
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        
app = MyApp()
app.run()