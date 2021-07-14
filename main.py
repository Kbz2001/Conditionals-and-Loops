# Warm up
#--------------------------------------
# Get first and last name as user input.
# Print the name is reverse order. (Ex. Kile Zimmermann -> Zimmermann Kile)

# Loops
#--------------------------------------
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# Boolean operators
#------------------

# Comparison Operators
# let x = 3
# x < 5 (Less than) True
# x > 5 (Greater than) False
# let x = 5
# x <= 5 (Less than or equal to) True
# x >= 5 (Greater than or equal to) True
# x == 5 (Equality) True
# x != 5 (Not equal to) False

# Logical Operators
# let x = 5 and y = 5
# and if x is 5 and if y is 5 True
# let x = 5 and y = 6
# if x is 5 and if y is 5 False
# or
# let x = 5 and y = 6
# if x is 5 or if y is 5 True
# if x is 8 or if y is 5 False
# not
# let x = 5
# if x is not 5 False
# if x is not 7 True

# While Loop
# While loop takes in a boolean expression (T/F)
# A while loop will only run if the boolean expression is true

# Infinite loop ! Watch out for these !
# counter = 0
# while(counter <= 5):
#   print(counter)

# counter = 0
# while(counter < 5):
#   print(counter + 1)
#   counter = counter + 1

# For Loops
# counter = 0
# for counter in range(5):
#   print(counter + 1)

# range(5) => 0, 1, 2, 3, 4.
# range(0, 5) => 0, 1, 2, 3, 4
# The range function is inclusive for the left parameter and exclusive for the right parameter.
# counter = 0
# for counter in range(2, 5):
#   print(counter + 1)

# # List of numbers
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for value in numbers:
#   sum = sum + value
# print(sum)
# Get the sum of all the numbers. Final answer should be 15
#--------------------------------

# Conditionals
#--------------------------------
# Definition: if x then y
# Ex. if I go to school then I learn
# Ex. if I go to the resurant then I will eat 
# Ex. if I drink and drive I will get into an accident.

# if statements are used for decision making. If statements only run if the boolean expression is true.

# Template: if <boolean expression>:
# Template: else
# money = 5
# if money == 5:
#   print("I have 5 dollars!")
#   money = 10
#   if money == 10:
#     print("I gained 5 more dollars!")
# elif money == 6:
#   print("I have 6 dollars!")
# elif money == 7:
#   print("I have 7 dollars!")
# else:
#   print("I have a different amount of money!")

# Different Seasons Activity
# Winter, Spring, Summer, Fall
# Depending on what season the user says it is, we want to tend to our garden.
# Winter: print => stay inside
# Spring: print => plant trees
# Summer: print => water trees
# Fall: print => pick apples

# season = input("What season is it? ")

# Guess the Number Project

import random

computerNumber = random.randint(0,10)
numberOfTries = 5
Win = False
Play = True

while Play == True:
  while numberOfTries > 0:
    playerNumber = input("Enter a number between 0-10:")
    playerNumber = int(playerNumber)
    
      # Handle user guessing the number
      # if the number is too big
      # if the number is too small
      # if the number is correct

    if playerNumber > 10 or playerNumber < 0:
       print("Bad Number")
       break
    else:
      if playerNumber > computerNumber:
        print("Number is too big")
        numberOfTries = numberOfTries - 1
        print("You have " + str(numberOfTries) + " tries left")
      elif playerNumber < computerNumber:
        print("Number is too small")
        numberOfTries = numberOfTries - 1
        print("You have " + str(numberOfTries) + " tries left")
      else:
        print("You got the correct number!")
        Win = True
        break
  if Win == True:
    print("Congrats you won at " + str(numberOfTries) + " tries")
  else:
    print("Out of Tries")
    print("The number was " + str(computerNumber))
    break

  answer = input("Do you want to play again? (Y/N)")
  if answer.upper() == "N":
    print("Bye bye!")
    Play = False
  else:
    Win = False
    numberOfTries = 5 
# Remember to always push your final project to GitHub!