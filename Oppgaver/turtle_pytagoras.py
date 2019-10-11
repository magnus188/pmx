import turtle
import math

a = 100
b = 200
c = math.sqrt(a**2 + b**2)

# Create triangle
pen = turtle.Turtle()
startPos = pen.position()
pen.forward(a)
pen.left(90)
pen.forward(b)
pen.goto(startPos)

#Create a area
pen.color("red")
pen.right(180)
pen.forward(a)
pen.left(90)
pen.forward(a)
pen.left(90)
pen.forward(a)

#Create b area
pen.color("green")
pen.right(90)
pen.forward(b)
pen.left(90)
pen.forward(b)
pen.left(90)
pen.forward(b)

#create c area
pen.color("blue")
#turn with angle of asin(a/c)
pen.right(math.degrees(math.asin(a/c)))
pen.forward(c)
pen.left(90)
pen.forward(c)
pen.left(90)
pen.forward(c)
