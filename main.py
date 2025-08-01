import TrackAstronauts
import CreateWorld
import UpdateISSPosition

TrackAstronauts.trackAstronauts()

CreateWorld.createWorld()

while True:
    UpdateISSPosition.updatePosition()
