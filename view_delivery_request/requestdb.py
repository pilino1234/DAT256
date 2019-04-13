from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class RequestListButton(ListItemButton):
    pass


class RequestDB(BoxLayout):
    # Connects the value in the TextInput widget to these
    # fields
    senders_loc_text_input = ObjectProperty()
    destination_loc_input = ObjectProperty()
    package_weight_text_input = ObjectProperty()
    price_text_input = ObjectProperty()
    package_name_text_input = ObjectProperty()
    money_lock_text_input = ObjectProperty()
    package_description_text_input = ObjectProperty()
    packinfo_list = ObjectProperty()

    def submit_package(self):
        # Add confirmation to ListView
        self.packinfo_list.adapter.data.extend(["Your delivery has been submitted"])

        # Reset the ListView
        self.packinfo_list._trigger_reset_populate()

    def getSender(self):
        senders_loc = self.senders_loc_text_input.text
        return senders_loc

    def getDestination(self):
        destination_loc = self.destination_loc_text_input.text
        return destination_loc

    def getWeight(self):
        package_weight = self.package_weight_text_input.text
        return package_weight

    def getPrice(self):
        price = self.price_text_input.text
        return price

    def getMoneyLock(self):
        money_lock = self.money_lock_text_input.text
        return money_lock

    def getPackageDescription(self):
        package_description = self.package_description_text_input.text
        return package_description

class RequestDBApp(App):
    def build(self):
        return RequestDB()

dbApp = RequestDBApp()

dbApp.run()
