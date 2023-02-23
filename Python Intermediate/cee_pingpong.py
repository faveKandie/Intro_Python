import turtle
import random
import time
from turtle import Turtle, Screen

var = Screen()
var.setup(width = 800, height = 600)
colours = ["pale violet red", "hot pink", "cornflower blue", "steel blue", "light sky blue", "violet", "pink"]
var.bgcolor(random.choice(colours))
var.title("Cee Ping Pong")
var.listen()
var.tracer(0)

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
wall = Turtle()
wall.ht()
wall.penup()
wall.speed("fastest")
wall.pencolor("black")
wall.pensize(11)
wall.setheading(90)
wall.forward(300)
wall.setheading(180)
wall.pendown()
wall.forward(400)
wall.setheading(270)
wall.forward(590)
wall.setheading(0)
wall.forward(790)
wall.setheading(90)
wall.forward(590)
wall.setheading(180)
wall.forward(400)
wall.setheading(270)
wall.pencolor("white")
wall.pensize(7)
for _ in range(0, 12):
	wall.color("white")
	wall.speed(6)
	wall.forward(10)
	wall.penup()
	wall.forward(10)
	wall.pendown()
for _ in range(0, 6):
	wall.color("black")
	wall.speed(6)
	wall.forward(10)
	wall.penup()
	wall.forward(10)
	wall.pendown()
for _ in range(0, 12):
	wall.color("white")
	wall.speed(6)
	wall.forward(10)
	wall.penup()
	wall.forward(10)
	wall.pendown()

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
score1 = 0
score2 = 0

def red():
	game_on = True
	x_move = 10
	y_move = 10
	global score1
	global score2
	while game_on:
		time.sleep(0.09)
		var.update()
		if ball.ycor() > 290 or ball.ycor() < -290: 
			y_move *= -1
		if ball.distance(bar1) < 30 and ball.xcor() > 50:
			board.clear()
			x_move *= -1
			score1 += 2
			board.penup()
			board.goto(100, 150)
			board.color("white")
			board.write(f"{score1}", align = "center", font = ("Comic Sans MS", 80, "bold"))
		if ball.distance(bar2) < 30 and ball.xcor() < -50:
			board.clear()
			x_move *= -1
			score2 += 2
			board.penup()
			board.goto(-100, 150)
			board.color("white")
			board.write(f"{score2}", align = "center", font = ("Comic Sans MS", 80, "bold"))
		if ball.xcor() > 390:
			board.penup()
			board.goto(300, 200)
			board.ht()
			ball.home()
			x_move *= -1
		if ball.xcor() < -390:
			board.penup()
			board.goto(-300, 200)
			board.ht()
			ball.home()
			x_move = 10
			y_move = 10
		new_x = ball.xcor() + x_move
		new_y = ball.ycor() + y_move
		ball.penup()
		ball.goto(new_x, new_y)

var.onkey(red, "space")
var.onkey(forward1, "Up")
var.onkey(backward1, "Down")
var.onkey(front, "Left")
var.onkey(back, "Right")
var.onkey(forward2, "d")
var.onkey(backward2, "a")
var.onkey(front2, "b")
var.onkey(back2, "c")

var.exitonclick()
