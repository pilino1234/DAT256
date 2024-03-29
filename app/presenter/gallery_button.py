import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.modalview import ModalView
from kivymd.button import MDFloatingActionButton
from kivymd.filemanager import MDFileManager
from kivymd.toast import toast

Builder.load_file("view/gallery_button.kv")


class GalleryButton(MDFloatingActionButton):
    """A FAB which opens the gallery."""

    path_selected_callback = ObjectProperty(lambda: None)

    def __init__(self, **kwargs):
        """Initializes the gallery button"""
        super(GalleryButton, self).__init__(**kwargs)
        self.manager_open = False
        self.manager = None

    def on_release(self):
        """Function called when the button is released."""
        self.file_manager_open()

    def file_manager_open(self):
        """Opens the file manager window"""
        if not self.manager:
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path)

            # Monkey patch file selection so that history is not erased
            def select_dir_or_file(path):
                """Called by tap on the name of the directory or file."""
                if os.path.isfile(path):
                    self.file_manager.select_path(path)
                    return

                self.file_manager.current_path = path
                self.file_manager.show(path)

            self.file_manager.select_dir_or_file = select_dir_or_file

            self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
        self.manager.open()

    def select_path(self, path):
        """
        It will be called when you click on the file name or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;

        """
        self.path_selected_callback(path)

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""
        self.manager.dismiss()
        self.manager_open = False
