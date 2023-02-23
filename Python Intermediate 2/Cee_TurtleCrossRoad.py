import turtle
import random
import time
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 900, height = 900)
screen.tracer(0)
screen.title("Cee Snake Game")
screen.listen()
colours = ["pale violet red", "hot pink", "cornflower blue", "steel blue", "light sky blue", "violet", "pink"]

wall = Turtle()
wall.color("white")
wall.shape("turtle")
wall.pencolor(random.choice(colours))
wall.pensize(15)
wall.speed("fastest")
wall.penup()
wall.backward(440)
wall.setheading(270)
wall.pendown()
wall.forward(430)
wall.setheading(0)
wall.forward(870)
wall.setheading(90)
wall.forward(870)
wall.setheading(180)
wall.forward(870)
wall.setheading(270)
wall.forward(350)
wall.penup()
wall.forward(30)
wall.setheading(0)
wall.forward(90)
wall.pendown()
wall.setheading(90)
wall.forward(320)
wall.setheading(0)
wall.forward(100)
wall.setheading(270)
wall.forward(250)
wall.setheading(0)
wall.penup()
wall.forward(90)
wall.setheading(0)
wall.pendown()
wall.forward(120)
wall.setheading(90)
wall.forward(145)
wall.setheading(180)
wall.forward(70)
wall.setheading(90)
wall.forward(90)
wall.setheading(0)
wall.forward(200)
wall.setheading(270)
wall.forward(320)
wall.setheading(180)
wall.forward(280)
wall.setheading(270)
wall.forward(70)
wall.setheading(180)
wall.forward(150)
wall.setheading(270)
wall.forward(305)
wall.setheading(0)
wall.forward(670)
wall.setheading(90)
wall.forward(670)
wall.setheading(180)
wall.forward(150)
wall.setheading(0)
wall.forward(45)
wall.setheading(270)
wall.forward(570)
wall.setheading(180)
wall.forward(470)
wall.setheading(90)
wall.forward(100)
wall.setheading(270)
wall.forward(100)
wall.setheading(0)
wall.forward(235)
wall.setheading(90)
wall.forward(150)
wall.setheading(0)
wall.forward(65)
wall.setheading(180)
wall.forward(130)

wall.ht()
screen.update()


shawn = Turtle()
shawn.penup()
shawn.shape("circle")
shawn.penup()
shawn.shapesize(0.5, 0.5)
shawn.color("white")
shawn.speed("fastest")
random_x = random.randint(-430, 430)
random_y = random.randint(-430, 430)
shawn.goto(random_x, random_y)

def refresh():
	random_x = random.randint(-430, 430)
	random_y = random.randint(-430, 430)
	shawn.goto(random_x, random_y)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_pos:
	new_segment = Turtle("square")
	new_segment.color(random.choice(colours))
	new_segment.penup()
	new_segment.goto(position)
	segments.append(new_segment)

def add():
	nt = Turtle("square")
	nt.color(random.choice(colours))
	nt.penup()
	segments.append(nt)

board = Turtle()
board.color("white")
board.ht()
board.penup()
board.goto(0, 360)
board.write("If your food is on a wall, then that's a death food! \nClick space to start and move forward\n And arrow keys to move in their respective directions.!", align = "center", font = ("Courier New", 14, "normal"))
board.goto(0, 410)

