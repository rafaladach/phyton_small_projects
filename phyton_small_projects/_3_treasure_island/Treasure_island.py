level1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if level1 == "left":
  level2 = input("You went over the lake. Do you want to swim or wait?\n").lower()
  if level2 == "wait":
    level3 = input("You are in front of the castle doors. Which doors do you choose(red, yellow, blue)?\n").lower()
    if level3 == "yellow":
      print("YOU WIN!")
    elif level3 == "red":
      print("Sodiers captured you! They put you into the cannon and fire you above mountains!")
      print("GAME OVER")
    elif level3 == "blue":
      print("You got into the gold room full of treasures, but the Yeti stands before it. Yegi Smashed you with Big Blue Foot!")
      print("GAME OVER")
    else:
      print("You fell asleep because you chose no door!")
      print("GAME OVER")
  else:
    print("You have been attacked! Big white bear eats you!")
    print("GAME OVER")
else:
  print("You have lost in forest and died from hunger!")
  print("GAME OVER")