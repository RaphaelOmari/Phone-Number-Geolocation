# Phone Number Locator

## Description
This project is a Python application that allows users to input a phone number and then provides the geographical location and service provider associated with that number. It uses the `phonenumbers` library for parsing phone numbers and obtaining geographic information and service providers. Additionally, it uses the `OpenCage Geocode` API for converting location names to geographical coordinates and `Folium` for visualizing these locations on a map.

## Features
- Parse phone numbers to find geographic location and service provider.
- Convert location names into geographical coordinates using the OpenCage Geocoder API.
- Visualize the location on a map using Folium.

## Requirements
- Python 3.10
- phonenumbers
- folium
- opencage.geocoder

## Setup and Installation
1. Ensure that Python 3.x is installed on your system.
2. Install the required Python packages:
3. Obtain an API key from [OpenCage Geocoder](https://opencagedata.com/).

## Usage
1. Run the script:
3. Obtain an API key from [OpenCage Geocoder](https://opencagedata.com/).

## Usage
1. Run the script:
2. Enter the phone number when prompted.
3. The program will display the location and service provider for the entered phone number, and generate an HTML file (`finishedlocal.html`) showing the location on a map.

## Configuration
- Set the OpenCage Geocoder API key in your environment variables or directly in the scrip(`your_default_api_key`).