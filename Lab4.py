from graphics import *
import time
import numpy as np
import math as mt
import random
import matplotlib.colors as colors


def draw_line_pixel(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0

    obj = Point(x, y)
    obj.setFill('blue')
    obj.draw(win)

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        obj = Point(x, y)
        obj.setFill('blue')
        obj.draw(win)
    return draw_line_pixel


def draw_line_pixel_color(x1, y1, x2, y2, red=0.999, green=0.999, blue=0.999):

    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0

    obj = Point(x, y)
    obj.setFill('yellow')
    obj.draw(win)
    points = list()

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        obj = Point(x, y)
        points.append(obj)
        # перетворення RGB в шеснадцятирічний код з пакету matplotlib !!!
        col16 = colors.rgb2hex((red, green, blue))
        # інтеграція змінної до поля строки !!! СПОСІБ - Конкатенація строк
        obj.setFill('' + col16)
        obj.draw(win)

    if red <= 0.5:
        red += 0.5
    else:
        red - 0.5
    if green <= 0.5:
        green += 0.5
    else:
        green - 0.5
    if blue <= 0.5:
        blue += 0.5
    else:
        blue - 0.5
    newcol = colors.rgb2hex((red, green, blue))

    for i in range(len(points) - 3):
        points[i].setFill('' + newcol)
        points[i + 1].setFill('' + newcol)
        points[i + 3].setFill('' + newcol)
    return draw_line_pixel_color


def PrlpdWiz_Pixel(Prxy3):
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
    draw_line_pixel(Ax1, Ay1, Bx1, By1)
    draw_line_pixel(Bx1, By1, Ix1, Iy1)
    draw_line_pixel(Ix1, Iy1, Mx1, My1)
    draw_line_pixel(Mx1, My1, Ax1, Ay1)

    # ближча грань - (в проекції права)
    draw_line_pixel(Dx1, Dy1, Cx1, Cy1)
    draw_line_pixel(Cx1, Cy1, Fx1, Fy1)
    draw_line_pixel(Fx1, Fy1, Ex1, Ey1)
    draw_line_pixel(Ex1, Ey1, Dx1, Dy1)

    # верхеня грань - (в проекції верхня)
    draw_line_pixel(Ax1, Ay1, Bx1, By1)
    draw_line_pixel(Bx1, By1, Cx1, Cy1)
    draw_line_pixel(Cx1, Cy1, Dx1, Dy1)
    draw_line_pixel(Dx1, Dy1, Ax1, Ay1)

    # верхеня грань - (в проекції верхня)
    draw_line_pixel(Mx1, My1, Ix1, Iy1)
    draw_line_pixel(Ix1, Iy1, Fx1, Fy1)
    draw_line_pixel(Fx1, Fy1, Ex1, Ey1)
    draw_line_pixel(Ex1, Ey1, Mx1, My1)

    # ліва грань - (в проекції ближня)
    draw_line_pixel(Ax1, Ay1, Mx1, My1)
    draw_line_pixel(Mx1, My1, Ex1, Ey1)
    draw_line_pixel(Ex1, Ey1, Dx1, Dy1)
    draw_line_pixel(Dx1, Dy1, Ax1, Ay1)

    # -права грань - (в проекції дальня)
    draw_line_pixel(Bx1, By1, Ix1, Iy1)
    draw_line_pixel(Ix1, Iy1, Fx1, Fy1)
    draw_line_pixel(Fx1, Fy1, Cx1, Cy1)
    draw_line_pixel(Cx1, Cy1, Bx1, By1)
    return PrlpdWiz_Pixel

def PrlpdWiz_Pixel_color(Prxy3):
    red = random.randint(0, 255) / 1000;
    green = random.randint(0, 255) / 1000;
    blue = random.randint(0, 255) / 1000

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
    draw_line_pixel_color(Ax1, Ay1, Bx1, By1, red, green, blue)
    draw_line_pixel_color(Bx1, By1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Mx1, My1, red, green, blue)
    draw_line_pixel_color(Mx1, My1, Ax1, Ay1, red, green, blue)

    # ближча грань - (в проекції права)
    draw_line_pixel_color(Dx1, Dy1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Dx1, Dy1, red, green, blue)

    # верхня грань - (в проекції верхня)
    draw_line_pixel_color(Ax1, Ay1, Bx1, By1, red, green, blue)
    draw_line_pixel_color(Bx1, By1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Dx1, Dy1, red, green, blue)
    draw_line_pixel_color(Dx1, Dy1, Ax1, Ay1, red, green, blue)

    # верхеня грань - (в проекції верхня)
    draw_line_pixel_color(Mx1, My1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Mx1, My1, red, green, blue)

    # ліва грань - (в проекції ближня)
    draw_line_pixel_color(Ax1, Ay1, Mx1, My1, red, green, blue)
    draw_line_pixel_color(Mx1, My1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Dx1, Dy1, red, green, blue)
    draw_line_pixel_color(Dx1, Dy1, Ax1, Ay1, red, green, blue)
    # права грань - (в проекції дальня)
    draw_line_pixel_color(Bx1, By1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Bx1, By1, red, green, blue)

    return PrlpdWiz_Pixel_color


def PrlpdWiz_Pixel_color_2(Prxy3):
    red = random.randint(0, 999) / 1000
    green = random.randint(0, 999) / 1000
    blue = random.randint(0, 999) / 1000
    background = colors.rgb2hex((red, green, blue))
    if red <= 0.3:
        new_red = red + 0.3
    else:
        new_red = red - 0.3
    if green <= 0.3:
        new_green = green + 0.3
    else:
        new_green = green - 0.3
    if blue <= 0.3:
        new_blue = blue + 0.3
    else:
        new_blue = blue - 0.3
    used_color = colors.rgb2hex((new_red, new_green, new_blue))

    Ax1 = Prxy3[0, 0]
    Ay1 = Prxy3[0, 1]

    Bx1 = Prxy3[1, 0]
    By1 = Prxy3[1, 1]

    Ix1 = Prxy3[2, 0]
    Iy1 = Prxy3[2, 1]

    Mx1 = Prxy3[3, 0]
    My1 = Prxy3[3, 1]

    Dx1 = Prxy3[4, 0]
    Dy1 = Prxy3[4, 1]

    Cx1 = Prxy3[5, 0]
    Cy1 = Prxy3[5, 1]

    Fx1 = Prxy3[6, 0]
    Fy1 = Prxy3[6, 1]

    Ex1 = Prxy3[7, 0]
    Ey1 = Prxy3[7, 1]

    # дальня грань - (в проекції ліва)
    draw_line_pixel_color(Ax1, Ay1, Bx1, By1, red, green, blue)
    draw_line_pixel_color(Bx1, By1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Mx1, My1, red, green, blue)
    draw_line_pixel_color(Mx1, My1, Ax1, Ay1, red, green, blue)

    # Тильна грань
    obj1 = Polygon(Point(Ax1, Ay1), Point(Bx1, By1), Point(Ix1, Iy1), Point(Mx1, My1))
    obj1.setOutline(background)
    obj1.setFill(used_color)
    obj1.draw(win)

    # ближча грань - (в проекції права)
    draw_line_pixel_color(Dx1, Dy1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Dx1, Dy1, red, green, blue)

#  Фронтальна грань
    obj2 = Polygon(Point(Dx1, Dy1), Point(Cx1, Cy1), Point(Fx1, Fy1), Point(Ex1, Ey1))
    obj2.setOutline(background)
    obj2.setFill(used_color)
    obj2.draw(win)

    # верхня грань - (в проекції верхня)
    draw_line_pixel_color(Ax1, Ay1, Bx1, By1, red, green, blue)
    draw_line_pixel_color(Bx1, By1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Dx1, Dy1, red, green, blue)
    draw_line_pixel_color(Dx1, Dy1, Ax1, Ay1, red, green, blue)

    #  Верхня грань
    obj3 = Polygon(Point(Ax1, Ay1), Point(Bx1, By1), Point(Cx1, Cy1), Point(Dx1, Dy1))
    obj3.setOutline(background)
    obj3.setFill(used_color)
    obj3.draw(win)

    # верхеня грань - (в проекції верхня)
    draw_line_pixel_color(Mx1, My1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Mx1, My1, red, green, blue)
    #  Нижня грань
    obj4 = Polygon(Point(Mx1, My1), Point(Ix1, Iy1), Point(Fx1, Fy1), Point(Ex1, Ey1))
    obj4.setOutline(background)
    obj4.setFill(used_color)
    obj4.draw(win)

    # ліва грань - (в проекції ближня)
    draw_line_pixel_color(Ax1, Ay1, Mx1, My1, red, green, blue)
    draw_line_pixel_color(Mx1, My1, Ex1, Ey1, red, green, blue)
    draw_line_pixel_color(Ex1, Ey1, Dx1, Dy1, red, green, blue)
    draw_line_pixel_color(Dx1, Dy1, Ax1, Ay1, red, green, blue)
    #  Ліва грань
    obj5 = Polygon(Point(Ax1, Ay1), Point(Mx1, My1), Point(Ex1, Ey1), Point(Dx1, Dy1))
    obj5.setOutline(background)
    obj5.setFill(used_color)
    obj5.draw(win)

    # права грань - (в проекції дальня)
    draw_line_pixel_color(Bx1, By1, Ix1, Iy1, red, green, blue)
    draw_line_pixel_color(Ix1, Iy1, Fx1, Fy1, red, green, blue)
    draw_line_pixel_color(Fx1, Fy1, Cx1, Cy1, red, green, blue)
    draw_line_pixel_color(Cx1, Cy1, Bx1, By1, red, green, blue)
    obj6 = Polygon(Point(Bx1, By1), Point(Ix1, Iy1), Point(Fx1, Fy1), Point(Cx1, Cy1))
    obj6.setOutline(background)
    obj6.setFill(used_color)
    obj6.draw(win)

    return PrlpdWiz_Pixel_color_2


def Rotate(Figure, TetaG1, TetaG2):
    TetaR1 = (3 / 14 * TetaG1) / 180;
    TetaR2 = (3 / 14 * TetaG2) / 180
    f1 = np.array([[mt.cos(TetaR1), 0, -mt.sin(TetaR1), 0], [0, 1, 0, 0],
                   [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 1], ])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2), mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2 = f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


