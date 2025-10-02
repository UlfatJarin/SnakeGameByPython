
import turtle 
import time

delay = 0.1

#setup Screen 
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0) # turns off the screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()  #so that it doesnot draw anything
head.goto(0,0)  # starts with the center of screen 
head.direction ="stop"

#functions

def go_up():
    head.direction ="up"
def go_down():
    head.direction ="down"
def go_left():
    head.direction ="left"
def go_right():
    head.direction ="right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y +20)
def move():
    if head.direction == "down":
        y = head.ycor()
        head.sety(y -20)
def move():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x -20)
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x +20)


# keyboard binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()