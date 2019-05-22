from geopy.distance import geodesic


class Location:
    """Represents a geolocation."""

    def __init__(self, name: str, longitude: float, latitude: float):
        """Initialize the location"""
        super(Location, self).__init__()
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def dist_to(self, other: 'Location') -> float:
        """Returns the distance to the other location in km"""
        p1 = (self.latitude, self.longitude)
        p2 = (other.latitude, other.longitude)
        dist_miles = geodesic(p1, p2).miles
        dist_km = dist_miles / 0.62137119223733
        return dist_km

    def is_close_to(self, other: 'Location') -> bool:
        """Checks if the other location is within a specified km radius."""
        return self.dist_to(other) < 5

    def __str__(self):
        """Format a delivery request for printing"""
        return "Location: ({longitude}, {latitude}) {name}".format(
            longitude=self.longitude, latitude=self.latitude, name=self.name)

    def to_dict(self) -> dict:
        """Returns the location as a dict."""
        return {
            'name': self.name,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    @staticmethod
    def from_dict(data_dict: dict) -> 'Location':
        """Creates a Location from a dict."""
        return Location(data_dict['name'], data_dict['longitude'],
                        data_dict['latitude'])
