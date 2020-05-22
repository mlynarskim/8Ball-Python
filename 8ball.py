import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def answers():
    answers = ["Prawdopodobnie","Tak", "Nie", "Oczywiście",
           "Absolutnie", "Nigdy w życiu", "Jeśli tylko chcesz", "Wykluczone",
           "W rzeczy samej", "Bardzo wątpliwe", "Możliwe", "Niewykluczone",
           "To nie wygląda zbyt dobrze", "Zapomnij o tym", "Nie teraz",
            "To musi poczekać"," Mam pewne wątpliwości", "Daj spokój",
            "Zrób to", "Na pewno tak", "TAK, TAK, TAK", "Tak - w swoim czasie"]
    messagebox.showinfo("Odpowiedź",answers[random.randint(0,len(answers)-1)])

self = Tk()
self.geometry("300x300")
self.resizable(0, 0)

self.title("8BALL")

image= tk.PhotoImage(file="8b.png")
image_ball= Label(self, image=image)
image_ball.pack()
image_ball.place(x=-50, y=50)

tk.Label(self, text="Zadaj mi pytanie").pack(padx=5, pady=5)
question = tk.Entry(self)
question.pack(padx=5, pady=2)

tk.Button(self, text="Enter", command=answers).pack(side=BOTTOM, pady=40)

tk.mainloop()



