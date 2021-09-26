from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = [(1, -1, -1), (1, 1, -1),  (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1),  (-1, 1, 1)
            ]

edges = ((0, 1),  (0, 3), (0, 4),  (2, 1), (2, 3), (2, 7), (6, 3),  (6, 4),  (6, 7),  (5, 1), (5, 4), (5, 7)
         )


def changesize(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, width, height)
    gluPerspective(45.0, width/height, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


def cube():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(2.0, -3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0)

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)


    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glFlush()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

glutInitWindowPosition(300, 152)
glutInitWindowSize(985, 500)
glutCreateWindow("RED Cube")

glEnable(GL_DEPTH_TEST)

glutDisplayFunc(cube)
glutReshapeFunc(changesize)

glutMainLoop()
