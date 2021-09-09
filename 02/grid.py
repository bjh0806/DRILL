import turtle

count = 4

turtle.penup()
turtle.goto(-250,250)
turtle.pendown()

while (count > 0):
    turtle.forward(500)
    turtle.right(90)
    count -= 1

count = 4

turtle.penup()
turtle.goto(-250,150)
turtle.pendown()

num = 0

while (count > 0):
    turtle.forward(500)

    if (num % 2 == 0):
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    else:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        
    count -= 1
    num += 1

count = 4

turtle.penup()
turtle.goto(-150,-250)
turtle.left(90)
turtle.pendown()

num = 0

while (count > 0):
    turtle.forward(500)

    if (num % 2 == 0):
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    else:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

    count -= 1
    num += 1

turtle.exitonclick()
