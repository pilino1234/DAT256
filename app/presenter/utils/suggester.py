import threading

from kivymd.menus import MDMenuItem, MDDropdownMenu
from model.map_api import MapAPI
from model.location import Location


class LocationSuggester():
    """Shows location suggestions for a textfield."""

    suggestion_thread = None
    suggestion_dropdown = None
    suggestions = []
    ignore_text_change = ""
    currently_used_suggestion = None

    def __init__(self, textfield):
        """Initialize the location"""
        super(LocationSuggester, self).__init__()
        self.textfield = textfield

    def on_search(self):
        if self.textfield.text == self.ignore_text_change:
            return

        if self.suggestion_thread:
            self.suggestion_thread.cancel()

        self.suggestion_thread = threading.Timer(
            0.2, lambda: self.show_suggestions())
        self.suggestion_thread.start()

    def show_suggestions(self):
        """Show suggestions based on current input in textfield."""
        suggestion_thread = None

        # Close previous suggestions
        if self.suggestion_dropdown:
            self.suggestion_dropdown.dismiss()

        # Avoid vague and empty inputs
        if len(self.textfield.text) < 2:
            self.currently_used_suggestion = None
            return

        new_suggestions = MapAPI.get_search_suggestions(self.textfield.text)

        # Only update if we need to
        if new_suggestions == self.suggestions:
            return
        self.suggestions = new_suggestions

        # Create menu items from suggestions
        search_suggestions = [{
            'viewclass': 'MDMenuItem',
            'text': s['name'] + ' ' + s['district'],
            'callback': lambda x: self.__apply_suggestion(s)
        } for s in self.suggestions]

        # Display dropdown with suggestions
        self.suggestion_dropdown = MDDropdownMenu(
            items=search_suggestions, width_mult=8)
        self.suggestion_dropdown.open(self.textfield)

    def __apply_suggestion(self, suggestion):
        self.currently_used_suggestion = Location.from_dict(suggestion)
        pretty_suggestion = suggestion['name'] + ' ' + suggestion['district']
        self.ignore_text_change = self.textfield.text = pretty_suggestion
