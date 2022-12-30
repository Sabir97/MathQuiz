import tkinter as tk

master = tk.Tk()

tk.Label(master, text="Enter the sum of ").grid(row=0)
tk.Label(master, text="Your Answer:").grid(row=1)
eans = tk.Entry(master)
eans.grid(row=1,column=1)

master.mainloop()
