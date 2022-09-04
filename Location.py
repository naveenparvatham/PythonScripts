# importing geopy library
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="GetLoc")

# Entering the location name
getLoc = loc.geocode("Salt Lake City")

# Printing address
print(getLoc.address)

# Printing latitude and longitude
print("Latitude =", getLoc.latitude)
print("Longitude =", getLoc.longitude)
