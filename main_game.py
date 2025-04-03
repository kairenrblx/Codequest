import pyglet
from pyglet.window import key, mouse
import json
import os
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

# Load world data
def load_world(filename="worldgen/world.json"):
    if not os.path.exists(filename):
        print("World file not found! Generate a world first.")
        return {}
    with open(filename, "r") as f:
        return json.load(f)

# Setup Pyglet window
window = pyglet.window.Window(width=800, height=600, caption="Custom PythonCraft", resizable=True)
glEnable(GL_DEPTH_TEST)

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, window.width / window.height, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def draw_block(x, y, z):
    vertices = np.array([
        [x, y, z], [x+1, y, z], [x+1, y+1, z], [x, y+1, z],
        [x, y, z+1], [x+1, y, z+1], [x+1, y+1, z+1], [x, y+1, z+1]
    ])
    edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3f(*vertices[vertex])
    glEnd()

world = load_world()

@window.event
def on_draw():
    window.clear()
    set_3d()
    glLoadIdentity()
    gluLookAt(30, 30, 30, 0, 0, 0, 0, 1, 0)
    
    for key in world.keys():
        x, y, z = map(int, key.split(","))
        draw_block(x, y, z)

pyglet.app.run()
