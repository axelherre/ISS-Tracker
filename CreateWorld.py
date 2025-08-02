import turtle
iss = turtle.Turtle()
user = turtle.Turtle()
screen = turtle.Screen()

def createWorld():
    screen.setup(1920, 1080)
    screen.setworldcoordinates(-180, -90,180,90)

    screen.bgpic("WorldMap.gif")
    
    screen.register_shape("ISSIcon.gif")
    iss.shape("ISSIcon.gif")
    
    screen.register_shape("UserIcon.gif")
    user.shape("UserIcon.gif")

    iss.turtlesize(0.5,0.5,0.5)
    iss.setheading(45)
    iss.penup()

    user.turtlesize(0.5,0.5,0.5)
    user.setheading(45)
    user.penup()