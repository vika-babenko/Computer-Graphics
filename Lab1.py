from tkinter import *
import matplotlib.pyplot as plt

root = Tk()

fig = plt.figure()

def show():
    plt.scatter(3, 4, color="black")
    plt.show()

root.title("Комп'ютерна графіка. Лабораторна робота 1")
root.geometry("300x200")

name = Label(root, text="ПІБ: Бабенко Вікторія", font=("Arial", 14))
name.grid(row=0, column=0)
group = Label(root, text="Група: ІВ-92", font=("Arial", 14))
group.grid(row=1, column=0)
nzk = Label(root, text="Номер залікової книжки : 9201", font=("Arial", 14))
nzk.grid(row=2, column=0)
number_in_group = Label(root, text="Номер у списку групи : 1", font=("Arial", 14))
number_in_group.grid(row=3, column=0)

show_dot = Button(root, text="Показати точку на графіку", command=show)
show_dot.grid(row=4, column=0)
root.mainloop()