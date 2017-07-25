import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(5)
  


    blake = turtle.Turtle()
    blake.shape("circle")
    blake.color("white")
    blake.speed(5)

    blake.forward(100)
    blake.right(80)
    blake.forward(100)
    blake.right(90)
    blake.forward(100)
    blake.right(90)
    blake.forward(100)
    blake.right(90)
    blake.forward(100)
    
    

    window.exitonclick()

draw_square()
