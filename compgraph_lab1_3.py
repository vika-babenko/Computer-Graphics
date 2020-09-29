import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
root = Tk()

# function for first task
def task1_def():
    #crating of rectangles
    plt.plot([10, 80, 80, 10, 10], [60, 60, 0, 0, 60], color="cyan", linewidth=3)
    plt.plot([15, 75, 75, 15, 15], [55, 55, 5, 5, 55], color="blue", linewidth=3)
    plt.plot([20, 70, 70, 20, 20], [50, 50, 10, 10, 50], color="red", linewidth=3)
    plt.plot([25, 65, 65, 25, 25], [45, 45, 15, 15, 45], color="darkorange", linewidth=3)
    plt.plot([30, 60, 60, 30, 30], [40, 40, 20, 20, 40], color="yellow", linewidth=3)

#show on screen
    plt.show()


def task2_1_def():
    x1 = [50, 90, 70, 50]# coordinates of logotypes triangle
    y1 = [110, 110, 60, 110]
    x2 = [20, 70, 20, 20]
    y2 = [80, 60, 40, 80]
    x3 = [50, 90, 70, 50]
    y3 = [10, 10, 60, 10]
    x4 = [120, 120, 70, 120]
    y4 = [80, 40, 60, 80]
#design
    plt.fill(x1, y1, linewidth=3, edgecolor="darkred", facecolor="red")
    plt.fill(x2, y2, linewidth=3, edgecolor="darkorange", facecolor="orange")
    plt.fill(x3, y3, linewidth=3, edgecolor="blue", facecolor="deepskyblue")
    plt.fill(x4, y4, linewidth=3, edgecolor="green", facecolor="lime")

#show on the screen
    plt.show()

# function for 2-d task
def task2_2_def():
    x1 = [50, 90, 70, 50]# coordinates
    y1 = [110, 110, 60, 110]
    x2 = [20, 70, 20, 20]
    y2 = [80, 60, 40, 80]
    x3 = [50, 90, 70, 50]
    y3 = [10, 10, 60, 10]
    x4 = [120, 120, 70, 120]
    y4 = [80, 40, 60, 80]
    fig, ax = plt.subplots()

    ax.fill(x1, y1, "green")
    ax.fill(x2, y2, "green")
    ax.fill(x3, y3, "green")
    ax.fill(x4, y4, "green")

    fig.set_figwidth(6)  # width and height
    fig.set_figheight(5)
    fig.set_facecolor('floralwhite')
    ax.set_facecolor('seashell')

    plt.show()
    plt.show()

# function for craeting graphics
def task3_1_def():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_label_coords(0.99, 0.48)
    ax.yaxis.set_label_coords(0.55, 0.99)
    # Независимая (x) и зависимая (y) переменные
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = 0.01 * 1 * np.sin(x)

    plt.plot(x, y, color="green")
    plt.show()

# function for third task
def task3_2_def():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_label_coords(0.99, 0.48)
    ax.yaxis.set_label_coords(0.55, 0.99)
    # Независимая (x) и зависимая (y) переменные
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = (1+3) * np.sin(x)

    plt.plot(x, y, color="green")
    plt.show()

# function for third task
def task3_3_def():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_label_coords(0.99, 0.48)
    ax.yaxis.set_label_coords(0.55, 0.99)
    # Независимая (x) и зависимая (y) переменные
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = 0.01 * 1 * np.cos(x)

    plt.plot(x, y, color="green")
    plt.show()

# function for third task
def task3_4_def():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_label_coords(0.99, 0.48)
    ax.yaxis.set_label_coords(0.55, 0.99)
    # Choose evenly spaced x intervals
    x3 = np.linspace(-2*np.pi, 2*np.pi, 666)
    y3 = (1+3) * np.sin(x3)
    y3[np.abs(np.cos(x3)) <= np.abs(np.sin(x3[1]-x3[0]))] = np.nan
    plt.plot(x3, y3, color="magenta")

    # Независимая (x) и зависимая (y) переменные

    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат

    x1 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y1 = 0.01 * 1 * np.cos(x1)

    plt.plot(x1, y1)

    x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y2 = 0.01 * 1 * np.sin(x2)

    plt.plot(x2, y2, color="green")

    plt.show()

#buttons for showing resolved tasks

task1_button = Button(root, text="Завдання 1", command=task1_def)
task2_1_button = Button(root, text="Завдання 2.1", command=task2_1_def)
task2_2_button = Button(root, text="Завдання 2.2", command=task2_2_def)
task3_1_button = Button(root, text="Завдання 3.1", command=task3_1_def)
task3_2_button = Button(root, text="Завдання 3.2", command=task3_2_def)
task3_3_button = Button(root, text="Завдання 3.3", command=task3_3_def)
task3_4_button = Button(root, text="Завдання 3.4", command=task3_4_def)



task1_button.pack()
task2_1_button.pack()
task2_2_button.pack()
task3_1_button.pack()
task3_2_button.pack()
task3_3_button.pack()
task3_4_button.pack()
root.mainloop()