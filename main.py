from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
start_race = False
user_bet = screen.textinput("Place your bet", prompt="Which turtle will win the race? "
                                                     "Choose a color \n (red - green -yellow -"
                                                     "blue - indigo - violet)")
colors = ["red", "green", "yellow", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    start_race = True

winner = ""
while start_race:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            start_race = False
            winner = turtle.pencolor()
        distance = random.randint(0, 10)
        turtle.forward(distance)

if user_bet.lower() == winner.lower():
    print(f"You win. The winner is the {winner} turtle")
else:
    print(f"You loose! The winner is the {winner} turtle")

screen.exitonclick()
