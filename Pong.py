import turtle

wn = turtle.Screen()
wn.title("Pong by enise")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
#this is vision speed, not its own speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#pixels for movements
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0 PlayerB: 0", align="center", font=("Courier",24,"normal"))

# Functions

def paddle_a_up(): #coordinat y increases
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): #coordinat y decreases
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): #coordinat y increases
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down(): #coordinat y increases
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = int(-1)*float(ball.dy)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = int(-1)*float(ball.dy)
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx *= -1
    elif ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1



    # paddle and ball collisions

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
