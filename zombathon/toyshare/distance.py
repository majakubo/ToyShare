import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

#ulica nr miasto
def calculate_distance(addres_s, addres_e):
    geolocator = Nominatim()
    location_s = geolocator.geocode(addres_s)
    location_e = geolocator.geocode(addres_e)

    position_s = (location_s.latitude, location_s.longitude)
    position_e = (location_e.latitude, location_e.longitude)

    return geodesic(position_s, position_e)


