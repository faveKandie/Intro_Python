import turtle 

# row_state = ['abia', 'adamawa', 'akwaibom', 'anambra', 'bauchi', 'bayelsa', 'benue', 'borno', 'crossriver']

# answer_text = input("mention a state: ")

# for n in row_state:
    # if answer_text == n:
        # print(f"{answer_text}. Yayy!")
        
# ella = "Hello"
# ela = "uju"
# print(ella + ela)

varscreen = turtle.Screen()
varscreen.title("cee_country_Game")
varscreen.setup(800,610)
varsc = turtle.Turtle()

running = True
def f():
    varsc.forward(50)
    varscreen.bgcolor("pink")
    varscreen.ontimer(fun= f, t = 2500)
f()
running = False
varscreen.mainloop()