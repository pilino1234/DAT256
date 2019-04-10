from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/main_menu.kv")

from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.vector import Vector


class PackageButton(ButtonBehavior, Image):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

    def on_release():
        print('package button clicked!')

class MainMenuScreen(Screen):
    pass
