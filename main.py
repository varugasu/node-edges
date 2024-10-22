import pyray as rl
from components import Node, Edges, LayoutController
from constants import WIDTH, HEIGHT

graph = {
    "A": ["B"],
    "B": ["A"],
}

rl.init_window(WIDTH, HEIGHT, "Node and Edges")

layout_controller = LayoutController(graph)

nodes: dict[str, Node] = {}
for node_id, (x, y) in layout_controller.get_node_position():
    nodes[node_id] = Node(node_id, x, y)

edges = Edges(graph, nodes)


while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)

    for node in nodes.values():
        node.draw()
    edges.draw()

    rl.end_drawing()

rl.close_window()
