# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#create a spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#configure spider legs
leg = 0
radius = 60
while leg < num_legs:
    spider.goto(0,20)
    if leg <4
        spider.setheading(angle*leg+125)
        spider.pendown()
        spider.circle(radius, 120)
        spider.penup()
    else:
        spider.setheading(angle*leg+90)
        spider.pendown()
        spider.circle(radius, -120)
        spider.penup()

    leg = leg +1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()