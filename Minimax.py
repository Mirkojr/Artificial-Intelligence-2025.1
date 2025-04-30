#Made by Marcos Jr 30/04/2025
#Algorithm Minimax made in AI class following teacher's example


tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [3, 5],
        "E": [6, 9],
        "F": [1, 2],
        "G": [0, -1]
    }

minimax_log = []

def minimax(node, is_maximizing):
    if isinstance(node, int): #if its a leaf, then return it
        return node
    
    if isinstance(tree[node][0], int): #leaf with trees
        values = tree[node]
        result = max(values) if is_maximizing else min(values)
        minimax_log.append((node, values, result))
        return result

    #recursion on childs alternating between max and min
    values = [minimax(child, not is_maximizing) for child in tree[node]]
    result = max(values) if is_maximizing else min(values)  
    minimax_log.append((node, values, result)) 
    return result

# Execute minmax starting from "A"
resultado_minimax = minimax("A", True)

#Exibit the logs

print("Question 1: Minimax")

for log in minimax_log:
    print(f"Node {log[0]}: Children {log[1]}, Result {log[2]}")

print(f"Optimal value for the root node 'A': {resultado_minimax}")

