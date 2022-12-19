# Math Quiz by Sabir Mohammedi Taieb
import random

time = 0
score = 0
correctAns = 0
userSum = 0
print("# Math Quiz by Sabir Mohammedi Taieb \n")
print("Write -1 to exit.")
while (userSum != -1):
  n1 = random.randint(0, 100)
  n2 = random.randint(0, 100)

  print(n1, " + ", n2)
  userSum = input("Enter the sum of these two numbers: ")
  userSum = int(userSum)
  Sum = n1 + n2

  if (userSum == Sum):
    print("Correct")
    score += 1
  if (userSum == -1):
    break
  else:
    print("Wrong answer! Try again, the correct answer is: ", Sum)

print("\n your score is: ", correctAns)