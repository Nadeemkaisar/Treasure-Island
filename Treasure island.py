print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Step1 = input(
    "You are at step 1 and from here there are two ways left or right.Where do u want to go?\n")
if Step1.lower() == "left":
    print("Well done welcome to the second step")
elif Step1.lower() == "right":
    print("Game over")
Step2 = input("Ok now you have reached the end area of island and now you have to cross river to go to other side you have two option 1.wait for boat or 2.Swim across the river. So choose wait or swim.\n")
if Step2.lower() == "wait":
    print("Sorry times up.You lost")
elif Step2.lower() == "swim":
    print("Good you reached other side.Well done!")
Step3 = input("Since you made it so far and for the last round you reached a house with 3 gates red,blue,yellow.So choose among these colors.\n")
if Step3.lower() == "red":
    print("Sorry the room is full of snakes you lost")
elif Step3.lower() == "blue":
    print("Congratulations.You have won the game.")
elif Step3.lower() == "yellow":
    print("Sorry the room is full of lions.You lost")
