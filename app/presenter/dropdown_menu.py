from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivymd.menus import MDDropdownMenu


class DropdownMenu(MDDropdownMenu):
    """A dropdown menu which copies the width and position of the caller widget."""

    def display_menu(self, caller: Widget):
        """Displays a dropdown of items, calculates size, position and plays an animation."""
        # We need to pick a starting point, see how big we need to be,
        # and where to grow to.
        c = caller.to_window(caller.center_x,
                             caller.center_y)  # Starting coords

        target_width = caller.width
        # md_menu = self.ids.md_menu
        # opts = md_menu.layout_manager.view_opts
        # md_item = md_menu.view_adapter.get_view(1, md_menu.data[1],
        #                                         opts[1]['viewclass'])

        target_height = sum([dp(48) for i in self.items])
        # If we're over max_height...
        if 0 < self.max_height < target_height:
            target_height = self.max_height

        # ---ESTABLISH VERTICAL GROWTH DIRECTION---
        if self.ver_growth is not None:
            ver_growth = self.ver_growth
        else:
            # If there's enough space below us:
            if target_height <= c[1] - self.border_margin:
                ver_growth = 'down'
            # if there's enough space above us:
            elif target_height < Window.height - c[1] - self.border_margin:
                ver_growth = 'up'
            # otherwise, let's pick the one with more space and adjust ourselves
            else:
                # if there's more space below us:
                if c[1] >= Window.height - c[1]:
                    ver_growth = 'down'
                    target_height = c[1] - self.border_margin
                # if there's more space above us:
                else:
                    ver_growth = 'up'
                    target_height = Window.height - c[1] - self.border_margin

        if ver_growth == 'down':
            tar_y = c[1] - target_height - caller.height / 4
        else:  # should always be 'up'
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
