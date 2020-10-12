from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math

root = Tk()
# переміщення
def move_figure():
    global window1
    if window1 is None:
        # координати кожної точки
        a_dot = np.array([[0, 0, 1]])
        b_dot = np.array([[30, 60, 1]])
        c_dot = np.array([[60, 60, 1]])
        # реалізація переміщення шляхом мнлження кожної з координат на матрицю
        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[1, 0, 5],
                          [0, 1, 5],
                          [0, 0, 1]])
            a = a.T
            a_dot = a_dot.dot(a)
            b_dot = b_dot.dot(a)
            c_dot = c_dot.dot(a)
            plt.plot([a_dot[0, 0] + a_dot[0, 2],
                      b_dot[0, 0] + b_dot[0, 2],
                      c_dot[0, 0] + c_dot[0, 2],
                      a_dot[0, 0] + a_dot[0, 2]],
                     [a_dot[0, 1] + a_dot[0, 2],
                      b_dot[0, 1] + b_dot[0, 2],
                      c_dot[0, 1] + c_dot[0, 2],
                      a_dot[0, 1] + a_dot[0, 2]])
        plt.show()
# обертання трикутника
def rotate_figure():
    global window2
    if window2 is None:
        # координати кожної точки трикутника
        a_dot = np.array([[0, 0, 1]])
        b_dot = np.array([[30, 60, 1]])
        c_dot = np.array([[60, 60, 1]])
        # множення кожної координати на матрицю з напрямними косинусами та синусами
        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[math.cos(i), -math.sin(i), 0],
                          [math.sin(i), math.cos(i), 0],
                          [0, 0, 1]])
            a = a.T
            a_dot = a_dot.dot(a)
            b_dot = b_dot.dot(a)
            c_dot = c_dot.dot(a)
            plt.plot([a_dot[0, 0] + a_dot[0, 2],
                      b_dot[0, 0] + b_dot[0, 2],
                      c_dot[0, 0] + c_dot[0, 2],
                      a_dot[0, 0] + a_dot[0, 2]],
                     [a_dot[0, 1] + a_dot[0, 2],
                      b_dot[0, 1] + b_dot[0, 2],
                      c_dot[0, 1] + c_dot[0, 2],
                      a_dot[0, 1] + a_dot[0, 2]])

        plt.show()
# масштабування
def size_figure():
    global window3
    if window3 is None:
        # координати трикутника(кожна точка окремо)
        a_dot = np.array([[0, 0, 1]])
        b_dot = np.array([[30, 60, 1]])
        c_dot = np.array([[60, 60, 1]])
        # множення кожної точки на матрицю з масштабуючими коефіцієнтами -- реалізація
        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[1.5, 0, 0],
                          [0, 1.5, 0],
                          [0, 0, 1]])
            a = a.T
            a_dot = a_dot.dot(a)
            b_dot = b_dot.dot(a)
            c_dot = c_dot.dot(a)
            plt.plot([a_dot[0, 0] + a_dot[0, 2],
                      b_dot[0, 0] + b_dot[0, 2],
                      c_dot[0, 0] + c_dot[0, 2],
                      a_dot[0, 0] + a_dot[0, 2]],
                     [a_dot[0, 1] + a_dot[0, 2],
                      b_dot[0, 1] + b_dot[0, 2],
                      c_dot[0, 1] + c_dot[0, 2],
                      a_dot[0, 1] + a_dot[0, 2]])
        plt.show()




# глобальні змінні
window1 = None
window2 = None
window3 = None

# надписи та книпки для головного вікна
task1_label = Label(root, text="Виконання першого завдання (матриця), бібліотека Matplotlib")
move_button = Button(root, text="Переміщення трикутника матриці", command=move_figure)
rotate_button = Button(root, text="Обертання трикутника матриці", command=rotate_figure)
size_button = Button(root, text="Розмір фігури матриці", command=size_figure)

root.title("Labwork2. Computer graphics:)")
task1_label.grid(column=1, row=1)
move_button.grid(column=1, row=2)
rotate_button.grid(column=1, row=3)
size_button.grid(column=1, row=4)


root.mainloop()