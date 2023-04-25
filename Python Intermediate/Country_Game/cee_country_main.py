#This is the main program for nigeria country game
import turtle
import pandas
import time
 
varscreen = turtle.Screen()
varscreen.title("Nigeria_country_Game")
cee_image = "New_Nigeria_map.gif"
varscreen.addshape(cee_image)    #add shape to the variable defined screen
varscreen.setup(800,610)

# turtle.shape(cee_image) it should be found in the folder
turtle.shape(cee_image)
varscreen.tracer(100)

#defining the turtle time function
timeee = turtle.Turtle()
timeee.ht()
timeee.penup()
#defining the turtle score function
scoree = turtle.Turtle()
scoree.ht()
scoree.penup()
#to get the coordinates of points we click on the turtle screen
def get_mouse_on_click(x, y):
    print(x, y)

#accessing the csv file through panda
rate = pandas.read_csv("50_states.csv")
row_state = rate["states"].to_list()

#the turtle to write the state on the map
writing = turtle.Turtle()
writing.ht()
truth = turtle.Turtle()
truth.ht()

timeee.goto(350, 280)
timeee.pendown()
timeee.write("Timer-", align = "center", font = ("Comic Sans MS", 15, "bold"))
scoree.goto(-300, 280)
scoree.pendown()
scoree.write("Score-", align = "center", font = ("Comic Sans MS", 15, "bold"))
    
score = 0
guessed_state = []       
varsc = turtle.Turtle()
varsc.ht()
varsc.penup()
varsc.goto(350,250)
varsc.pendown()

answer_text = varscreen.textinput(title="Name: ", prompt="What's your name: ").title()        
Time = 90
running = True
def f():
    global Time
    global score
    global answer_text
    if Time > 0 and answer_text != "Exit":
        Time -= 1
        mod = int(Time / 60)
        moder = Time % 60
        varsc.clear()
        if mod < 10 and moder >= 10:
            varsc.write(f"0{mod}:{moder}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        elif mod < 10 and moder < 10:
            varsc.write(f"0{mod}:0{moder}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        else:
            varsc.write(f"{mod}:{moder}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        varscreen.ontimer(fun= f, t = 1800)
    elif Time == 0:
        rare = []
        for m in range(37):
            if row_state[m] not in guessed_state:
                rare.append(row_state[m])
        for m in rare:
            time.sleep(1)
            randname = rate[rate.states == m]
            x_x = randname["x"]
            print(x_x)
            xj = int(x_x)
            y_y = randname["y"]
            print(y_y)
            yj = int(y_y)
            writing.ht()
            writing.penup()
            writing.goto(xj,yj)
            writing.pendown()
            writing.color("white")
            writing.write(f"{m}", align = "center", font = ("Comic Sans MS", 10, "bold"))
        varscreen.clear()
        varscreen.bgcolor("black")
        writing.penup()
        writing.goto(0,0)
        writing.pendown()
        writing.write(f"Game Over\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
    elif answer_text == "Exit" or score == 37:
        pass
    

f()
running = False 
game = True    
while len(guessed_state) != 38: 
    if Time < 2:
        break
    answer_text = varscreen.textinput(title="Guess the State", prompt="What's another state name: ").title()
    if answer_text == "Exit":
        rare = []
        for m in range(37):
            if row_state[m] not in guessed_state:
                rare.append(row_state[m])
        print(rare)
        for m in rare:
            time.sleep(0.7)
            randname = rate[rate.states == m]
            x_x = randname["x"]
            print(x_x)
            xj = int(x_x)
            y_y = randname["y"]
            print(y_y)
            yj = int(y_y)
            writing.ht()
            writing.penup()
            writing.goto(xj,yj)
            writing.pendown()
            writing.color("white")
            writing.write(f"{m}", align = "center", font = ("Comic Sans MS", 10, "bold"))
        varscreen.clear()
        varscreen.bgcolor("black")
        writing.penup()
        writing.goto(0,0)
        writing.pendown()
        writing.write(f"Game Over\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        break
    if answer_text in row_state:
        guessed_state.append(answer_text)
        randname = rate[rate.states == answer_text]
        score += 1
        truth.clear()
        truth.ht()
        truth.penup()
        truth.goto(-300,250)
        truth.pendown()
        truth.write(f"{score}/37", align = "center", font = ("Comic Sans MS", 20, "bold"))
        #accessing the co-ordinate of the imputed state
        x_x = randname["x"]
        print(x_x)
        xj = int(x_x)
        y_y = randname["y"]
        print(y_y)
        yj = int(y_y)
        print(f"\n{randname}\n")
        writing.ht()
        writing.penup()
        writing.goto(xj,yj)
        writing.pendown()
        writing.write(f"{answer_text}", align = "center", font = ("Comic Sans MS", 10, "bold"))
    if score == 37:
        varscreen.clear()
        varscreen.bgcolor("black")
        writing.penup()
        writing.goto(0,0)
        writing.pendown()
        writing.color("white")
        writing.write(f"Game Over\nYou WIN!\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        break
        
varscreen.onscreenclick(get_mouse_on_click)
varscreen.mainloop()
