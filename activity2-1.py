from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def printShapes():
    # points
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(100, 100)
    glVertex2f(300, 200)
    glEnd()

    # rectangle
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(300, 100)
    glVertex2f(300, 200)
    glVertex2f(100, 200)
    glEnd()

    # triangle
    glBegin(GL_TRIANGLES)
    glVertex2f(300, 210)
    glVertex2f(100, 210)
    glVertex2f(300, 300)
    glEnd()


def loop():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def view():
    glClearColor(1, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    loop()
    printShapes()
    glColor3f(0.2, 0.5, 0.4)
    glutSwapBuffers()


glutInit()

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)

window = glutCreateWindow("Activity 1")

glutDisplayFunc(view)
glutIdleFunc(view)

glutMainLoop()
