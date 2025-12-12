import os
import fileinput
import math

os.chdir('./day-8/')

# a solution with a very janky graph model using "adjacency sets"
# part 2: even jankier patch to count connected boxes

class Vector3i:

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z
    
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __repr__(self):
        return self.__str__()
    
    def distance_to(self, v: Vector3i) -> float:
        dx: int = v.x - self.x
        dy: int = v.y - self.y
        dz: int = v.z - self.z
        return math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))
    
class JunctionBox:

    next_id: int = 0

    def __init__(self, position: Vector3i) -> None:
        self.position: Vector3i = position
        self.is_connected: bool = False
        self.id: int = JunctionBox.next_id
        JunctionBox.next_id += 1

    def __str__(self):
        return f'[{self.id} {self.position}]'

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, JunctionBox):
            return NotImplemented
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    
    def distance_to(self, j: JunctionBox) -> float:
        return self.position.distance_to(j.position)

class Edge:

    def __init__(self, box_from: JunctionBox, box_to: JunctionBox, is_connected: bool = False) -> None:
        self.boxes: set[JunctionBox] = {box_from, box_to}
        self.distance: float = box_from.distance_to(box_to)
        self.is_connected: bool = is_connected
 
    def __str__(self):
        b: list[JunctionBox] = list(self.boxes)
        c: str = '*' if self.is_connected else '-'
        return f'({b[0]}{c}{b[1]})'

    def __repr__(self):
        return self.__str__()
     
    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented
        return self.boxes == other.boxes

    def __hash__(self):
        return hash(frozenset(self.boxes))
    
    def contains_box(self, box: JunctionBox) -> bool:
        return len(self.boxes.intersection({box})) > 0
    
    def get_other_box(self, not_box: JunctionBox) -> JunctionBox:
        return list(self.boxes.difference({not_box}))[0]
    
class Circuit:

    def __init__(self, edge: Edge) -> None:
        self.edges: set[Edge] = {edge}
    
    def add(self, new_edge: Edge) -> bool:
        for e in self.edges:
            if e.boxes.intersection(new_edge.boxes) and new_edge.is_connected:
                self.edges.add(new_edge)
                return True
        
        return False
    
    #def remove(self, e: Edge) -> bool:
    #    if e in self.edges:
    #        self.edges.remove(e)
    #        return True
    #    else:
    #        return False
    
    def size(self) -> int:
        return len(self.edges)
    
    def is_empty(self) -> bool:
        return len(self.edges) == 0

class LightsDecor:

    def __init__(self, boxes: list[JunctionBox]) -> None:
        self.junction_boxes: set[JunctionBox] = set(boxes)
        self.connections: set[Edge] = set()
        self.connected_box_order: list[JunctionBox] = []

        self._generate_connections()

    def __str__(self):
        return f'{{{self.junction_boxes} ({self.connections})}}'

    def __repr__(self):
        return self.__str__()

    def connect_edge(self, edge: Edge) -> None:
        edge.is_connected = True
        new_boxes: list[JunctionBox] = []
        for box in edge.boxes:
            if not box.is_connected:
                box.is_connected = True
                self.connected_box_order.append(box)
    
    #def disconnect_edge(self, edge: Edge) -> None:
    #    edge.is_connected = False

    def identify_circuit_with(self, e: JunctionBox) -> set[Edge]:
        ...
    
    def _generate_connections(self) -> None:
        for box_a in self.junction_boxes:
            for box_b in self.junction_boxes:
                if box_a != box_b:
                    self.connections.add(Edge(box_a, box_b))
    
    def find_connected_path(self, box_from: JunctionBox, box_to: JunctionBox):
        connected: set[Edge] = set([edge for edge in self.connections if edge.is_connected])

        def find_path(connected: set[Edge], box_from: JunctionBox, box_to: JunctionBox, path: list[JunctionBox]):
            path.append(box_from)
            if box_from == box_to:
                return path
            with_edge: set[Edge] = {edge for edge in connected if edge.contains_box(box_from)}
            for edge in with_edge:
                if edge.get_other_box(box_from) not in path:
                    new_path: list[JunctionBox] = find_path(connected, edge.get_other_box(box_from), box_to, path)
                    if new_path:
                        return new_path
            return []

        return find_path(connected, box_from, box_to, [])

    def closest_connections(self, top_limit: int = -1) -> list[Edge]:
        if top_limit == -1:
            return sorted(self.connections, key=lambda connection: connection.distance)
        else:
            return sorted(self.connections, key=lambda connection: connection.distance)[:top_limit]

    def identify_circuits(self) -> list[set[Edge]]:
        connected: set[Edge] = set([edge for edge in self.connections if edge.is_connected])
        circuits: list[set[Edge]] = []
        
        while len(connected) > 0:
            found: list[set[Edge]] = []
            edge: Edge = connected.pop()
            for c in circuits:
                for e in c:
                    if len(e.boxes.intersection(edge.boxes)) > 0:
                        found.append(c)
                        break
            if found:
                new_circuit: set[Edge] = {edge}
                for f in found:
                    new_circuit.update(list(f))
                    circuits.remove(f)
                circuits.append(new_circuit)
            else:
                circuits.append({edge})
        return circuits
    
    def circuit_size(self, circuit: set[Edge]) -> int:
            boxes: set[JunctionBox] = set()
            for e in circuit:
                boxes.update(e.boxes)
            return len(boxes)
    
    def circuit_sizes(self, circuits: list[set[Edge]]) -> list[int]:
        return list(map(self.circuit_size, circuits))

    # didn't even need this, oops
    # def connected_boxes(self) -> list[JunctionBox]:
    #    return [box for box in self.junction_boxes if box.is_connected]

def main():
    
    input_file: str = 'input.txt'

    # parse file
    lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]
    positions: list[Vector3i] = [Vector3i(*map(int, line.split(','))) for line in lines]
    lights: LightsDecor = LightsDecor([JunctionBox(position) for position in positions])
    
    closest_pairs: list[Edge] = lights.closest_connections()
    closest_pairs.reverse()
    
    # didn't really need the *order* of boxes, but here we are
    last_edge: Edge | None = None
    while closest_pairs and len(lights.connected_box_order) < len(lights.junction_boxes):
        edge: Edge = closest_pairs.pop()
        lights.connect_edge(edge)
        last_edge = edge
        print(edge)

    # we need the two boxes from just the last EDGE
    if last_edge:
        last_x_pos: list[int] = [(b.position).x for b in last_edge.boxes]
        print(last_edge, last_x_pos, math.prod(last_x_pos))

if __name__ == '__main__':
    main()