# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

# penup stops turtle drawing
painter.circle(100)
painter.penup()
painter.forward(200)
painter.pendown()
#pendown starts the turtle drawing
painter.circle(100)
painter.penup()
painter.back(160)
painter.pendown()
painter.circle (50)
painter.penup()
painter.forward(210)
painter.pendown()
painter.circle(50)
painter.penup()
painter.left(130)
painter.forward(20)
painter.pendown()
painter.circle(60)
painter.penup()
painter.backward(80)
painter.right(90)
painter.pendown()
painter.circle(250)

painter.penup()
painter.left(100)
painter.forward(300)
painter.pendown()
painter.forward(100)
painter.penup()
painter.right(180)
painter.forward(100)
painter.right(180)
painter.foward(100)
painter.pendown()
painter.forward(100)
# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()