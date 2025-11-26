#colors/setup
import turtle as trtl
trtl.speed(0)
trtl.pencolor('maroon')
trtl.pensize(8)
trtl.penup()
trtl.goto(-125,10)
trtl.left(45)
trtl.pendown()
#head
trtl.begin_fill()
for n in range(2):
    trtl.circle(150,90)
    trtl.circle(75,90)
trtl.fillcolor('maroon')
trtl.end_fill()
#eyes
trtl.pensize(8)
trtl.pencolor('black')
trtl.penup()
trtl.left(45)
trtl.forward(150)
trtl.pendown()
trtl.begin_fill()
trtl.fillcolor('white')
trtl.circle(20)
trtl.end_fill()
trtl.penup()
trtl.left(90)
trtl.forward(15)
trtl.pendown()
trtl.begin_fill()
trtl.fillcolor('black')
trtl.circle(10)
trtl.end_fill()
trtl.penup()
trtl.forward(85)
trtl.pendown()
trtl.begin_fill()
trtl.fillcolor('white')
trtl.circle(20)
trtl.end_fill()
trtl.forward(5)
trtl.begin_fill()
trtl.fillcolor('black')
trtl.circle(10)
trtl.end_fill()
#arm 1
trtl.pensize(8)
trtl.pencolor('maroon')
trtl.penup()
trtl.left(-135)
trtl.goto(-125,10)
trtl.pendown()
trtl.circle(-75,130)
trtl.circle(75,130)
trtl.forward(62)
trtl.penup()
trtl.goto(-155,-10)
trtl.pendown()
trtl.circle(-65,130)
trtl.circle(105,173)
#wand
trtl.pensize(5)
trtl.pencolor('black')
trtl.begin_fill()
trtl.fillcolor('black')
trtl.left(15)
trtl.forward(-60)
trtl.forward(120)
trtl.right(90)
trtl.forward(10)
trtl.right(90)
trtl.forward(120)
trtl.right(90)
trtl.forward(10)
trtl.right(90)
trtl.forward(120)
trtl.end_fill()



#arm2
trtl.pensize(8)
trtl.pencolor('maroon')
trtl.penup()
trtl.left(-135)
trtl.goto(-125,10)
trtl.pendown()
trtl.circle(-75,130)
trtl.circle(75,130)
trtl.forward(100)
trtl.penup()
trtl.goto(-150,-15)
trtl.pendown()
trtl.circle(-65,130)
trtl.circle(105,173)
#arm3
trtl.penup()
trtl.left(-135)
trtl.goto(-125,10)
trtl.pendown()
trtl.circle(-75,130)
trtl.circle(75,130)
trtl.forward(100)
trtl.penup()
trtl.goto(-150,-15)
trtl.pendown()
trtl.circle(-65,130)
trtl.circle(105,173)
#arm4
trtl.penup()
trtl.left(-0)
trtl.goto(-110,10)
trtl.pendown()
trtl.circle(-75,130)
trtl.circle(75,130)
trtl.forward(100)
trtl.penup()
trtl.goto(-150,-15)
trtl.pendown()
trtl.circle(-65,130)
trtl.circle(105,173)
#arm5
trtl.penup()
trtl.left(-300)
trtl.goto(-110,10)
trtl.pendown()
trtl.circle(-75,130)
trtl.circle(75,130)
trtl.forward(100)
trtl.penup()
trtl.goto(-150,-15)
trtl.pendown()
trtl.circle(-65,130)
trtl.circle(105,173)
#mouth
trtl.penup()
trtl.pencolor('black')
trtl.goto(-200,50)
trtl.pendown()
trtl.circle(-20,360)
#hat
trtl.pencolor('black')
trtl.penup()
trtl.goto(-260,240)
trtl.right(60)
trtl.pendown()
trtl.forward(160)
trtl.penup()
trtl.goto(-210,245)
trtl.right(270)
trtl.pendown()
trtl.forward(50)
trtl.pencolor('red')
trtl.forward(20)
trtl.right(90)
trtl.forward(60)
trtl.penup()
trtl.forward(-60)
trtl.left(90)
trtl.pendown()
trtl.pencolor('black')
trtl.forward(70)
trtl.penup()
trtl.right(90)
trtl.pendown()
trtl.forward(60)
trtl.penup()
trtl.right(90)
trtl.pendown()
trtl.forward(70)
trtl.pencolor('red')
trtl.forward(20)
trtl.right(90)
trtl.forward(60)
trtl.penup()
trtl.forward(-60)
trtl.left(90)
trtl.pendown()
trtl.pencolor('black')
trtl.forward(50)
#magic hat build
my_turtles = []

turtle_shapes = ["arrow"]
turtle_colors = ["black"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  t.penup()
  my_turtles.append(t)


startx = -260
starty = 240
direction = 90
#
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(45)
  t.forward(50)



  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()


#magic hat build 2
my_turtles = []

turtle_shapes = ["arrow"]
turtle_colors = ["black"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  t.penup()
  my_turtles.append(t)


startx = -100
starty = 250
direction = 90

for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(-45)
  t.forward(50)


#
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

wn = trtl.Screen()
wn.mainloop()

wn = trtl.Screen()
wn.mainloop()












wn = trtl.Screen()
wn.mainloop()