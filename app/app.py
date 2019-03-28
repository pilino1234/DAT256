from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from presenter.screen.main_menu import MainMenuScreen
from presenter.screen.settings import SettingsScreen
from presenter.screen.math import MathScreen

# App screens
screen_manager = ScreenManager()
screen_manager.add_widget(MainMenuScreen(name='main_menu'))
screen_manager.add_widget(SettingsScreen(name='settings'))
screen_manager.add_widget(MathScreen(name='math'))
screen_manager.current = 'main_menu'

class Carrepsa(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    Carrepsa().run()
