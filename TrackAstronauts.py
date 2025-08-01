import webbrowser
import urllib.request
import geocoder
import json

def trackAstronauts():
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    file = open("iss.txt", "w")
    file.write("There are currently " + 
              str(result["number"])+" astronauts in space: \n\n")
    people = result["people"]
    for p in people:
        file.write(p["name"] + " - on board: " + p["craft"] + "\n")
    g = geocoder.ip('me')
    file.write("\n Your current lat / long is: " + str(g.latlng))
    file.close()
    webbrowser.open("iss.txt")
