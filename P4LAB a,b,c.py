import turtle
wn = turtle.Screen()
j = turtle.Turtle()
j.pensize(9)

# Move turtle to starting position
j.penup()
j.setposition(x=-250, y=0)
j.pendown()

# Start letter "J"

j.color("pink")
j.right(90)
j.forward(100)
for i in range (25) :
    j.forward(3)
    j.right(7)
j.penup()
j.right(50)
j.forward(150)
j.right(45)
j.pendown()

# Start letter "F"

j.color("hot pink")
j.forward(55)
j.backward(55)
j.right(90)
j.forward(114)
j.backward(57)
j.left(90)
j.forward(50)
j.penup()
j.forward(50)
j.pendown()

# Start "Square"

j.color("grey")
j.forward(100)
j.right(90)
j.forward(100)
j.right(90)
j.forward(100)
j.right(90)
j.forward(100)
j.penup()
j.right(110)
j.forward(170)
j.pendown()

# Start "Circle"

j.color("light blue")
j.circle(60)



