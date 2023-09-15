from turtle import Turtle,Screen
jim=Turtle()

screen=Screen()

def move_forward():
    jim.fd(10)
def move_backward():
    jim.backward(10)

def move_right():
    new_heading=jim.heading()-10
    jim.setheading(new_heading)

def move_left():
    #jim.left(10)
    new_heading=jim.heading()+10
    jim.setheading(new_heading)
def clear_screen():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

def pen_up():
    jim.penup()
def pen_down():
    jim.pendown()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(pen_up,"Up")
screen.onkey(pen_down,"Down")
screen.onkey(clear_screen,"c")
screen.exitonclick()