import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import os

def get_location_and_provider(phone_number):
    try:
        phone_number_parsed = phonenumbers.parse(phone_number)
        location = geocoder.description_for_number(phone_number_parsed, "en")
        service_provider = carrier.name_for_number(phone_number_parsed, "en")
        return location, service_provider
    except phonenumbers.NumberParseException:
        return None, None

def get_coordinates(location, api_key):
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(location)
    if results:
        latitude = results[0]["geometry"]['lat']
        longitude = results[0]["geometry"]['lng']
        return latitude, longitude
    else:
        return None, None

def create_map(coordinates, location):
    my_map = folium.Map(location=coordinates, zoom_start=10)
    folium.Marker(coordinates, popup=location).add_to(my_map)
    my_map.save("finishedlocal.html")

def main():
    test_number = input("Please input your test number: ")
    location, service_provider = get_location_and_provider(test_number)

    if location and service_provider:
        print(f"{location} provider is {service_provider}")

        api_key = os.getenv('OPENCAGE_API_KEY', 'your_default_api_key')
        latitude, longitude = get_coordinates(location, api_key)

        if latitude and longitude:
            print(f"Location Coordinates: {latitude}, {longitude}")
            create_map([latitude, longitude], location)
        else:
            print("Geocoding failed.")
    else:
        print("Invalid phone number or parsing failed.")

if __name__ == "__main__":
    main()
