import time
import os
import keyboard
from random import choice

def GameOver(score):
    print("Game Over!")
    print(f"Score: {score}")
    print("Press the R key to retry or Q to quit.")
    while True:
        if keyboard.is_pressed("R"):
            GameLoop()
            return
        if keyboard.is_pressed("Q"):
            quit()

def CreateNewFood(foodLocation, gameBoard, locations):
    if len(foodLocation) == 2:
        foodLocation.pop()
        foodLocation.pop()
    foodLocation.append(choice([i for i in range(0, 20) if i not in locations[0]]))
    foodLocation.append(choice([i for i in range(0, 20) if i not in locations[1]]))
    gameBoard[foodLocation[0]][foodLocation[1]] = '●'
    return foodLocation, gameBoard

def GameLoop():
    score = 1
    xLocation = 8
    yLocation = 8
    locations = [[yLocation],[xLocation]]
    foodLocation = []
    lastinput = "right"
    gameSpeed = .1
    row = ['□'] * 20
    gameBoard = []

    for i in range(20):
        gameBoard.append(row[:])

    while True:
        # Get input
        if keyboard.is_pressed("up") and lastinput != "down":
            lastinput = "up"
        elif keyboard.is_pressed("down") and lastinput != "up":
            lastinput = "down"
        elif keyboard.is_pressed("left") and lastinput != "right":
            lastinput = "left"
        elif keyboard.is_pressed("right") and lastinput != "left":
            lastinput = "right"
        if lastinput == "up":
            yLocation -= 1
        elif lastinput == "down":
            yLocation += 1
        elif lastinput == "left":
            xLocation -= 1
        elif lastinput == "right":
            xLocation += 1
        
        # Check if new snake position is off screen
        if xLocation < 0 or xLocation > 19 or yLocation < 0 or yLocation > 19:
            GameOver(score)
            return

        # Check if new snake position collides with itself
        for i in range(len(locations[0])):
            if yLocation == locations[0][i] and xLocation == locations[1][i]:
                GameOver(score)
                return

        # Remove last snake position
        gameBoard[locations[0][0]][locations[1][0]] = '□'
        locations[0].pop(0)
        locations[1].pop(0)

        # Store current snake position in locations list
        locations[0].append(yLocation)
        locations[1].append(xLocation)
        for i in range(len(locations[0])):
            gameBoard[locations[0][i]][locations[1][i]] = '■'

        # Add in food if food array is empty
        if not foodLocation:
            foodLocation, gameBoard = CreateNewFood(foodLocation, gameBoard, locations)
        # Check if new snake position and food location are the same
        if yLocation == foodLocation[0] and xLocation == foodLocation[1]:
            foodLocation, gameBoard = CreateNewFood(foodLocation, gameBoard, locations)
            locations[0].append(yLocation)
            locations[1].append(xLocation)
            score += 1

        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the game board
        for i in gameBoard:
            print(" ".join(i))


        # Pause program
        time.sleep(gameSpeed)

GameLoop()