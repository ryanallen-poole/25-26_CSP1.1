#   a113_flower.py
#   This code draws a flower.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# draw stem
painter.color("green")
painter.pensize(35)
painter.goto(0, -220)
painter.setheading(90)
painter.forward(100)
# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2.6)

# draw flower
painter.color("pink")
painter.goto(-75, 100)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.stamp()

#draw pollen/seed thing
painter.turtlesize(0.5)
painter.color("yellow")
painter.goto(-75, 100)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()