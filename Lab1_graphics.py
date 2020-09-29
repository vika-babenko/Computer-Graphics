from tkinter import *
from graphics import *
import matplotlib.pyplot as plt
import numpy as np



root = Tk()
root.title("Лабораторна робота 1")

# function for 1 task
def show_task1():
    global window1
    if window1 is None:
        window1 = GraphWin("Вікно для графіки", 500, 500)#window for drawing
        #coordinates
        start_coordinate_1 = 30
        start_coordinate_2 = 10
        start_coordinate_3 = 350
        start_coordinate_4 = 180
        #colours
        colours = ["yellow", "orange", "red", "blue", "green", "magenta"]
        c = 0
#creating ovals
        a = (50, 60, 70, 80, 90)
        for i in a:
            obj = Oval(Point(start_coordinate_1 + i, start_coordinate_2 + i),
                       Point(start_coordinate_3 - i, start_coordinate_4 - i))
            c += 1
            obj.setWidth(2)
            obj.setOutline(colours[c])
            obj.draw(window1)

        start_coordinate_12 = 30
        start_coordinate_22 = 80
        start_coordinate_23 = 350
        start_coordinate_24 = 250
        colours2 = ["yellow", "orange", "red", "cyan", "magenta"]
        k = 0

        b = (50, 60, 70, 80, 90)
#creating rectangle by lines
        for i in b:
            obj1 = Line(Point(start_coordinate_12 + i, start_coordinate_22 + i),
                        Point(start_coordinate_23 - i, start_coordinate_22 + i))

            obj2 = Line(Point(start_coordinate_23 - i, start_coordinate_22 + i),
                        Point(start_coordinate_23 - i, start_coordinate_24 - i))

            obj3 = Line(Point(start_coordinate_23 - i, start_coordinate_24 - i),
                        Point(start_coordinate_12 + i, start_coordinate_24 - i))

            obj4 = Line(Point(start_coordinate_12 + i, start_coordinate_24 - i),
                        Point(start_coordinate_12 + i, start_coordinate_22 + i))

            obj1.setOutline(colours2[k])
            obj2.setOutline(colours2[k])
            obj3.setOutline(colours2[k])
            obj4.setOutline(colours2[k])

            obj1.setWidth(2)
            obj2.setWidth(2)
            obj3.setWidth(2)
            obj4.setWidth(2)

            obj1.draw(window1)
            obj2.draw(window1)
            obj3.draw(window1)
            obj4.draw(window1)

            k += 1

#logotype
def show_task21():
    global window21
    if window21 is None:
        window21 = GraphWin("Вікно для графіки", 300, 300)#window
        # creating triangles
        obj1 = Polygon(Point(120, 40), Point(200, 40), Point(160, 140))
        obj2 = Polygon(Point(60, 100), Point(60, 180), Point(160, 140))
        obj3 = Polygon(Point(260, 180), Point(260, 100), Point(160, 140))
        obj4 = Polygon(Point(120, 240), Point(200, 240), Point(160, 140))

           #width
        obj1.setWidth(3)
        obj2.setWidth(3)
        obj3.setWidth(3)
        obj4.setWidth(3)

# filling of triangles
        obj1.setFill("green")
        obj2.setFill("green")
        obj3.setFill("green")
        obj4.setFill("green")

        obj1.setOutline("green")
        obj2.setOutline("green")
        obj3.setOutline("green")
        obj4.setOutline("green")

        obj1.draw(window21)
        obj2.draw(window21)
        obj3.draw(window21)
        obj4.draw(window21)




    else:
        window21.destroy()
        window21 = None

#function for 2 task
def show_task22():
    global window22
    if window22 is None:
        window22 = GraphWin("Вікно для графіки", 300, 300)
        obj1 = Polygon(Point(120, 40), Point(200, 40), Point(160, 140))
        obj2 = Polygon(Point(60, 100), Point(60, 180), Point(160, 140))
        obj3 = Polygon(Point(260, 180), Point(260, 100), Point(160, 140))
        obj4 = Polygon(Point(120, 240), Point(200, 240), Point(160, 140))

        obj1.setWidth(3)
        obj2.setWidth(3)
        obj3.setWidth(3)
        obj4.setWidth(3)

        obj1.setFill("red")
        obj2.setFill("blue")
        obj3.setFill("orange")
        obj4.setFill("green")

        obj1.setOutline("white")
        obj2.setOutline("white")
        obj3.setOutline("white")
        obj4.setOutline("white")

        obj1.draw(window22)
        obj2.draw(window22)
        obj3.draw(window22)
        obj4.draw(window22)

    else:
        window22.destroy()
        window22 = None

#function for third task
def show_task3():
    global window3
    if window3 is None:
        # Независимая (x) и зависимая (y) переменные
        plt.xlabel("x", fontsize=14)  # ось абсцисс
        plt.ylabel("y", fontsize=14)  # ось ординат
        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        y = 0.01 * np.sin(x)
        y1 = 4 * 0.01 * np.sin(x)
        y2 = 0.01 * np.cos(x)
        plt.plot(x, y, x, y1, x, y2)
        plt.show()








# globals
window1 = None
window21 =None
window22 =None
window3 = None

#buttons for showing
show_t1_button = Button(root, text="Переглянути 1 завдання", command=show_task1)
show_t1_button.pack()
show_t21_button = Button(root, text="Переглянути 2.1 завдання", command=show_task21)
show_t21_button.pack()
show_t22_button = Button(root, text="Переглянути 2.2 завдання", command=show_task22)
show_t22_button.pack()
show_t3_button = Button(root, text="Переглянути 3 завдання", command=show_task3)
show_t3_button.pack()
root.mainloop()
