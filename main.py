import TrackAstronauts
import CreateWorld
import UpdateISSPosition
import getUserPosition

TrackAstronauts.trackAstronauts()
CreateWorld.createWorld()
getUserPosition.fetchUserPosition()


while True:
    UpdateISSPosition.updatePosition()
