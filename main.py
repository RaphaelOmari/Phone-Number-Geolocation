import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

testnumber  = input("Please input your test number: ")

test = phonenumbers.parse(testnumber)

mylocation = geocoder.description_for_number(test, "en")
service_prov = carrier.name_for_number(test, "en")
print(f"{mylocation} provider is {service_prov}")

key = 'abc'
geocoder = OpenCageGeocode(key)
query = str(mylocation)

results = geocoder.geocode(query)
print(results)

latitude = results[0]["geometry"]['lat']
longitude = results[0]["geometry"]['lng']

L1_location = [latitude, longitude]

print(L1_location)

myMap = folium.Map(location=L1_location, zoom_start=10)

folium.Marker(L1_location, popup=mylocation).add_to((myMap))
myMap.save("finishedlocal.html")