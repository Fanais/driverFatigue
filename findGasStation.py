import googlemaps
import requests
import json
import playsound
from datetime import datetime
from gtts import gTTS
from io import BytesIO


def giveLocationWarning():
    # # get current location
    r = requests.post(
        'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDYWHatnxIjjNRFP2C-wPIfyRmSI0MuyaY')
    currLocJson = r.json()
    latitude = currLocJson["location"]["lat"]
    longitude = currLocJson["location"]["lng"]

    gmaps = googlemaps.Client(key='AIzaSyDYWHatnxIjjNRFP2C-wPIfyRmSI0MuyaY')

    # find closest gas station
    places_results = gmaps.places("gas station", (latitude, longitude))
    closest_station = places_results["results"][0]["formatted_address"]

    # # Request directions via driving
    now = datetime.now()
    directions_result = gmaps.directions(
        (latitude, longitude), closest_station, mode="driving", departure_time=now)
    closest_dist = float(directions_result[0]["legs"][0]["distance"]["text"].split(" ")[
        0])
    closest_dur = float(directions_result[0]["legs"]
                        [0]["duration"]["text"].split(" ")[0])

    # talk
    mp3_fp = BytesIO()
    text_to_string = 'You are extremely drowsy. I highly recommend taking a quick 15 minute nap to avoid the chances of an accident. The closest gas station is %.1f minutes away by car at a distance of %.1f miles.' % (
        closest_dur, closest_dist)
    tts = gTTS(text_to_string, 'en')
    tts.save("warning.mp3")
    playsound.playsound("warning.mp3")
