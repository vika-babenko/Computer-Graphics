import random
from graphics import *
import math as mt
import time
import numpy as np

# coordinates of parallelepiped
xw = 600
yw = 600
st = 300

# matrix of coordinates
Parallelepiped = np.array([[0, 0, 0, 1],
                           [st, 0, 0, 1],
                           [st, st, 0, 1],
                           [0, st, 0, 1],
                           [0, 0, st, 1],
                           [st, 0, st, 1],
                           [st, st, st, 1],
                           [0, st, st, 1]])
print("Координати паралелепіпеда у вигляді матриці")
print(Parallelepiped)

# функція проекції на ХОУ
def ProjectXY(Figure):
   f = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 1]])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('Проекція на ХОУ')
   print(Prxy)
   return Prxy

# зміщення
def ShiftXYZ(Figure, l, m, n):
   f = np.array([[1, 0, 0, l],
                 [0, 1, 0, m],
                 [0, 0, 1, n],
                 [1, 0, 0, 1]])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('зміщення')
   print(Prxy)
   return Prxy
# обертання коло oх
def insertX(Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([[1, 0, 0, 0],
                  [0, mt.cos(TetaR), mt.sin(TetaR), 0],
                  [0, -mt.sin(TetaR), mt.cos(TetaR), 0],
                  [0, 0, 0, 1]])
    ft=f.T
    Prxy = Figure.dot(ft)
    print('обертання коло х')
    print(Prxy)
    return Prxy
# аксонометрія
def dimetri(Figure, TetaG1, TetaG2):

    TetaR1=(3/14*TetaG1)/180
    TetaR2=(3/14*TetaG2)/180

    f1 = np.array([[mt.cos(TetaR1), 0, -mt.sin(TetaR1), 0],
                   [0, 1, 0, 0],
                   [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1],
                   [0, 0, 0, 0]])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array([[1, 0, 0, 0],
                   [0, mt.cos(TetaR2), mt.sin(TetaR2), 0],
                   [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0],
                   [0, 0, 0, 1] ])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    print('Аксонометрія')
    print(Prxy2)
    return Prxy2
# функція побудови паралелепіпеда
def PrlpdWiz(Prxy):
    Ax = Prxy[0, 0]
    Ay = Prxy[0, 1]

    Bx = Prxy[1, 0]
    By = Prxy[1, 1]

    Ix = Prxy[2, 0]
    Iy = Prxy[2, 1]

    Mx = Prxy[3, 0]
    My = Prxy[3, 1]

    Dx = Prxy[4, 0]
    Dy = Prxy[4, 1]

    Cx = Prxy[5, 0]
    Cy = Prxy[5, 1]

    Fx = Prxy[6, 0]
    Fy = Prxy[6, 1]

    Ex = Prxy[7, 0]
    Ey = Prxy[7, 1]

    # print(Ax, Ay); print(Bx, By); print(Ix, Iy);  print(Mx, My);
    # print(Dx, Dy); print(Cx, Cy); print(Fx, Fy); print(Ex, Ey);
    colors = ["red", "orange", "magenta", "pink", "lime", "green", "black"]
    colors_2 = ["skyblue", "cyan", "blue"]
    a = colors[random.randint(0, len(colors) - 1)]
    b = colors[random.randint(0, len(colors) - 1)]
    c = colors[random.randint(0, len(colors) - 1)]
    d = colors[random.randint(0, len(colors) - 1)]
    e = colors_2[random.randint(0, len(colors_2) - 1)]
    z = colors_2[random.randint(0, len(colors_2) - 1)]
    t = colors_2[random.randint(0, len(colors_2) - 1)]
    r = colors_2[random.randint(0, len(colors_2) - 1)]



    obj1 = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ix, Iy), Point(Mx, My))
    obj1.setFill(e)
    obj1.setOutline(a)
    obj1.draw(win)

    obj2 = Polygon(Point(Dx, Dy), Point(Cx, Cy), Point(Fx, Fy), Point(Ex, Ey))
    obj2.setFill(z)
    obj2.setOutline(b)
    obj2.draw(win)

    obj3 = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj3.setFill(t)
    obj3.setOutline(c)
    obj3.draw(win)

    obj4 = Polygon(Point(Mx, My), Point(Ix, Iy), Point(Fx, Fy), Point(Ex, Ey))
    obj4.setFill(r)
    obj4.setOutline(d)
    obj4.draw(win)
    return PrlpdWiz
#-------------------------------------------- побудова паралелепіпеда -----------------------------
win = GraphWin("3-D модель паралелепіпеда, аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600
yw=600
st=50
TetaG1=0
TetaG2=-90
l=(xw/3)-st
m=(yw/3)-st
n=m

#Prlpd1=ShiftXYZ (Prlpd, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
#Prlpd2=insertX (Prlpd1, TetaG1)
#Prxy3=ProjectXY (Prlpd2)

Prxy3 = Parallelepiped
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда, аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600
yw=600
st=50
TetaG1=0
TetaG2=-90

# l=(xw/3)-st
m=(yw/3)-st
# n=m

Prlpd1=ShiftXYZ (Parallelepiped, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
Prlpd2=insertX(Prlpd1, TetaG1)
Prxy3=ProjectXY(Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда оберт коло Х аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600
yw=600
st=50
TetaG1=180
TetaG2=-90
l=(xw/3)-st
m=(yw/3)-st
n=m
Prlpd1=ShiftXYZ (Parallelepiped, l, m, n)
#Prlpd2=dimetri (Prlpd1, TetaG1, TetaG2)
Prlpd2=insertX(Prlpd1, TetaG1)
Prxy3=ProjectXY(Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D паралелепіпеда діметричний оберт навколо Х та У аксонометрічна проекція на ХУ", xw, yw)
win.setBackground('white')
xw=600
yw=600
st=50
TetaG1=180
TetaG2=-90
l=(xw/2)-st
m=(yw/2)-st
n = m
Prlpd1=ShiftXYZ(Parallelepiped, l, m, n)
Prlpd2=dimetri(Prlpd1, TetaG1, TetaG2)
#Prlpd2=insertX (Prlpd1, TetaG1)
Prxy3=ProjectXY(Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

