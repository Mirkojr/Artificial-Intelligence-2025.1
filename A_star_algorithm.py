#Made by Marcos 30/04/2025

import heapq #Library for a min-heap 

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def A_star(graph_AdjList: dict, graph_edges:dict, start, goal, h):

    nodes_heap = [] #heap used to store the nodes we're going to use later
    heapq.heappush(nodes_heap, start)

    cameFrom = {}   #cameFrom[n] for a node n, its the parent of this node

    #gScore[n], for a node n, its the cheapest currently known path from start to n
    gScore = dict.fromkeys(graph_AdjList.keys(), None) #initializing every node score with None to represent infinity
    gScore[start] = 0                        

    #fScore[n] = gScore[n] + h(n), for a node n, its our best guess as to how cheap a path could be from start to finish if it goes through n
    fScore = dict.fromkeys(nodes_heap, None) #initializing every node best guess with None to represent infinity
    fScore[start] = h[start]

    while nodes_heap != []:
        current = heapq.heappop(nodes_heap)

        if current == goal:
            return reconstruct_path(cameFrom, current)

        for neighbor in graph_AdjList[current]:

            edge_weight = graph_edges[(current, neighbor)] if (current, neighbor) in graph_edges else graph_edges[(neighbor, current)] 

            tentative_gScore = gScore[current] + edge_weight
            if  (gScore[neighbor] == None) or (tentative_gScore < gScore[neighbor]):
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h[neighbor]

                if neighbor not in nodes_heap:
                    heapq.heappush(nodes_heap, neighbor)
    return False
def main ():
    # Example graph represented as an adjacency list (using AI to make this example)
    graph_AdjList = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Example graph edges with weights
    graph_edges = {
        ('A', 'B'): 1,
        ('A', 'C'): 2,
        ('B', 'D'): 4,
        ('B', 'E'): 2,
        ('C', 'F'): 3,
        ('E', 'F'): 1,
    }

    # Example heuristic function (h)
    h = {
        'A': 6,
        'B': 5,
        'C': 2,
        'D': 1,
        'E': 0,
        'F': 3
    }

    start = 'A'
    goal = 'F'

    print(A_star(graph_AdjList, graph_edges, start, goal, h))

if __name__ == "__main__":
    main()