import tkinter as tk
import random
import time

#time = 0.0
score = 0
correctAns = 0
userSum = 0
#start = 0.0
#finish = 0.0
# print("# Math Quiz by Sabir Mohammedi Taieb \n")
# print("Write -1 to exit.")

start = time.perf_counter()
# while (userSum != -1):
n1 = random.randint(0, 100)
n2 = random.randint(0, 100)

#   #print(n1, " + ", n2)
#   #userSum = input("Enter the sum of these two numbers: ")
#   userSum = int(userSum)
Sum = n1 + n2

#   if (userSum == Sum):
#     #print("Correct")
#     correctAns += 1
#   elif (userSum == -1):
#     break
#   else:
#     print("Wrong answer! Try again, the correct answer is: ", Sum)

finish = time.perf_counter()
time = finish - start
score = correctAns - time/60
if(correctAns==0):
  score=0

master = tk.Tk()
master.title("Math Quiz")
eans = tk.Entry(master)
eans.grid(row=1,column=1)
userSum = eans.get()
tk.Label(master, text=f"Enter the sum of {n1} and {n2}").grid(row=0)
tk.Label(master, text="Your Answer:").grid(row=1,column=0)
EnterBtn=tk.Button(text="Enter")
EnterBtn.grid(row=1,column=2)
StopBtn = tk.Button(text="Stop")
StopBtn.grid(row=1, column="3")
lscore=tk.Label(master, text="Hello")
lscore.grid(row=3)
EnterBtn.bind('<Enter>', lambda event: ansFunc())

def ansFunc():
  if(userSum == Sum):
    lanswer = tk.Label(master, text=f"Correct answer!")
    lanswer.grid(row=2)
    correctAns +=1
  else:
    lanswer = tk.Label(master, text=f"Wrong, The correct answer is: {Sum}")
    lanswer.grid(row=2)
  
my_text=f"Your time was: {time:0.2f} sec. Number of correct answers is: {correctAns} . Your Score is: {score}"
lscore.config(text=my_text)

master.mainloop()