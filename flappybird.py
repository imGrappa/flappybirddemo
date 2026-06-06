from ursina import *
import random

app = Ursina()
camera.orthographic = True
camera.fov = 10
window.color = color.cyan

bird = Entity(model='quad', texture='white_cube', color=color.yellow, scale=.6, x=-3, collider="box")
start = Text("Space ile başla", origin=(0,0), scale=2)

v, started =  0, False
jump, gravity, speed, gap_size = 4, 15, 3, 3.5
pipes = []

def pipe(x):
    gap = random.uniform(-1,1)
    top = Entity(model="quad", color=color.green, scale=(.8,4),
                 position=(x, gap+gap_size,0), collider="box")
    bottom = Entity(model="quad", color=color.green, scale=(.8,4),
                    position=(x, gap-gap_size,0), collider="box")
    pipes.append((top, bottom))

for x in (4, 8, 12):
    pipe(x)

def input(key):
    global v, started
    if key == 'space':
        v = jump
        started = True
        start.enabled = False

def update():
    global v
    if not started: return

    bird.y += v * time.dt
    v = max(v - gravity * time.dt, -4)

    for top, bottom in pipes:
        top.x -= speed * time.dt
        bottom.x -= speed * time.dt

        if top.x < -6:
            gap = random.uniform(-1,1)
            top.position = (8, gap+gap_size,0)
            bottom.position = (8, gap-gap_size,0)

        if bird.intersects(top).hit or bird.intersects(bottom).hit:
            application.quit()
        
    if abs(bird.y) > 5:
        application.quit()

app.run()