from collections import defaultdict
from typing import Generator
import pyray as rl
from constants import WIDTH, HEIGHT
import math


class Node:
    radius = 40

    def __init__(self, id: str, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def draw(self):
        rl.draw_circle(self.x, self.y, Node.radius, rl.BLACK)


class Edges:
    arrow_length = 10

    def __init__(self, graph: dict[str, list[str]], nodes: dict[str, Node]):
        self.graph = graph
        self.nodes = nodes
        self.node_edges: dict[str, list[dict[str, Node]]] = defaultdict(list)
        self.edge_count: dict[str, int] = defaultdict(int)
        for node_id, neighbors in self.graph.items():
            for neighbor_id in neighbors:
                self.node_edges[node_id].append(
                    {"from": self.nodes[node_id], "to": self.nodes[neighbor_id]}
                )
                self.edge_count[node_id] += 1
                self.edge_count[neighbor_id] += 1

    def get_node_edges(self, node_id: str) -> list[dict[str, Node]]:
        return self.node_edges[node_id]

    def draw(self):
        for edges in self.node_edges.values():
            for edge in edges:
                vx = edge["to"].x - edge["from"].x
                vy = edge["to"].y - edge["from"].y
                vector_length = math.sqrt(vx**2 + vy**2)
                normalized_vx = vx / vector_length
                normalized_vy = vy / vector_length

                from_x = int(edge["from"].x + Node.radius * normalized_vx)
                from_y = int(edge["from"].y + Node.radius * normalized_vy)

                to_x = int(edge["to"].x - Node.radius * normalized_vx)
                to_y = int(edge["to"].y - Node.radius * normalized_vy)

                rl.draw_line_ex(
                    rl.Vector2(from_x, from_y),
                    rl.Vector2(to_x, to_y),
                    4,
                    rl.BLACK,
                )

                arrow_direction = 1 if to_x > from_x else -1
                arrow_offset = 10 * arrow_direction * -1

                v1 = (to_x + arrow_offset, to_y - self.arrow_length * arrow_direction)
                v2 = (to_x + arrow_offset, to_y + self.arrow_length * arrow_direction)
                v3 = (to_x, to_y)

                rl.draw_triangle(
                    rl.Vector2(*v1),
                    rl.Vector2(*v2),
                    rl.Vector2(*v3),
                    rl.BLACK,
                )


class LayoutController:
    def __init__(self, graph: dict[str, list[str]]):
        self.graph = graph

    def get_node_position(self) -> Generator[tuple[str, tuple[int, int]], None, None]:
        positions = [(WIDTH // 2 - 100, HEIGHT // 2), (WIDTH // 2 + 100, HEIGHT // 2)]
        for node_id, position in zip(self.graph, positions):
            yield node_id, position
