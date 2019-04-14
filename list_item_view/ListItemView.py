from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ListItemView(BoxLayout):
    pass


class ListItemViewApp(App):
    def build(self):
        return ListItemView()

    @staticmethod
    def get_name():
        return "Stort paket med glass"

    @staticmethod
    def get_origin():
        return "Gothenburg"

    @staticmethod
    def get_destination():
        return "New York"

    @staticmethod
    def get_price():
        return "100 SEK"

    @staticmethod
    def get_weight():
        return "5 kg"

    @staticmethod
    def get_price():
        return "100 SEK"
    @staticmethod
    def get_distance():

       from geopy.geocoders import Nominatim
       geolocator = Nominatim()
       location = geolocator.geocode("Gothenburg")
       var = ((location.latitude, location.longitude))
       print((var))

       geolocator2 = Nominatim()
       location2 = geolocator2.geocode("Stockholm")
       var2 = ((location2.latitude, location2.longitude))
       print((location2.latitude, location2.longitude))

       from geopy.distance import geodesic
       return str(round(geodesic(var,var2).kilometers))


if __name__ == '__main__':
    ListItemViewApp().run()
