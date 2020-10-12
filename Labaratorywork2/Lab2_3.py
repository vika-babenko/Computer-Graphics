from tkinter import *
import numpy as np
import time
import matplotlib.pyplot as plt
import math
# переміщення трикутника
def move_figure():
    global window1
    if window1 is None:
        # координати
        x1 = 0
        y1 = 0
        x2 = 30
        y2 = 60
        x3 = 60
        y3 = 60

        # за допомгою скалярних обчислень реалізуємо переміщення
        for i in [5, 10, 15, 20]:
            x1 = x1 + 5
            x2 = x2 + 5
            x3 = x3 + 5
            y1 = y1 + 5
            y2 = y2 + 5
            y3 = y3 + 5
            plt.plot([x1, x2, x3, x1],[y1, y2, y3, y1])

        plt.show()
    else:
        window1.destroy()
        window1 = None

# обертання фігури(трикутника)
def rotate_figure():
    global window2
    if window2 is None:
        # координати
        x1 = 0
        y1 = 0
        x2 = 30
        y2 = 60
        x3 = 60
        y3 = 60
        # за допомою матриці з напрямними косинусами реалізуємо обертання
        for i in [0.5, 0.25, 0.125, 0.625, 0.8]:
            plt.plot([x1 * math.cos(i) + y1 * math.sin(i), x2 * math.cos(i) + y2 * math.sin(i),
                      x3 * math.cos(i) + y3 * math.sin(i), x1 * math.cos(i) + y1 * math.sin(i)],
                     [-x1 * math.sin(i) + y1 * math.cos(i), -x2 * math.sin(i) + y2 * math.cos(i),
                      -x3 * math.sin(i) + y3 * math.cos(i), -x1 * math.sin(i) + y1 * math.cos(i)])

        plt.show()


    else:
        window2.destroy()
        window2 = None

# масштабування
def size_figure():
    global window3
    if window3 is None:
        # координати
        x1 = 0
        y1 = 0
        x2 = 30
        y2 = 60
        x3 = 60
        y3 = 60
        # реалізація масштабування з введенням коефіцієнту масштабування - константи
        for i in [5, 10, 15, 20]:
            x1 = 1.5*x1
            x2 = 1.5*x2
            x3 = 1.5*x3

            y1 = 1.5*y1
            y2 = 1.5*y2
            y3 = 1.5*y3

            plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])

        plt.show()

    else:
        window3.destroy()
        window3 = None


root = Tk()
# глобальні змінні
window1 = None
window2 = None
window3 = None
# кнопки та надписи
task1_label = Label(root, text="Виконання першого завдання - скалярні обчислення(Matplotlib)")
move_button = Button(root, text="Переміщення трикутника", command=move_figure)
rotate_button = Button(root, text="Обертання трикутника", command=rotate_figure)
size_button = Button(root, text="Масштабування трикутника", command=size_figure)

task1_label.grid(column=1, row=1)
move_button.grid(column=1, row=2)
rotate_button.grid(column=1, row=3)
size_button.grid(column=1, row=4)
root.mainloop()