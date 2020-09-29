from tkinter import *
import math



root = Tk()
root.title("Лабораторна робота 1")

# function for 1 task
def show_task1():
    global window1
    if window1 is None:
        window1 = Canvas(width=400, height=400, bg='white')
        window1.pack()
        #start coordinates, list of colours
        start_coordinate_1 = 30
        start_coordinate_2 = 10
        start_coordinate_3 = 350
        start_coordinate_4 = 180
        colours = ["yellow", "orange", "red", "cyan"]
        c = 0

        a = (50, 60, 70, 80)
        for i in a:
            #creating ovals
            window1.create_oval(start_coordinate_1 + i, start_coordinate_2 + i,
                                 start_coordinate_3 - i, start_coordinate_4 - i,
                                width=2, outline=colours[c])
            c += 1
        # start coordinates, list of colours
        start_coordinate_12 = 30
        start_coordinate_22 = 80
        start_coordinate_23= 350
        start_coordinate_24 = 250
        colours2 = ["yellow", "orange", "red", "cyan"]
        k = 0
        b = (50, 60, 70, 80)
        for i in b:
            #creating rectangle
            window1.create_polygon((start_coordinate_12+i, start_coordinate_22+i),
                                   (start_coordinate_23-i, start_coordinate_22+i),
                                   (start_coordinate_23-i, start_coordinate_24-i),
                                   (start_coordinate_12+i, start_coordinate_24-i),
                                   outline=colours2[k], fill='white', width=2)
            k +=1


    else:
        window1.destroy()
        window1 = None

# function for 2 task

def show_task21():
    global window21
    if window21 is None:
        # creating of 4 triangles for logotype, colour is green
        window2 = Canvas(width=400, height=400, bg='white')
        window2.pack()
        window2.create_polygon(120, 40, 200, 40, 160, 140, outline='green', width=2, fill='white')
        window2.create_polygon(60, 100, 60, 180, 160, 140, outline='green', width=2, fill='white')
        window2.create_polygon(120, 240, 200, 240, 160, 140, outline='green', width=2, fill='white')
        window2.create_polygon(260, 100, 260, 180, 160, 140, outline='green', width=2, fill='white')
    else:
        window21.destroy()
        window21 = None

# function for 2 task

def show_task22():
    global window22
    if window22 is None:
        window2 = Canvas(width=400, height=400, bg='white')
        window2.pack()
        # creating of 4 triangles for logotype, colour is green
        window2.create_polygon(120, 40, 200, 40, 160, 140, outline='white', width=2, fill='red')
        window2.create_polygon(60, 100, 60, 180, 160, 140, outline='white', width=2, fill='blue')
        window2.create_polygon(120, 240, 200, 240, 160, 140, outline='white', width=2, fill='green')
        window2.create_polygon(260, 100, 260, 180, 160, 140, outline='white', width=2, fill='orange')
    else:
        window22.destroy()
        window22 = None


# function for 3 task

def show_task3():
    global window3
    if window3 is None :
        c = Canvas(window3, width=700, height=200, bg='white')
        a = 1
        points1 = []
        #creating axis
        c.create_line(100, 100, 697, 100, width=3, fill="black", arrow="last")
        c.create_line(415, 200, 415, 3, width=3, fill="black", arrow="last")
        #set of x
        for x in range(500):
            y = 0.01 * a * math.sin(-x)# my graphic3
            points1.append(tuple([x * 50000  + 100, y * 50000 + 100]))
        c.create_line(points1, fill="red", smooth=1, width=1)

        a = 1
        points2 = []
        for x in range(500):
            y = 0.01 * (a + 3) * math.sin(-x)# my graphic1
            points2.append(tuple([x * 50000 + 100, y * 50000 + 100]))
        c.create_line(points2, fill="green", smooth=1, width=1)

        a = 1
        points2 = []
        for x in range(500):
            y = (a * 1) * math.cos(-x)# my graphic2
            points2.append(tuple([x * 50000 + 100, y * 50000 + 100]))
        c.create_line(points2, fill="orange", smooth=1, width=1)
        c.create_text(697, 105, text="x")
        c.create_text(410, 3, text="y")

        c.pack()




# globals

window1 = None
window21 = None
window22 = None
window3 = None

#buttons for showing
task1show_button = Button(root, text="Переглянути 1 завдання", command=show_task1)
task21show_button = Button(root, text="Переглянути 2.1 завдання", command=show_task21)
task22show_button = Button(root, text="Переглянути 2.2 завдання", command=show_task22)
task3show_button = Button(root, text="Переглянути 3 завдання", command=show_task3)

task1show_button.pack()
task21show_button.pack()
task22show_button.pack()
task3show_button.pack()

root.mainloop()
