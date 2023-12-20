import turtle

turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
      for colours in ["red","blue","green","blue","red","green"]:
               turtle.color(colours)
               turtle.circle(100)
               turtle.left(20)

turtle.done()
