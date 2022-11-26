from turtle import ManualTurtle
from random import randint

# initialise game board
destination = [randint(0, 50), randint(0, 50)]
user_turtle = ManualTurtle()

print(f"The destination is {destination}.")

# main game loop
while destination != user_turtle.location:
  user_turtle.navigate_to_dest()

print(f"You've won! The turtle reached {destination}.")