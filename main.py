import pyray as rl


class Node:
    radius = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        rl.draw_circle(self.x, self.y, Node.radius, rl.BLACK)


WIDTH = 800
HEIGHT = 450

rl.init_window(WIDTH, HEIGHT, "Node and Edges")

nodes: list[Node] = [
    Node(WIDTH // 2 - 100, HEIGHT // 2),
    Node(WIDTH // 2 + 100, HEIGHT // 2),
]

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)

    for node in nodes:
        node.draw()

    rl.end_drawing()

rl.close_window()
