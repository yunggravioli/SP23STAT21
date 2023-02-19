import turtle # might need Python 3.11 or possibly install turtle

# if you are looking at this in Week 01, I'm assuming you know a lot already

# create a turtle object assign it to "t"
t = turtle.Turtle()

# set the turtle line thickness (5 pixels) color (UCLA Blue) fill (UCLA Gold)
# and drawing speed (default = 1 so twice default speed)
t.pensize(5)
t.pencolor('#2774AE')  # UCLA Blue
t.fillcolor('#FFD100')  # UCLA Gold
t.speed(2)

# fill first, then draw
t.begin_fill()

# the "turtle" starts facing right
# draw the right half of the heart
t.left(45)  # degrees
t.forward(100)  # distance
t.circle(50, 180)  # radius, extent

# then draw the left half
t.right(90)
t.circle(50, 180)
t.forward(100)

# need to end_fill for drawing to be filled
t.end_fill()

# move the turtle to a new position
t.penup()
t.goto(150, 0)
t.pendown()

t.fillcolor('#2774AE')
t.pencolor('#FFD100')

# fill first, then draw
t.begin_fill()

# draw the left half of the heart
t.left(-90) # degrees
t.forward(100) # distance
t.circle(50, 180) # radius, extent

# then draw the other half
t.right(90)
t.circle(50, 180)
t.forward(100)

# need to end_fill for drawing to be filled
t.end_fill()

# move the turtle to a third position
t.penup()
t.goto(-150, 0)
t.pendown()

# fill first, then draw
t.begin_fill()

# draw the right half of the heart
t.right(0) # degrees
t.forward(-100) # distance
t.circle(50, -180) # radius, extent

# then draw the other half
t.left(-90)
t.circle(-50, 180)
t.forward(100)

# need to end_fill for the drawing to be filled
t.end_fill()

# hide the cursor
t.hideturtle()

# keep the window open, must manually close
turtle.done()

