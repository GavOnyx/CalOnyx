import kivy

kivy.require("2.3.1")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel


class Root(TabbedPanel):
    """This is the root widget used to host the others"""

    # This is used to add events to the events list
    def add_event(self):
        new_event = Label(text="new event", size_hint=(0.2, 0.2))
        self.add_widget(new_event)


class CalApp(App):
    def build(self):
        Window.size = (350, 650)
        return Root()


if __name__ == "__main__":
    CalApp().run()
