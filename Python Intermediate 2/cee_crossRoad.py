//
import turtle
import random
import time
from turtle import Turtle, Screen

var = Screen()
var.listen()
var.setup(width = 800, height = 800)
var.bgcolor("black")
var.tracer(0)

cars = Turtle()
road = Turtle()

y = 300
road.pensize(7)
road.pencolor("white")
road.setheading(270)
road.penup()
road.forward(y)
road.setheading(0)
road.forward(380)
road.setheading(180)
for _ in range(8):
	road.pendown()
	road.forward(50)
	road.penup()
	road.forward(50)
rady = True

while rady:
	if road.xcor() <= -380:
		roady = road.ycor()
		roady += 90
		road.goto(380, roady)
		for _ in range(8):
			road.pendown()
			road.forward(50)
			road.penup()
			road.forward(50)
	if road.ycor() >= 300:
		rady = False

per = Turtle()
per.shape("turtle")
per.color("white")
per.penup()
per.goto(0, -380)
per.setheading(90)
per.penup()

def forward():
	per.setheading(90)
	per.forward(20)
def backward():
	per.backward(20)
def right():
	per.setheading(0)
	per.forward(20)
def left():
	per.setheading(180)
	per.forward(20)

POSITION = [(500, -350), (500, -260), (500, -170), (500, -80), (500, 10), (500, 100), (500, 190), (500, 280)]
colours = ["pale violet red", "hot pink", "cornflower blue", "steel blue", "light sky blue", "violet", "pink"]
segment = []
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
board = Turtle()
board.color("white")
board.penup()
board.goto(300, 300)
boar = Turtle()
boar.color("white")
boar.penup()
boar.goto(-310, 350)
bor = Turtle()
bor.color("white")
bor.penup()
bor.goto(0, 350)
bor.ht()
board.ht()
boar.ht()
score = 0
tee = 60
rate = True
while rate:
	time.sleep(0.08)
	var.update()
	var.onkey(forward, "Up")
	var.onkey(backward, "Down")
	var.onkey(right, "Right")
	var.onkey(left, "Left")
	rand = random.randint(0, 6)
	num = 30
	tee -= 0.08
	ree = round(tee, 2)
	boar.clear()
	boar.write(f"{ree}seconds", align = "center", font = ("Comic Sans MS", 20, "bold"))
	if ree <= 0:
		rate = False
		board.clear()
		bor.write(f"Your final score is {score}", align = "center", font = ("Comic Sans MS", 15, "bold"))
	if rand == 1 or rand == 3:
		new_cars = Turtle("square")
		new_cars.shapesize(1, 2)
		new_cars.color(random.choice(colours))
		new_cars.penup()
		new_cars.setheading(180)
		new_cars.goto(random.choice(POSITION))
		segment.append(new_cars)
	for car in segment:
		car.forward(num)
		if per.distance(car) < 15:
			rate = False
			board.clear()
			bor.write(f"Your final score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
		if per.ycor() == 400 and score < 8:
			score += 2
			sad = random.randint(-300, 300)
			board.clear()
			board.write(f"{score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
			per.penup()
			per.goto(sad, -380)
			per.setheading(90)
			per.penup()
			num += 10
			car.forward(num)
		if per.ycor() == 400 and score == 8:
			var.clear()
			var.bgcolor("black")
			user_bet = var.numinput(title = "CEE", prompt = "Type 1 to move to next game: ")
			rad = int(user_bet)
			if rad == 1:
				import Cee_TurtleCrossRoad

var.exitonclick()