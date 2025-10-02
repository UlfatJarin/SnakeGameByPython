
import turtle 
import time
import random

delay = 0.1

#setup Screen 
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("skyblue")
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


#snake FoodFOOD
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()  #so that it doesnot draw anything
food.goto(0,100)  # starts with the center of screen 


segments = []


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

    if head.direction == "down":
        y = head.ycor()
        head.sety(y -20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x -20)

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

    #check for a collision with the food
    if head.distance(food)< 20:
        #move the food random place
        x = random.randint(-299,290)
        y = random.randint(-299,290)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle() 
        new_segment.speed(0) # animation speed
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
    
    #move the end segments first in reverse order
    for index in range(len(segments)-1 ,0,-1):
        x= segments[index -1].xcor()
        y= segments[index -1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments)> 0 :
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)


    move()

    time.sleep(delay)

wn.mainloop()