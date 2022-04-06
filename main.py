from datetime import date
import time


today = date.today()
d1 = today.strftime("%B %d, %Y")
print("Welcome, What's your name? ")
user_name = input()
print("Okay", user_name, "Do you want to learn date? yes/no " )
answer = input() 
if answer == "yes":
  print("Today is: ", d1)
else:
  print("Ok,", user_name, "what do you wanna know please type in ...")
  type_in = input()
  time.sleep(3)
  print("I'm thinking")
  time.sleep(3)
  print("I'm still thinking")
  time.sleep(3)
  print("Hmmm")
  time.sleep(5)
  print(user_name, "I think we're stuck in a loop! ")

