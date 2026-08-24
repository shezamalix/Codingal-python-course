import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500, 500)

# line 6 initializes the drawing turtle
pen = turtle.Turtle()

sides = 20
ext_angle = 360 / sides

for i in range(sides):
    #when u use forward the number denotes the lenght of the line u want
    #for right its the angle by which the numbe rotates
    pen.forward(30)
    pen.left(ext_angle)
    

turtle.done()

