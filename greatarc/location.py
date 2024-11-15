import math

class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def calculate_distance(self, other_location, unit="km"):
        import math
        # Haversine formula to calculate distance between two points on the Earth
        
        radius_km = 6371
        radius_mi = (6371 * 0.621371)
        
        radius = 6371  # Earth radius in kilometers
        dlat = math.radians(other_location.latitude - self.latitude)
        dlon = math.radians(other_location.longitude - self.longitude)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(self.latitude)) * \
            math.cos(math.radians(other_location.latitude)) * math.sin(dlon / 2) ** 2
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        if unit == "km":
        distance = radius_km * c
        elif unit == "miles":
        distance = radius_mi * c
        else:
        raise ValueError("Unit must be 'km' or 'miles'")
        
        return distance


