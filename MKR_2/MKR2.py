# --------------- ПРИКЛАД 1 технології створення реалістичних зображент з бібліотекою PyOpenGL ------
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
#--------------------- Оголошення глобальних змінних ------------------------------------------------
global xrot         # Величина оборту за віссю x
global yrot         # Величина оборту за віссю y
global ambient      # Розсіювання світла
global gcolor1      # Колір 1
global gcolor2      # Колір 2
global gcolor3      # Колір 3
global gcolor4      # Колір 4
global gcolor5      # Цвет 5
global lightpos     # Положення джерела світла
#--------------------- Ініціалізація вихідних даних та параметрів ----------------------------------
def init():
    global xrot         # Величина оборту за віссю  x
    global yrot         # Величина оборту за віссю  y
    global ambient      # Розсіювання світла
    global gcolor1      # Колір 1
    global gcolor2      # Колір 2
    global gcolor3      # Колір 3
    global gcolor4      # Колір 4
    global gcolor5      # Колір 5
    global lightpos     # Положення джерела світла
    # ----------------- характеристики фігури------------------------------
    xrot = 0.0                          # Величина оборту за віссю x = 0
    yrot = 0.0                          # Величина оборту за віссю = 0
    ambient = (1.0, 1.0, 1.0, 5)        # СВІТЛО: Трійка чисел - колір у форматі RGB, а остання - яскравість
    gcolor1 = (0.9, 0.3, 0.1, 0.8)      # Коллір фігур
    gcolor2 = (0.2, 0.8, 0.0, 0.8)      # Коллір фігури
    gcolor3 = (0.9, 0.8, 0.0, 0.8)      # Коллір фігури
    gcolor4 = (0.9, 0.6, 0.1, 0.8)      # Коллір фігури
    gcolor5 = (0.2, 0.4, 0.9, 0.8)      # Коллір фігури
    # ----------------- характеристики світла ------------------------------
    lightpos = (0.0, 0.0, 1.0)          # Положення джерела світла по віссям xyz
    glClearColor(0.5, 0.5, 0.5, 1.0)                # Сірий колір первинного окрасу
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Межи малювання: горизонталь, вертикаль
    glRotatef(-90, 1.0, 0.0, 0.0)                   # Зміщення по віссі Х на 90 грд.
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Встановлення моделі освітлення
    glEnable(GL_LIGHTING)                           # Включення освітлення
    glEnable(GL_LIGHT0)                             # Включення одного джерела світла
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Визначення положення джерела світла
#--------------------------- Обробка подій керуючих клавіш ---------------------------------------
def specialkeys(key, x, y):
    global xrot
    global yrot
    if key == GLUT_KEY_UP:      # До верху
        xrot -= 10.0
    if key == GLUT_KEY_DOWN:    # До низу
        xrot += 10.0
    if key == GLUT_KEY_LEFT:    # Ліворуч
        yrot -= 10.0
    if key == GLUT_KEY_RIGHT:   # Праворуч
        yrot += 10.0
    glutPostRedisplay()         # Виклик функції побудови графічної сцени
#--------------------------------- Побудова графічної сцени ---------------------------------------
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor
    global treecolor1

    glClear(GL_COLOR_BUFFER_BIT)                                # Очищення графічного вікна та заливка сірим
    glPushMatrix()                                              # Збереження поточного положення світла

    glPushMatrix()

    glRotatef(xrot-20, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    # ---------------------------Конус-------------------------------
    glTranslatef(0.5, 0.0, 0.3)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, gcolor4)
    glutSolidCone(0.35, 0.35, 20, 20)
    # ---------------------------Піраміда-------------------------------
    glRotatef(xrot + 120, 1.0, 0.0, 0.0)
    glRotatef(yrot+35, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    glTranslatef(0.1-0.8, -0.1, 0.1)
    s = 0.3
    glBegin(GL_TRIANGLES)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.9, 0.6))
    glVertex3f(0.0, s, 0.0)
    glVertex3f(-s, -s, s)
    glVertex3f(s, -s, s)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.7, 1, 0.9))
    glVertex3f(0.0, s, 0.0)
    glVertex3f(-s, -s, -s)
    glVertex3f(s, -s, -s)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.4, 1, 0.3))
    glVertex3f(0.0, s, 0.0)
    glVertex3f(-s, -s, -s)
    glVertex3f(-s, -s, s)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1, 0.9, 0.3))
    glVertex3f(0.0, s, 0.0)
    glVertex3f(s, -s, -s)
    glVertex3f(s, -s, s)



    glEnd()
    glPopMatrix()
    glutSwapBuffers()

    # Відображення графічної сцени
#--------------------------------- Реалізація викликів  ---------------------------------------
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # директива використання подвійної буферизації та моделі RGB
glutInitWindowSize(600, 600)                      # розміри графічного вікна
glutInitWindowPosition(500, 50)                    # положення графічного вікна відносно екрану монітора
glutInit(sys.argv)                                # ініціалізація OpenGl
glutCreateWindow(b"MKR_2 Babenko Victoria") # заголовок графічного вікна
init()                                            # Ініціалізація параметрів
glutDisplayFunc(draw)                             # Малювання сцени
glutSpecialFunc(specialkeys)                      # Керування сценою
glutMainLoop()                                    # Ініціалізація запуску
