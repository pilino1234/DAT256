from geopy.distance import geodesic


class Location:
    """Represents a geolocation."""

    def __init__(self, name: str, longitude: str, latitude: str):
        """Initialize the location"""
        super(Location, self).__init__()
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def dist_to(self, other) -> float:
        """Returns the distance to the other location in km"""
        p1 = (self.latitude, self.longitude)
        p2 = (other.latitude, other.longitude)
        dist_miles = geodesic(p1, p2).miles
        dist_km = dist_miles / 0.62137119223733
        return dist_km

    def is_close_to(self, other) -> bool:
        return self.dist_to(other) < 3.5

    def __str__(self):
        """Format a delivery request for printing"""
        return "Location: ({longitude}, {latitude}) {name}".format(
            self.longitude, self.latitude, self.name)
