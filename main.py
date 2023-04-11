# CODING CHALLENGE TRASURE ISLAND
print("Welcome to Treasure Island. Your mission is to find the treasure")

choice1 = input('You\'re at a crossroad, where do you want to go? "left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake, There is an Island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
    if choice3 == "red":
      print("You ain't win shit bitch")
    elif choice3 == "yellow":
      print("Yes family. You did it!")
    elif choice3 == "blue":
      print("all your opps just found you. g'luck")
    else:
      print(" lol you chose an imaginary door lmao foh")
  else:
    print("Dayum! You got eaten by whole whale..")
else:
  print("LMAO Your dumbass just fell into a ditch bitch")