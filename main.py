from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class BotApp(App):
    def build(self):
        self.lbl = Label(text="XAUUSD Bot Ready\nSurat")
        Clock.schedule_once(lambda dt: self.start(), 2)
        return self.lbl

    def start(self):
        self.lbl.text = "Bot Started - waiting for signal"

BotApp().run()
