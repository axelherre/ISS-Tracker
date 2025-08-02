import geocoder
import CreateWorld

user = CreateWorld.user
g = geocoder.ip('me')

def fetchUserPosition():
    userLat = g.lat
    userLng = g.lng
    print("Current user postion: Lat " + str(userLat)+" Lon "+str(userLng))
    user.goto(userLat,userLng)
