'''
file: driver.py
author: Alex Giang
class: CS550 Artificial Intelligence
'''
from boardtypes import TileBoard

up = [-1,0]
down = [1,0]        
left = [0,-1]
right = [0,1]
none = [0,0]

tileBoard = TileBoard(8);
tileBoard.get_actions() # need this for location of empty tile

print("Tile Game Start: ")
print("To move the blank tile: Type 'left', 'right', 'up', or 'down'")
print("To leave game: Type 'stop' or 'exit'")
print(tileBoard.__repr__())

while not tileBoard.solved():
    # lists available actions for the player
    actions = tileBoard.get_actions()
    actionList = []
    for i in range(len(actions)): 
        if actions[i] == left:
            actionList.append("left")
        if actions[i] == right:
            actionList.append("right")
        if actions[i] == up:
            actionList.append("up")
        if actions[i] == down:
            actionList.append("down")
    print("Available Actions: ")
    print(actionList)
    # takes input from player 
    count = 0
    while not count == 1:
        user = input()
        if user in actionList and user == "left":
            temp = tileBoard.move(left)
            count += 1
        if user in actionList and user == "right":
            temp = tileBoard.move(right)
            count += 1
        if user in actionList and user == "up":
            temp = tileBoard.move(up)
            count += 1
        if user in actionList and user == "down":
            temp = tileBoard.move(down)
            count += 1
        if user == "stop" or user == "exit":
            print("Better luck next time")
            exit()
        if user not in actionList:
            print("Please try another move.")        
    print(temp)
    tileBoard = temp

print("Congrats! You've solved it!")


