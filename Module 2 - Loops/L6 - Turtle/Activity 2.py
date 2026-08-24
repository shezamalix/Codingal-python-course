import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500, 500)

pen = turtle.Turtle()

sides = 3
angle = 360 / sides

pen.forward(150)
pen.left(120)
pen.forward(150)
pen.left(120)
pen.forward(150)

pen.penup()

pen.right(150)
pen.forward(80)
pen.right(90)
pen.pendown()

pen.forward(150)
pen.right(120)
pen.forward(150)
pen.right(120)
pen.forward(150)
pen.right(120)


    

turtle.done()