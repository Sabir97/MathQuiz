# Math Quiz by Sabir Mohammedi Taieb
import random

userSum = 0
print("# Math Quiz by Sabir Mohammedi Taieb")

while (userSum != -1):
  n1 = random.randint(0, 100)
  n2 = random.randint(0, 100)

  print(n1, " + ", n2)
  userSum = input("Enter the sum of these two numbers: ")
  userSum = int(userSum)
  Sum = n1 + n2

  if (userSum == Sum):
    print("Correct")
  else:
    print("Wrong answer! Try again, the correct answer is: ", Sum)
