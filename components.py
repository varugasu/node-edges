from collections import defaultdict
from typing import Generator
import pyray as rl
from constants import WIDTH, HEIGHT


class Node:
    radius = 40

    def __init__(self, id: str, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def draw(self):
        rl.draw_circle(self.x, self.y, Node.radius, rl.BLACK)


class Edges:
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
                rl.draw_line_ex(
                    rl.Vector2(edge["from"].x, edge["from"].y),
                    rl.Vector2(edge["to"].x, edge["to"].y),
                    4,
                    rl.BLACK,
                )


class LayoutController:
    def __init__(self, graph: dict[str, list[str]]):
        self.graph = graph

    def get_node_position(self) -> Generator[tuple[str, tuple[int, int]], None, None]:
        positions = [(WIDTH // 2 - 100, HEIGHT // 2), (WIDTH // 2 + 100, HEIGHT // 2)]
        for node_id, position in zip(self.graph, positions):
            yield node_id, position
