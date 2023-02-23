import turtle
import random
import time
from turtle import Turtle, Screen

rare = Screen()
rare.setup(width = 800, height = 600)
colours = ["pale violet red", "hot pink", "cornflower blue", "steel blue", "light sky blue", "violet", "pink"]
rare.bgcolor(random.choice(colours))
rare.title("Cee Ping Pong")
rare.listen()
rare.tracer(0)

user_1 = rare.textinput(title = "Cee PingPong!🦋", prompt = "What is your name?: ")
user_2 = rare.textinput(title = "Cee PingPong!🦋", prompt = "What is your name?: ")
User_1 = user_1
User_2 = user_2

walls = Turtle()
cent = Turtle()
cent.penup()
cent.ht()
cent.setheading(90)
cent.forward(80)
cent.pendown()
cent.setheading(180)
cent.forward(50)
cent.setheading(270)
cent.forward(160)
cent.setheading(0)
cent.forward(80)
cent.setheading(90)
cent.forward(160)
cent.setheading(180)
cent.forward(50)
walls.ht()
walls.penup()
walls.speed("fastest")
walls.pencolor("black")
walls.pensize(11)
walls.setheading(90)
walls.forward(300)
walls.setheading(180)
walls.pendown()
walls.forward(400)
walls.setheading(270)
walls.forward(590)
walls.setheading(0)
walls.forward(790)
walls.setheading(90)
walls.forward(590)
walls.setheading(180)
walls.forward(400)
walls.setheading(270)
walls.pencolor("white")
walls.pensize(7)
for _ in range(0, 11):
	walls.color("white")
	walls.speed(6)
	walls.forward(10)
	walls.penup()
	walls.forward(10)
	walls.pendown()
for _ in range(0, 8):
	walls.color("black")
	walls.speed(6)
	walls.forward(10)
	walls.penup()
	walls.forward(10)
	walls.pendown()
for _ in range(0, 11):
	walls.color("white")
	walls.speed(6)
	walls.forward(10)
	walls.penup()
	walls.forward(10)
	walls.pendown()

bar1 = Turtle()
bar1.shape("square")
bar1.shapesize(3, 1)
bar1.penup()
new_y = 0
bar1.goto(350, new_y)
bar2 = Turtle()
bar2.shape("square")
bar2.shapesize(3, 1)
bar2.penup()
new_b = 0
bar2.goto(-350, new_b)
ball = Turtle()
ball.shape("circle")
ball.shapesize(1, 1)

def forward1():
	global new_y
	new_y += 50
	bar1.penup()
	bar1.goto(bar1.xcor(), new_y)

def backward1():
	global new_y
	new_y -= 50
	bar1.penup()
	bar1.goto(bar1.xcor(), new_y)

def front():
	bar1.forward(50)

def back():
	bar1.backward(50)

def forward2():
	global new_b
	new_b += 50
	bar2.penup()
	bar2.goto(bar2.xcor(), new_b)

def backward2():
	global new_b
	new_b -= 50
	bar2.penup()
	bar2.goto(bar2.xcor(), new_b)

def front2():
	bar2.forward(50)

def back2():
	bar2.backward(50)

board = Turtle()
board.ht()
bord = Turtle()
bord.ht()
score1 = 0
score2 = 0
bard = Turtle()
win = Turtle()

def red():
	game_on = True
	x_move = 10
	y_move = 10
	tim = 0.09
	global score1
	global score2
	board.penup()
	board.goto(100, 150)
	board.color("white")
	board.write(f"{score1}", align = "center", font = ("Comic Sans MS", 80, "bold"))
	bord.penup()
	bord.goto(-100, 150)
	bord.color("white")
	bord.write(f"{score2}", align = "center", font = ("Comic Sans MS", 80, "bold"))
	while game_on:
		time.sleep(tim)
		rare.update()
		if ball.ycor() > 290 or ball.ycor() < -290: 
			y_move *= -1
		if ball.distance(bar1) < 30 and ball.xcor() > 50:
			board.clear()
			x_move *= -1
			tim *= 0.1
			score1 += 2
			board.penup()
			board.goto(100, 150)
			board.color("white")
			board.write(f"{score1}", align = "center", font = ("Comic Sans MS", 80, "bold"))
		if ball.distance(bar2) < 30 and ball.xcor() < -50:
			bord.clear()
			x_move *= -1
			tim *= 0.1
			score2 += 2
			bord.penup()
			bord.goto(-100, 150)
			bord.color("white")
			bord.write(f"{score2}", align = "center", font = ("Comic Sans MS", 80, "bold"))
		if ball.xcor() > 390:
			bard.penup()
			bard.goto(100, -200)
			bard.color("white")
			bard.write(f"MISS", align = "center", font = ("Comic Sans MS", 20, "bold"))
			ball.home()
			x_move *= -1
		if ball.xcor() < -390:
			bard.penup()
			bard.goto(-100, -200)
			bard.color("white")
			bard.write(f"MISS", align = "center", font = ("Comic Sans MS", 20, "bold"))
			ball.home()
			x_move = 10
			y_move = 10
		if score1 >= 90:
			win.color("white")
			win.write(f"{User_1} has won!", align = "center", font = ("Comic Sans MS", 20, "bold"))
			game_on = False
		if score2 >= 90:
			win.color("white")
			win.write(f"{User_2} has won!", align = "center", font = ("Comic Sans MS", 20, "bold"))
			game_on = False
		new_x = ball.xcor() + x_move
		new_y = ball.ycor() + y_move
		ball.penup()
		ball.goto(new_x, new_y)

rare.onkey(red, "space")
rare.onkey(forward1, "Up")
rare.onkey(backward1, "Down")
rare.onkey(front, "Left")
rare.onkey(back, "Right")
rare.onkey(forward2, "s")
rare.onkey(backward2, "x")
rare.onkey(front2, "c")
rare.onkey(back2, "z")

rare.exitonclick()
rare.update()