from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

angle_planet1 = 0
angle_planet2 = 0
angle_moon1 = 0
angle_moon2 = 0
running = False


def draw_scene():
    global angle_planet1, angle_planet2, angle_moon1, angle_moon2

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(100):
        theta = 2.0 * math.pi * i / 100
        glVertex2f(0.1 * math.cos(theta), 0.1 * math.sin(theta))
    glEnd()

    glPushMatrix()
    glRotatef(angle_planet1, 0, 0, 1)
    glTranslatef(0.5, 0.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidSphere(0.05, 20, 20)

    glPushMatrix()
    glRotatef(angle_moon1, 0, 0, 1)
    glTranslatef(0.1, 0.0, 0.0)
    glColor3f(0.5, 0.5, 0.5)
    glutSolidSphere(0.02, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glRotatef(angle_moon2, 1, 1, 0)
    glTranslatef(0.12, 0.12, 0.0)
    glColor3f(0.7, 0.7, 0.7)
    glutSolidSphere(0.015, 10, 10)
    glPopMatrix()

    glPopMatrix()

    glPushMatrix()
    glRotatef(angle_planet2, 0, 0, 1)
    glTranslatef(-0.7, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(0.06, 20, 20)
    glPopMatrix()

    glutSwapBuffers()


def update(value):
    global angle_planet1, angle_planet2, angle_moon1, angle_moon2
    if running:
        angle_planet1 -= 2
        angle_planet2 += 2
        angle_moon1 -= 5
        angle_moon2 += 4
        glutPostRedisplay()
    glutTimerFunc(30, update, 0)


def keyboard(key, x, y):
    global running
    if key == b'Y' or key == b'y':
        running = not running


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Simulacao de Planetas")
    init()
    glutDisplayFunc(draw_scene)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(30, update, 0)
    glutMainLoop()


if __name__ == "__main__":
    main()
