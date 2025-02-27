import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Define the 3D cube vertices
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the surfaces (faces) of the cube
surfaces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
]

# Define colors for the cube faces
colors = [
    (1, 0, 0),  # red
    (0, 1, 0),  # green
    (0, 0, 1),  # blue
    (1, 1, 0),  # yellow
    (1, 0, 1),  # magenta
    (0, 1, 1)   # cyan
]

# Function to draw a single cube
def draw_cube():
    glBegin(GL_QUADS)
    for surface, color in zip(surfaces, colors):
        glColor3fv(color)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Black for edges
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Function to initialize the game window
def init_game():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Function to handle user input for camera movement
def handle_input():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glTranslatef(0.1, 0, 0)
    if keys[K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keys[K_UP]:
        glTranslatef(0, 0.1, 0)
    if keys[K_DOWN]:
        glTranslatef(0, -0.1, 0)

# Function to generate a random 3D world of cubes
def generate_world():
    world = []
    for x in range(-5, 5):
        for y in range(-5, 5):
            for z in range(-5, 5):
                if random.random() > 0.7:  # 30% chance to generate a block
                    world.append((x, y, z))
    return world

# Main game loop
def game_loop():
    init_game()
    world = generate_world()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_input()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for block in world:
            glPushMatrix()
            glTranslatef(block[0], block[1], block[2])
            draw_cube()
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    game_loop()
