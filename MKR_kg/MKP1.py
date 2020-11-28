import random
from graphics import *
import time
import numpy as np
import math as mt

# координати піраміди
st = 300
Pyramid = np.array([[0, st, 0, 1],
                    [st, st, 0, 1],
                    [st, st, st, 1],
                    [0, st, st, 1],
                    [st/2, 0, st/2, 1]])


# проекція на xy, z=0
def ProjectXY(Figure):
   f = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   return Prxy


# зміщення
def ShiftXYZ (Figure, l, m, n):
   f = np.array([[1, 0, 0, l],
                 [0, 1, 0, m],
                 [0, 0, 1, n],
                 [1, 0, 0, 1]])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   return Prxy

# обертання навколо осі X дає проекцію паралелепіпеда на вісь XY
def insertX (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([ [1, 0, 0, 0],
                   [0, mt.cos(TetaR), mt.sin(TetaR), 0],
                   [0, -mt.sin(TetaR),  mt.cos(TetaR), 0],
                   [0, 0, 0, 1] ])
    ft=f.T
    Prxy = Figure.dot(ft)
    return Prxy


# аксонометрія
def dimetri (Figure, TetaG1, TetaG2):
    TetaR1=(3/14*TetaG1)/180
    TetaR2=(3/14*TetaG2)/180
    f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0],
                   [0, 1, 0, 0],
                   [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1],
                   [0, 0, 0, 0]])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)

    f2 = np.array([ [1, 0, 0, 0],
                    [0, mt.cos(TetaR2), mt.sin(TetaR2), 0],
                    [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0],
                    [0, 0, 0, 1] ])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2


# побудови піраміди
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def drawPolygon(x1, y1, x2, y2, x3, y3, color, outline, win):
    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.setFill(color)
    triangle.setOutline(outline)
    triangle.setWidth(3)
    triangle.draw(win)

def drawPolygon4(x1, y1, x2, y2, x3, y3, x4, y4, color, outline, win):
    rectangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
    rectangle.setFill(color)
    rectangle.setOutline(outline)
    rectangle.setWidth(3)
    rectangle.draw(win)

def PyramidWiz(Prxy, dim):
    Ax = Prxy[0, 0]
    Ay = Prxy[0, 1]
    Bx = Prxy[1, 0]
    By = Prxy[1, 1]
    Cx = Prxy[2, 0]
    Cy = Prxy[2, 1]
    Dx = Prxy[3, 0]
    Dy = Prxy[3, 1]
    Ex = Prxy[4, 0]
    Ey = Prxy[4, 1]

    for i in range(5):

        if dim == 2:
            drawPolygon(Ax, Ay, Dx, Dy, Ex, Ey, "pink", "black", win)
            drawPolygon(Dx, Dy, Ex, Ey, Cx, Cy, "pink", "black", win)
            drawPolygon(Cx, Cy, Bx, By, Ex, Ey, "pink", "black", win)
            drawPolygon(Ax, Ay, Ex, Ey, Bx, By, "pink", "black", win)
            drawPolygon4(Ax, Ay, Dx, Dy, Cx, Cy, Bx, By, "pink", "black", win)
            time.sleep(0.5)


        elif dim == 32:
            colors = ["red", "orange", "magenta", "pink", "lime", "green", "black"]
            a = colors[random.randint(0, len(colors) - 1)]
            b = colors[random.randint(0, len(colors) - 1)]
            c = colors[random.randint(0, len(colors) - 1)]
            d = colors[random.randint(0, len(colors) - 1)]
            e = colors[random.randint(0, len(colors) - 1)]
            drawPolygon(Ax, Ay, Dx, Dy, Ex, Ey, "pink", a, win)
            drawPolygon(Dx, Dy, Ex, Ey, Cx, Cy, "pink", b, win)
            drawPolygon(Cx, Cy, Bx, By, Ex, Ey, "pink", c, win)
            drawPolygon(Ax, Ay, Ex, Ey, Bx, By, "pink", d, win)
            drawPolygon4(Ax, Ay, Dx, Dy, Cx, Cy, Bx, By, "pink", e, win)
            clear(win)

    return PyramidWiz


# виведення піраміди на екран
win = GraphWin("3-D модель піраміди, аксонометрічна проекція на ХУ", 700, 700)
win.setBackground("white")
PyramidWiz(ProjectXY(Pyramid), 2)
win.getMouse()
win.close()

win = GraphWin("3-D модель піраміди, аксонометрічна проекція на ХУ", 700, 700)
win.setBackground("white")
xw = 700
yw = 700
st = 50
TetaG1 = 0
TetaG2 = -90
l = (xw/3)-st
m = (yw/3)-st
n = m
Pyramid1 = ShiftXYZ(Pyramid, l, m, n)
#Pyramid2 = insertX(Pyramid1, TetaG1)
Prxy3 = ProjectXY(Pyramid1)
PyramidWiz(Prxy3, 2)
win.getMouse()
win.close()


win = GraphWin("3-D пірамід циклічний оберт навколо X та Y", 700, 700)
win.setBackground("white")
xw = 700
yw = 700
st = 50

l = (xw/2)-st
m = st
n = m
Pyramid1 = ShiftXYZ(Pyramid, l, m, n)
for i in range(1000):
    TetaG1 = i
    TetaG2 = i - 90
    Pyramid2 = dimetri(Pyramid1, TetaG1, TetaG2)
    Prxy3 = ProjectXY(Pyramid2)
    PyramidWiz(Prxy3, 32)
    time.sleep(0.000000005)

win.getMouse()
win.close()


