from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class RequestListButton(ListItemButton):
    pass


class RequestDelivery(BoxLayout):
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
        self.packinfo_list_list.adapter.data.extend(["Your delivery was successfully requested"])

        # Reset the ListView
        self.packinfo_list._trigger_reset_populate()

    def getSender():
        senders_loc = self.senders_loc_text_input.text
        return senders_loc

    def getDestination():
        destination_loc = self.destionation_loc_text_input.text
        return destination_loc

    def getWeight():
        package_weight = self.destionation_loc_text_input.text
        return package_weight

    def getPrice():
        price = self.destionation_loc_text_input.text
        return price

    def getMoneyLock():
        money_lock = self.destionation_loc_text_input.text
        return money_lock

    def getPackageDescription():
        package_description = self.destionation_loc_text_input.text
        return package_description

class RequestDeliveryApp(App):
    def build(self):
        return RequestDelivery()

dbApp = RequestDeliveryApp()

dbApp.run()
