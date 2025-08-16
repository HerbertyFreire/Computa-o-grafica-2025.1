import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFlor():
  
    glClearColor(0.0, 0.0, 0.0, 0.0)
    
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)

def florFunc():
   
    glClear(GL_COLOR_BUFFER_BIT)

    
    glColor3f(0.0, 0.5, 0.0)  
    glBegin(GL_POLYGON)
    glVertex2i(245, 0)
    glVertex2i(255, 0)
    glVertex2i(255, 200)
    glVertex2i(245, 200)
    glEnd()

    
    glColor3f(1.0, 1.0, 0.0)  
    glBegin(GL_POLYGON)
    glVertex2i(240, 200)
    glVertex2i(260, 200)
    glVertex2i(260, 220)
    glVertex2i(240, 220)
    glEnd()

   
    glColor3f(1.0, 0.0, 0.0) 

    # Pétala de cima
    glBegin(GL_POLYGON)
    glVertex2i(240, 220)
    glVertex2i(260, 220)
    glVertex2i(260, 260)
    glVertex2i(240, 260)
    glEnd()

   
    glBegin(GL_POLYGON)
    glVertex2i(260, 200)
    glVertex2i(300, 200)
    glVertex2i(300, 220)
    glVertex2i(260, 220)
    glEnd()

    
    glBegin(GL_POLYGON)
    glVertex2i(240, 160)
    glVertex2i(260, 160)
    glVertex2i(260, 200)
    glVertex2i(240, 200)
    glEnd()
    
    
    glBegin(GL_POLYGON)
    glVertex2i(200, 200)
    glVertex2i(240, 200)
    glVertex2i(240, 220)
    glVertex2i(200, 220)
    glEnd()

   
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow(b"Flor Simples")
    initFlor()
    glutDisplayFunc(florFunc)
    glutMainLoop()

if __name__ == "__main__":
    main()
