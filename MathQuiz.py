# Math Quiz CLI by Sabir Mohammedi Taieb
import random
import time

#time = 0.0
score = 0
correctAns = 0
userSum = 0
#start = 0.0
#finish = 0.0
print("# Math Quiz CLI by Sabir Mohammedi Taieb \n")
print("Write -1 to exit.")

start = time.perf_counter()
while (userSum != -1):
  n1 = random.randint(0, 100)
  n2 = random.randint(0, 100)

  print(n1, " + ", n2)
  userSum = input("Enter the sum of these two numbers: ")
  userSum = int(userSum)
  Sum = n1 + n2

  if (userSum == Sum):
    print("Correct")
    correctAns += 1
  elif (userSum == -1):
    break
  else:
    print("Wrong answer! Try again, the correct answer is: ", Sum)

finish = time.perf_counter()
time = finish - start
score = correctAns - time/60
if(correctAns==0):
  score=0

print(f"\n Your time was: {time:0.2f} sec. Number of correct answers is:", correctAns, ". Your Score is: ",score)

input("\n Press Enter to exit ...")