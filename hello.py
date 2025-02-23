from cs50 import *

def main():
  x = get_int("enter number")
  y = get_int("enter 2nd number")
  print(x/y)




def get_int(prompt):
 while True:
     try:
      return int(input(prompt))
     except ValueError:
      print("Error!")
           
      

main()



