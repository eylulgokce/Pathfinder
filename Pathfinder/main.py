import pathfinder as pf


def create_graph():
    return {
        'A': {'B': 5, 'D': 1},
        'B': {'A': 3, 'C': 1},
        'C': {'A': 10, 'G': 4},
        'D': {'E': 3},
        'E': {'C': 2},
        'F': {'A': 2, 'D': 7, 'G': 4},
        'G': {'C': 1, 'E': 1, 'F': 1}
    }


if __name__ == '__main__':

    graph = create_graph()
    start_node = "F"
    end_node = "C"

    print("The path between", start_node, "to", end_node)

    pf.bfs(graph, start_node, end_node)
    pf.dijkstra(graph, start_node, end_node)



