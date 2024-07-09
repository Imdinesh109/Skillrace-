import turtle
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def draw_chakra():
    turtle.penup()
    turtle.goto(0, -7)
    turtle.pendown()
    turtle.color("navy")
    for i in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading((i * 360) / 24)
        turtle.pendown()
        turtle.forward(70)
def draw_indian_flag():
    turtle.speed(3)
    turtle.bgcolor("white")
    draw_rectangle("orange", -180, 100, 360, 66)
    draw_rectangle("white", -180, 34, 360, 66)
    draw_rectangle("green", -180, -32, 360, 66)
    draw_chakra()
    turtle.hideturtle()
    turtle.done()
draw_indian_flag()