def print_dijkstra_path(end_node, neighbour_node):
    path = ""
    path = end_node + "->" + path
    while True:
        end_node = neighbour_node[end_node]
        if end_node is None:
            path += ""
            break
        path = end_node + "->" + path

    print("Following is the Dijkstra algorithm:")
    print("Path (Dijsktra) =", path[:-2])
    return path[:-2]


def dijkstra(graph, start_node, end_node):
    path = dict()
    neighbour_node = dict()
    unvisited_nodes = []

    for node in graph:
        path[node] = float("inf")  # lowest path cost
        neighbour_node[node] = None
        unvisited_nodes.append(node)

    path[start_node] = 0

    while unvisited_nodes:
        key_min = unvisited_nodes[0]
        min_val = path[key_min]
        for i in range(1, len(unvisited_nodes)):
            if path[unvisited_nodes[i]] < min_val:
                key_min = unvisited_nodes[i]
                min_val = path[key_min]
        curr = key_min
        unvisited_nodes.remove(curr)

        for node in graph[curr]:
            new_path = graph[curr][node] + path[curr]
            if path[node] > new_path:
                path[node] = new_path
                neighbour_node[node] = curr

    return print_dijkstra_path(end_node, neighbour_node)


# breadth-first search
def bfs(graph, start_node, end_node):
    visited = []
    queue = [[start_node]]

    if start_node == end_node:
        print("Same Node!")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        # If current node is not visited
        if node not in visited:
            neighbours = graph[node]

            # Iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # If neighbour node is destination
                if neighbour == end_node:
                    print("Following is the Breadth-First Search:")
                    print("Path (BFS) = ", *new_path)  # print list as string
                    return new_path
            visited.append(node)

    print("Connecting path doesn't exist!")
    return
