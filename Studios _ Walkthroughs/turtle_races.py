# In this studio we are going to work step by step through the problem of racing turtles. The idea is that we want to
# create two or more turtles and have them race across the screen from left to right. The turtle that goes the farthest
# is the winner.

# There are several different, and equally plausible, solutions to this problem. Let’s look at what needs to be done,
# and then look at some of the options for the solution. When you are faced with a problem like this in computer science
# it is often a good idea to find a solution to a simple problem first and then figure out how to make the solution more
# general. So to start, let’s think about a solution to the simplest form of the problem, a race between two turtles.
# We’ll look at more complex races later.

# Here is a possible sequence of steps that we will need to accomplish:

# Import the modules we need
# Create a screen
# Create two turtles
# Move the turtles to their starting positions
# Send them racing across the screen
# Here is the Python code for the first 4 steps above. Continue below for a discussion on possible solutions.
import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
finish_line = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
finish_line.up()
finish_line.goto(150, 150)
andy.goto(-200, 20)
lance.goto(-200, -20)

# your code goes here
finish_line.down()
finish_line.right(90)
finish_line.forward(250)

for race in range(5):
    andy_distance = random.randrange(0, 100)
    lance_distance = random.randrange(0, 100)

    andy.forward(andy_distance)
    lance.forward(lance_distance)

wn.exitonclick()
