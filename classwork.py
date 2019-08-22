### Problem 1:
#Create a program that prints the user input until they enter 'q' to quit.

#userInput = input("enter words or q to quit")
#while userInput != "q":
 #   print(userInput)
  #  userInput = input("enter words or q to quit")

### Problem 3:
#Create a program that takes user input in a while loop. If they enter 1, print 1. If they enter 2, print 2. If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.

#userInput = input( "enter 1, print 1 enter 2, print 2 enter 3 print 3. enter q or 0 to quit ")
#while userInput != "q" and userInput != "0":

 #   if userInput == "1":
   #     print(1)
  #  elif userInput == "2":
  #      print(2)
   # elif userInput == "3":
   #     print(3)
   # else:
  #      print("error")
 #   userInput = input( "enter 1, print 1 enter 2, print 2 enter 3 print 3. enter q or 0 to quit ")

## Problem 4:
#Create a program that takes the user input until they enter 'q'. You should store all of their input and separate the input with a comma. Once they enter 'q', print all of the comma separated words they entered.

userInput = input("enter words or q to quit")
total = ""
while userInput != "q":

    total = userInput + ", " + total
    userInput = input("enter words or q to quit")
print(total)

