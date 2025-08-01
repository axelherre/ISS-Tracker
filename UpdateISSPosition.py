import time
import CreateWorld
import json
import urllib.request

iss = CreateWorld.iss

def updatePosition():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    lat = float(lat)
    lon = float(lon)

    print("\nLatitude: "+str(lat))
    print("\nLongitude: "+str(lon))

    iss.goto(lon,lat)
    time.sleep(5)