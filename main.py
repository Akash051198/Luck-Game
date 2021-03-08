print("welcome to the game of luck....")

name = input("what is your name: ")

age = int(input("what is your age? "))

if age >= 18:
  check =input("do you want to play [yes or no]? ").lower()

  if check == 'yes':

    print(f"welcome abord {name}...")
    print("you have initially 10 health during this game.")
    print("We will provide you tab as a guide as you progress")
    print("lets play..!")
    print("-------------------------------------------------")

    left_right=input("journey starts do you wanna go left or right.?").lower()

    if (left_right == "left"):
      print("your next checkpoint is near the lake...see ya!")
      print("-------------------------------------------------")
      print("its time to make next decision..")
      print("do you want to swim across the lake or take a boat[takes time to travel and you lose initially 5 points..] ")
      task1= input("").lower()
      if task1 == "swim":
        print("Oops you died..")
        print("Game over")
      elif task1 == "boat":
        print("nice choice but you boat is damaged hehehe..")
        print("-------------------------------------------------")
        print("check your toolbox and see if anything useful")
        task2 = input("choose wisely between the rope and flex tape: ").lower()
        if task2 == "rope":
          print("oops you died")
          print("Game over:(")
        elif task2 == "flextape":
          print("Wise decision.but you lost 3 health")
          print("you have 2 health remaining")
          print("-------------------------------------------------")
          print("Congrats you have reached the final part of game:")
          print("your last question...")
          task3= input("What do you choose a perfect antonym between win or lose ").lower()
          if task3 == "win":
            print("you lost Go learn English..")
            print("Gameover:(")
          elif task3 == "lose":
            print("Hooooray you won")


    elif (left_right == "right"):

      print("Oops wrong decision..Its the hardest path you will lose 3 health")
      print("you have 7 health remaining c.. choose you next decision wisely")
      print("your next checkpoint is near the swampy...see ya!")
      print("-------------------------------------------------")
      task4 = input("Do you want to run on swampland or walk across swampland" ).lower()
      if task4 == "run":
        print("Oops you died... ")
        print("Game over:(")

      elif task4 == "walk":
        print("wise decision but you lost 3 points of your health.. ")
        print("your next destination is near racetrack.. seeya")
        print("-------------------------------------------------")
        print("Welcome to the burnout paradise..you will pass-on next destination only if you beat the rider")
        task5= input("Choose between the red or blue bike..").lower()
        if task5 == "red":
          print("whoops the engine is in bad condition...BOOM! engine blown u died ")
          print("Game over:(")

        elif task5 == "blue":
          print("Do your best...!you will win")
          print("See you at finish lane...!")
          print("-------------------------------------------------")
          print("Congrats you have reached the final part of game:")
          print("your last question...")
          task6= input("What do you choose a perfect antonym between win or lose ").lower()
          if task6 == "win":
            print("you lost Go learn English..")
            print("Gameover:(")
          elif task6 == "lose":
            print("Hooooray you won")






  elif check == "no":
    print("buh byeee")



else:
  print("you are not allowed to play :( ")

  


