#Simple pong game like baby table tennis
#Turtle is  simplest and in-built but you can install pygames


import turtle
wn=turtle.Screen()
wn.title('Pong by Kerry')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)
#he claims tis will make your game run much faster and does not make your window be updated

paddle_a=turtle.Turtle()
paddle_a.shape('square')
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


paddle_b=turtle.Turtle()
paddle_b.shape('square')
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


ball=turtle.Turtle()
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)




#Every game must have a main game loop
while True:
     wn.update()