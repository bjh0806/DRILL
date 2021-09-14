import turtle

def drunken_up_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_down_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def drunken_right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(drunken_up_move, 'w')
turtle.onkey(drunken_left_move, 'a')
turtle.onkey(drunken_down_move, 's')
turtle.onkey(drunken_right_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
