import turtle
iss = turtle.Turtle()
screen = turtle.Screen()

def createWorld():
    screen.setup(1920, 1080)
    screen.setworldcoordinates(-180, -90,180,90)

    screen.bgpic("WorldMap.gif")
    screen.register_shape("ISSIcon.gif")
    iss.shape("ISSIcon.gif")
    iss.turtlesize(0.5,0.5,0.5)
    iss.setheading(45)
    iss.penup()