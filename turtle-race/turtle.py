class Turtle:

  # Initialise the instance of the class.
  # If there isn't a pre-set starting location, we have a default of [0,0]
  def __init__(self, starting_location=[0, 0]):
    self.location = starting_location

  # Movement methods. These are "private" because of the underscore, indicating they should not be called directly
  # this is just convention for programmers, like a flag that says... Please don't use this method manually. You can still do it.
  # Other languages like Java can prevent this entirely.
  # This code is not very DRY. Could abstract it out into '_move' and take an axis.
  def _up(self, step=1):
    self.location[1] += step

  def _down(self, step=1):
    self.location[1] -= step

  def _right(self, step=1):
    self.location[0] += step

  def _left(self, step=1):
    self.location[0] -= step

  # Navigation method. The default is that the Turtle automatically walks towards the destination one unit at a time
  def navigate_to_dest(self, destination):
    while self.location != destination:
      if destination[0] > self.location[0]:
        self._right()
      elif destination[0] < self.location[0]:
        self._left()
      elif destination[1] > self.location[1]:
        self._up()
      elif destination[1] < self.location[1]:
        self._down()

    print(f"New location: {self.location}")
    return self.location


# A class that EXTENDS the Turtle class above. This means it has all the same methods.
class ManualTurtle(Turtle):

  # A new function to handle the special case of user input.
  def _navigate_with_input(self):
    # Take input from user. Allow for a step to be inputted
    while True:
      user_input = input(
        f"Turtle is at {self.location}. Move where? \n [U]p / [D]own / [L]eft / [R]ight {{step}} \n -> "
      ).lower().split()

      # If the user hasn't input a step, default to 1.
      if len(user_input) != 2:
        step = 1
      else:
        step = user_input[1]
        # If they have input not a digit, we reset to top of while loop.
        if not step.isdigit():
          continue
        step = int(step)

      # Grab the first string input
      # If the direction isn't a u, d, l or r character, we reset to top of while loop.
      direction = user_input[0]
      if direction not in 'udlr':
        continue
      else:
        break

    # Now we call the movement methods.
    if direction == 'u':
      self._up(step)
    elif direction == 'd':
      self._down(step)
    elif direction == 'l':
      self._left(step)
    elif direction == 'r':
      self._right(step)

  # I have overridden the Turtle navigate_to_dest function that I get from inheritance.
  def navigate_to_dest(self):
    self._navigate_with_input()
