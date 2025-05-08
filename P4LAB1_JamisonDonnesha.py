import turtle

# Set up the screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):  
        my_turtle.forward(side_length)  
        my_turtle.right(90)  

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):  
        my_turtle.forward(side_length)  
        my_turtle.left(120)  

# Draw the square
my_turtle.penup()  
my_turtle.goto(-100, -50)  
my_turtle.pendown()  
draw_square(100)


my_turtle.penup()  
my_turtle.goto(0, 0)  
my_turtle.pendown()  
draw_triangle(100)  


turtle.done() 
