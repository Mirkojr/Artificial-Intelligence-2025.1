import sys

tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [3, 5],
        "E": [6, 9],
        "F": [1, 2],
        "G": [0, -1]
    }

alphabeta_log = []
visited_nodes = 0
def alphabeta(node, alpha, beta, is_maximazing):
    global visited_nodes
    visited_nodes += 1

    if isinstance(node, int): #if its a leaf, then return it
        return node
    
    if isinstance(tree[node][0], int): #leaf with trees
        values = tree[node]
        result = max(values) if is_maximazing else min(values)
        alphabeta_log.append((node, values, result, alpha, beta, False))
        return result

    best = float('-inf') if is_maximazing else float('inf')
    prune = False
    values = []

    for child in tree[node]:
        val = alphabeta(child, alpha, beta, not is_maximazing)

        values.append(val)
        if is_maximazing:
            best = max(best, val)
            alpha = max(alpha, best)
        else:
            best = min(best, val)
            beta = min(beta, best)
        
        # Verifica se ocorre poda
        if beta <= alpha:
            prune = True
            break

    alphabeta_log.append((node, values, best, alpha, beta, prune))
    return best

# executing the algorithm beginning from the root node "A"
result = alphabeta("A", float('-inf'), float('inf'), True)

# printing the result
print("Result:", result)
print("Visited nodes:", visited_nodes)
print("\nAlpha-Beta Log:")
for entry in alphabeta_log:
    print(entry)
    