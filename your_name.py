# This program takes place in the wild west   <<---- this line is a comment. Comments start with a '#'

import time     # <<-- here, we are telling the program to use some code someone else has written for us to do a task

bullets=6       # <<-- this is our first variable. It's of type 'int' (or integer)

print("\n" * 10)   # <<-- Here, we're printing 10 'new lines', just to clear the screen out a bit

your_name = input("Howdy! What's your name, stranger? ")     #<<-- this line asks the user to input some information, which is stored in a variable called 'your_name'


#   The code that you see next is an 'IF' statement.
#   It's evaluating the value of the your_name variable.
#   If you don't enter anything, then the code does somenthing different 
#   Note that you MUST indent your code to show it as a block, 3 spaces is the norm.

if your_name !="":

   print("\n Real swell to meet you, " + your_name)

else:

  print("\n Not talkin' eh?")
  your_name = "Old Billy No-Name"     # <<-- when you've run the code a few times, see what happens if you remove the indent on this line

time.sleep(2)         # <<-- this is a sleep timer. We've not had to write the code for this.

print("\n Now dance!!!")

time.sleep(1)


# next comes a 'WHILE' loop, which loops while the cowboy has bullets in his gun....
# again, you MUST indent the code in the WHILE block.

while bullets > 0:
   print(" " * bullets + "BANG!!")
   time.sleep(0.5)
   bullets = bullets - 1

time.sleep(2)
print("How d'ya like that, " + your_name + "?")
time.sleep(0.5)
print("\n Now get outta town!")
print("\n" * 3)

time.sleep(5)
