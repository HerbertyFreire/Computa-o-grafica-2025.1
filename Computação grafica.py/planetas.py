from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
import random


class SolarSystem:
    def __init__(self):
        # Ângulos de rotação
        self.angle_planet1 = 0
        self.angle_planet2 = 0
        self.angle_moon1 = 0
        self.angle_moon2 = 0

        # Controle da animação
        self.running = False

        # Gerar estrelas aleatórias no fundo
        self.stars = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(200)]

        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutCreateWindow(b"Simulacao de Planetas - Estetica Melhorada")

        self.init_gl()

      
        glutDisplayFunc(self.draw_scene)
        glutKeyboardFunc(self.keyboard)
        glutTimerFunc(30, self.update, 0)

        glutMainLoop()

    def init_gl(self):
        glClearColor(0.0, 0.0, 0.05, 1.0)  # Fundo escuro (espaço)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        # Projeção 
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)

    def draw_stars(self):
      
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POINTS)
        for x, y in self.stars:
            glVertex2f(x, y)
        glEnd()

    def draw_orbit(self, radius):
        glColor3f(0.3, 0.3, 0.3)  # cinza claro
        glBegin(GL_LINE_LOOP)
        for i in range(100):
            theta = 2 * math.pi * i / 100
            glVertex2f(radius * math.cos(theta), radius * math.sin(theta))
        glEnd()

    def draw_sun(self):
        
        glColor3f(1.0, 1.0, 0.0)
        glutSolidSphere(0.12, 40, 40)

    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Estrelas de fundo
        self.draw_stars()

        # Sol
        self.draw_sun()

        # Órbita planeta 1
        self.draw_orbit(0.5)

        # Planeta 1 (azul)
        glPushMatrix()
        glRotatef(self.angle_planet1, 0, 0, 1)
        glTranslatef(0.5, 0.0, 0.0)
        glColor3f(0.1, 0.4, 1.0)
        glutSolidSphere(0.06, 30, 30)

        # Órbita Lua 1
        self.draw_orbit(0.12)

        # Lua 1
        glPushMatrix()
        glRotatef(self.angle_moon1, 0, 0, 1)
        glTranslatef(0.12, 0.0, 0.0)
        glColor3f(0.7, 0.7, 0.7)
        glutSolidSphere(0.025, 15, 15)
        glPopMatrix()

        # Lua 2 (outra órbita)
        glPushMatrix()
        glRotatef(self.angle_moon2, 1, 1, 0)
        glTranslatef(0.15, 0.12, 0.0)
        glColor3f(0.9, 0.9, 0.9)
        glutSolidSphere(0.02, 15, 15)
        glPopMatrix()
        glPopMatrix()

        # Órbita planeta 2
        self.draw_orbit(0.7)

        # Planeta 2 (vermelho)
        glPushMatrix()
        glRotatef(self.angle_planet2, 0, 0, 1)
        glTranslatef(-0.7, 0.0, 0.0)
        glColor3f(1.0, 0.3, 0.3)
        glutSolidSphere(0.07, 30, 30)
        glPopMatrix()

        glutSwapBuffers()

    def update(self, value):
        if self.running:
            self.angle_planet1 -= 1.5
            self.angle_planet2 += 1.5
            self.angle_moon1 -= 4
            self.angle_moon2 += 3
            glutPostRedisplay()
        glutTimerFunc(30, self.update, 0)

    def keyboard(self, key, x, y):
        if key in (b'y', b'Y'):
            self.running = not self.running


if __name__ == "__main__":
    SolarSystem()