score = 0
def red():
	game_on = True
	while game_on:
		global score
		screen.update()
		time.sleep(0.1)
		for seg in range(len(segments) - 1, 0, -1):
			new_x = segments[seg - 1].xcor()
			new_y = segments[seg - 1].ycor()
			segments[seg].goto(new_x, new_y)
		if segments[0].distance(shawn) < 17:
			refresh()
			score += 1
			board.clear()
			board.write(f"YOUR CURRENT SCORE IS : {score}")
			add()
		segments[0].forward(10)
		if segments[0].xcor() > 430 or segments[0].xcor() == -430 or segments[0].ycor() == 430 or segments[0].ycor == -430:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == 330 and segments[0].ycor() >= -330 and segments[0].ycor() <= 335:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == 220 and segments[0].ycor() >= -230 and segments[0].ycor() <= 335:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -350 and segments[0].ycor() <= 380 and segments[0].ycor() >= 50:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -340 and segments[0].ycor() >= -330 and segments[0].ycor() <= -30:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -240 and segments[0].ycor() <= 380 and segments[0].ycor() >= 120:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -250 and segments[0].ycor() >= -230 and segments[0].ycor() <= -120:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -190 and segments[0].ycor() >= -30 and segments[0].ycor() <= 50:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -30 and segments[0].ycor() <= 260 and segments[0].ycor() >= 120:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == -10 and segments[0].ycor() >= -220 and segments[0].ycor() <= -80:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].xcor() == 90 and segments[0].ycor() <= 370 and segments[0].ycor() >= 50:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == 380 and segments[0].xcor() >= -340 and segments[0].xcor() <= -240:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == 370 and segments[0].xcor() >= -100 and segments[0].xcor() <= 90:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == 260 and segments[0].xcor() >= -90 and segments[0].xcor() <= -30:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == 130 and segments[0].xcor() >= -150 and segments[0].xcor() <= -30:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == 40 and segments[0].xcor() >= -200 and segments[0].xcor() <= 90:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == -20 and segments[0].xcor() <= -200 and segments[0].xcor() >= -340:
			game_on = False
			board.goto(-385, 0)
			board.write(f"Game Over! Your final score is {score}")
		if segments[0].ycor() == -330 and segments[0].xcor() >= -340 and segments[0].xcor() <= 320:
			game_on = False
			board.goto(-385, 0)
			board.write(f"GAME OVER! YOUR FINAL SCORE IS {score}")
		if segments[0].ycor() == -220 and segments[0].xcor() >= -250 and segments[0].xcor() <= 220:
			game_on = False
			board.goto(-385, 0)
			board.write(f"GAME OVER! YOUR FINAL SCORE IS {score}")
		if segments[0].ycor() == -80 and segments[0].xcor() >= -75 and segments[0].xcor() <= 75:
			game_on = False
			board.goto(-385, 0)
			board.write(f"GAME OVER! YOUR FINAL SCORE IS {score}")
		if segments[0].ycor() == 340 and segments[0].xcor() >= 180 and segments[0].xcor() <= 320:
			game_on = False
			board.goto(-385, 0)
			board.write(f"GAME OVER! YOUR FINAL SCORE IS {score}")
		if segments[0].xcor() == -110 and segments[0].ycor() <= 370 and segments[0].ycor() >= 260:
			game_on = False
			board.goto(-385, 0)
			board.write(f"GAME OVER! YOUR FINAL SCORE IS {score}")
		for segment in segments[1:]:
			if segments[0].distance(segment) < 5:
				game_on = False
				board.goto(-385, 0)
				board.write(f"YOU BIT YOURSELF. GAME OVER! YOUR FINAL SCORE IS {score}") 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def blue():
		screen.update()
		for seg in range(len(segments) - 1, 0, -1):
			new_x = segments[seg - 1].xcor()
			new_y = segments[seg - 1].ycor()
			segments[seg].goto(new_x, new_y)
		if segments[0].heading() != DOWN:
			segments[0].setheading(UP)

def green():
		screen.update()
		for seg in range(len(segments) - 1, 0, -1):
			new_x = segments[seg - 1].xcor()
			new_y = segments[seg - 1].ycor()
			segments[seg].goto(new_x, new_y)
		if segments[0].heading() != RIGHT:
			segments[0].setheading(LEFT)

def pink():
		screen.update()
		for seg in range(len(segments) - 1, 0, -1):
			new_x = segments[seg - 1].xcor()
			new_y = segments[seg - 1].ycor()
			segments[seg].goto(new_x, new_y)
		if segments[0].heading() != UP:
			segments[0].setheading(DOWN)

def orange():
		screen.update()
		for seg in range(len(segments) - 1, 0, -1):
			new_x = segments[seg - 1].xcor()
			new_y = segments[seg - 1].ycor()
			segments[seg].goto(new_x, new_y)
		if segments[0].heading() != LEFT:
			segments[0].setheading(RIGHT)

screen.onkey(red, "space")
screen.onkey(blue, "Up")
screen.onkey(green, "Left")
screen.onkey(pink, "Down")
screen.onkey(orange, "Right")