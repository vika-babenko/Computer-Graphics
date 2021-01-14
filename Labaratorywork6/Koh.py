import turtle
from random import random, randrange
import numpy as np
import math as mt

# координати паралелепіпеда
xw=600
yw=600
st=300
# розташування координат у строках: дальній чотирикутник - A B I M,  ближній чотирикутник D C F E
Prlpd = np.array([[0, 0, 0, 1],
                  [st, 0, 0, 1],
                  [st, st, 0, 1],
                  [0, st, 0, 1],
                  [0, 0, st, 1],
                  [st, 0, st, 1],
                  [st, st, st, 1],
                  [0, st, st, 1]])
# функция проекції на xy, z=0
def ProjectXY(Figure):
   f = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   return Prxy
# зміщення
def ShiftXYZ(Figure, l, m, n):
   f = np.array([[1, 0, 0, l],
                 [0, 1, 0, m],
                 [0, 0, 1, n],
                 [1, 0, 0, 1]])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   return Prxy
# обертання коло х
def insertX(Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([[1, 0, 0, 0],
                  [0, mt.cos(TetaR), mt.sin(TetaR), 0],
                  [0, -mt.sin(TetaR),  mt.cos(TetaR), 0],
                  [0, 0, 0, 1]])
    ft=f.T
    Prxy = Figure.dot(ft)
    return Prxy
# аксонометрія
def dimetri(Figure, TetaG1, TetaG2):
    TetaR1=(3/14*TetaG1)/180
    TetaR2=(3/14*TetaG2)/180
    f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0],
                   [0, 1, 0, 0],
                   [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1],
                   [0, 0, 0, 0],])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array([[1, 0, 0, 0],
                   [0, mt.cos(TetaR2), mt.sin(TetaR2), 0],
                   [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0],
                   [0, 0, 0, 1]])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2


# функція побудови растрового паралелепіпеда
def PrlpdWiz(Prxy3):
    # дальня грань - (в проекції ліва)
    Ax1 = Prxy3[0, 0]
    Ay1 = Prxy3[0, 1]
    Bx1 = Prxy3[1, 0]
    By1 = Prxy3[1, 1]
    Ix1 = Prxy3[2, 0]
    Iy1 = Prxy3[2, 1]
    Mx1 = Prxy3[3, 0]
    My1 = Prxy3[3, 1]
    # ближня грань - (в проекції права)
    Dx1 = Prxy3[4, 0]
    Dy1 = Prxy3[4, 1]
    Cx1 = Prxy3[5, 0]
    Cy1 = Prxy3[5, 1]
    Fx1 = Prxy3[6, 0]
    Fy1 = Prxy3[6, 1]
    Ex1 = Prxy3[7, 0]
    Ey1 = Prxy3[7, 1]

    # дальня грань - (в проекції ліва)
    turtle.up()
    turtle.goto(Ax1, Ay1)
    turtle.down()
    turtle.goto(Bx1, By1)
    turtle.goto(Ix1, Iy1)
    turtle.goto(Mx1, My1)
    turtle.goto(Ax1, Ay1)

    # ближча грань - (в проекції права)
    turtle.up()
    turtle.goto(Dx1, Dy1)
    turtle.down()
    turtle.goto(Cx1, Cy1)
    turtle.goto(Fx1, Fy1)
    turtle.goto(Ex1, Ey1)
    turtle.goto(Dx1, Dy1)

    # верхеня грань - (в проекції верхня)

    turtle.up()
    turtle.goto(Ax1, Ay1)
    turtle.down()
    turtle.goto(Bx1, By1)
    turtle.goto(Cx1, Cy1)
    turtle.goto(Dx1, Dy1)
    turtle.goto(Ax1, Ay1)

    # верхеня грань - (в проекції верхня)
    turtle.up()
    turtle.goto(Mx1, My1)
    turtle.down()
    turtle.goto(Ix1, Iy1)
    turtle.goto(Fx1, Fy1)
    turtle.goto(Ex1, Ey1)
    turtle.goto(Mx1, My1)

    # ліва грань - (в проекції ближня)
    turtle.up()
    turtle.goto(Ax1, Ay1)
    turtle.down()
    turtle.goto(Mx1, My1)
    turtle.goto(Ex1, Ey1)
    turtle.goto(Dx1, Dy1)
    turtle.goto(Ax1, Ay1)

    # права грань - (в проекції дальня)
    turtle.up()
    turtle.goto(Bx1, By1)
    turtle.down()
    turtle.goto(Ix1, Iy1)
    turtle.goto(Fx1, Fy1)
    turtle.goto(Cx1, Cy1)
    turtle.goto(Bx1, By1)

    return PrlpdWiz



size = 300; n = 2;
def koch_curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)

def draw_koch_snowflake(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)

draw_koch_snowflake(size, n)
# --------------- багатократний фрактал КОХА (сніжинка) - як форма черепашки ---------
def koch_curve(turtle, steps, length):
    if steps == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, steps - 1, length / 3)
            turtle.left(angle)

def koch_snowflake(turtle, steps, length):
    turtle.begin_poly()

    for _ in range(3):
        koch_curve(turtle, steps, length)
        turtle.right(120)

    turtle.end_poly()

    return turtle.get_poly()
# ------------------------------ зміна характеристик черепахи ---------------------
turtle.speed("fastest")
turtle.register_shape("snowflake", koch_snowflake(turtle.getturtle(), 2, 100))
turtle.reset()
turtle.penup()
turtle.shape("snowflake")

width, height = turtle.window_width() / 2, turtle.window_height() / 2
width=int(width)
height =int(height)
for _ in range(7):
    turtle.color((random(), random(), random()), (random(), random(), random()))
    turtle.goto(randrange(-width, width), randrange(-height, height))
    turtle.stamp()

# ------------------------------ зміна характеристик черепахи ---------------------
turtle.shape("triangle")
turtle.stamp()
turtle.forward(1)


xw=600; yw=600; st=50; TetaG1=180; TetaG2=-90
l=(xw/2)-st; m=(yw/2)-st; n=m
#Prlpd1=ShiftXYZ (Prlpd, l, m, n)
Prlpd2=dimetri (Prlpd, TetaG1, TetaG2)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
turtle.screen.exitonclick()
turtle.screen.mainloop()
#--------------------------------------------------------------------------------------
