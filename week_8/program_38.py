import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color
# screen.bgpic("background.gif")  # Uncomment and add your image file if you have one

# Create turtle
t = turtle.Turtle()
t.color("black", "yellow")  # Pen color, Fill color

# Start filling
t.begin_fill()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()  # End filling

turtle.done()