xw = 500
yw = 500
st = 300

win = GraphWin("Second level", 1000, 1000)
win.setBackground("white")
random.seed()
ranges = list()

win.getMouse()

counter = 0
for i in range(3, 100):
    if i//2 == 1:
        angle1 = random.randint(0, 180)
        angle2 = random.randint(0, 120)
        st = random.randint(100, 400)
        for i in range(3): ranges.append(random.randint(10, 500))

        Prlpd = np.array([[0, 0, 0, 1],
                           [st, 0, 0, 1],
                           [st, st, 0, 1],
                           [0, st, 0, 1],
                           [0, 0, st, 1],
                           [st, 0, st, 1],
                           [st, st, st, 1],
                           [0, st, st, 1]])

        f = np.array([[1, 0, 0, ranges[0]], [0, 1, 0, ranges[1]], [0, 0, 1, ranges[2]], [1, 0, 0, 1]])  # по строках
        ft = f.T
        Prlpd = Prlpd.dot(ft)

        figure = Rotate(Prlpd, angle1, angle2)
        PrlpdWiz_Pixel_color(figure)
        # time.sleep(0.1)
        clear(win)
        ranges.clear()
        counter += 1

    else:
        angle1 = random.randint(0, 180)
        angle2 = random.randint(0, 120)
        st = random.randint(100, 400)
        for i in range(3): ranges.append(random.randint(10, 500))

        Prlpd = np.array([[0, 0, 0, 1],
                           [st, 0, 0, 1],
                           [st, st, 0, 1],
                           [0, st, 0, 1],
                           [0, 0, st, 1],
                           [st, 0, st, 1],
                           [st, st, st, 1],
                           [0, st, st, 1]])

        f = np.array([[1, 0, 0, ranges[0]],
                      [0, 1, 0, ranges[1]],
                      [0, 0, 1, ranges[2]],
                      [1, 0, 0, 1]])  # по строках
        ft = f.T
        Prlpd = Prlpd.dot(ft)

        figure = Rotate(Prlpd, angle1, angle2)
        PrlpdWiz_Pixel_color_2(figure)
        # time.sleep(0.1)
        clear(win)
        ranges.clear()
        counter += 1
