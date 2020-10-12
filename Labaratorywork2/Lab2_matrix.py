from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math
# переміщення
def move_figure():
    global window1
    if window1 is None:
        # координати
        triangle = np.array([[0, 0, 1],
                                 [30, 60, 1],
                                 [60, 60, 1]])
        # перетворення координат  для переміщення (розширена матриця)
        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[1, 0, 5],
                          [0, 1, 5],
                          [0, 0, 1]])
            a = a.T
            triangle = triangle.dot(a)
            plt.plot([triangle[0, 0] + triangle[0, 2], triangle[1, 0] + triangle[1, 2],
                      triangle[2, 0] + triangle[2, 2],
                      triangle[0, 0] + triangle[0, 2]],
                     [triangle[0, 1] + triangle[0, 2], triangle[1, 1] + triangle[1, 2],
                      triangle[2, 1] + triangle[2, 2],
                      triangle[0, 1] + triangle[0, 2]])

        plt.show()
    else:
        window1.destroy()
        window1 = None

# обертання фігури навколо ОХ
def rotate_figure():
    global window3
    if window3 is None:
        # координати трикутника
        triangle = np.array([[0, 0, 1],
                            [30, 60, 1],
                            [60, 60, 1]])

        # за допомогою матриці напрямних косинусів та синусів реалізуємо обертання

        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[math.cos(i), -math.sin(i), 0],
                          [math.sin(i), math.cos(i), 0],
                          [0, 0, 1]])
            a = a.T
            triangle = triangle.dot(a)
            plt.plot([triangle[0, 0] + triangle[0, 2],
                      triangle[1, 0] + triangle[1, 2],
                      triangle[2, 0] + triangle[2, 2],
                      triangle[0, 0] + triangle[0, 2]],
                     [triangle[0, 1] + triangle[0, 2],
                      triangle[1, 1] + triangle[1, 2],
                      triangle[2, 1] + triangle[2, 2],
                      triangle[0, 1] + triangle[0, 2]])

        plt.show()

    else:
        window3.destroy()
        window3 = None

# масштабування
def size_figure():
    global window2
    if window2 is None:
        # координати трикутника
        triangle = np.array([[0, 0, 1],
                                 [30, 60, 1],
                                 [60, 60, 1]])
        # реалізація масштабування за допомогою масштабних коефіцієнтів
        for i in [0, 0.5, 0.5, 0.5]:
            a = np.array([[1.5, 0, 0],
                          [0, 1.5, 0],
                          [0, 0, 1]])
            a = a.T
            triangle = triangle.dot(a)
            plt.plot([triangle[0, 0] + triangle[0, 2],
                      triangle[1, 0] + triangle[1, 2],
                      triangle[2, 0] + triangle[2, 2],
                      triangle[0, 0] + triangle[0, 2]],
                     [triangle[0, 1] + triangle[0, 2],
                      triangle[1, 1] + triangle[1, 2],
                      triangle[2, 1] + triangle[2, 2],
                      triangle[0, 1] + triangle[0, 2]])
        plt.show()

    else:
        window2.destroy()
        window2 = None


root = Tk()
# глобальні змінні
window1 = None
window2 = None
window3 = None
# кнопки та написи
task1_label = Label(root, text="Виконання першого завдання(розширена матриця), бібліотека Matplotlib")
move_button = Button(root, text="Переміщення трикутника матриці", command=move_figure)
rotate_button = Button(root, text="Обертання трикутника матриці", command=rotate_figure)
size_button = Button(root, text="Розмір фігури матриці", command=size_figure)

root.title("Labwork2. Computer graphics:)")
task1_label.grid(column=1, row=1)
move_button.grid(column=1, row=2)
rotate_button.grid(column=1, row=3)
size_button.grid(column=1, row=4)
root.mainloop()