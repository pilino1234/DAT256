from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivymd.menus import MDDropdownMenu


class DropdownMenu(MDDropdownMenu):
    """A dropdown menu which copies the width and position of the caller widget."""

    def display_menu(self, caller: Widget):
        """Displays a dropdown of items, calculates size, position and plays an animation."""
        c = caller.to_window(caller.center_x, caller.center_y)

        target_width = caller.width

        target_height = dp(48 * len(self.items))

        if 0 < self.max_height < target_height:
            target_height = self.max_height

        if self.ver_growth is not None:
            ver_growth = self.ver_growth
        else:
            if target_height <= c[1] - self.border_margin:
                ver_growth = 'down'
            elif target_height < Window.height - c[1] - self.border_margin:
                ver_growth = 'up'
            else:
                if c[1] >= Window.height - c[1]:
                    ver_growth = 'down'
                    target_height = c[1] - self.border_margin
                else:
                    ver_growth = 'up'
                    target_height = Window.height - c[1] - self.border_margin

        if ver_growth == 'down':
            tar_y = c[1] - target_height - caller.height / 4
        else:
            tar_y = c[1]

        tar_x = c[0] - target_width / 2

        anim = Animation(x=tar_x,
                         y=tar_y,
                         width=target_width,
                         height=target_height,
                         duration=.3,
                         transition='out_quint')
        menu = self.ids.md_menu
        menu.pos = c
        anim.start(menu)
