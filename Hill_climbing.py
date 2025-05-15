import random
import math 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return x**2 + y**2 + 25 * ((np.sin(x))**2 + (np.sin(y))**2)


def hill_climbing(func, x_start, y_start, step_size=0.1, max_iterations=100000000000000000):
    x = x_start
    y = y_start
    best_value = func(x, y)
    best_x = x
    best_y = y

    for _ in range(max_iterations):
        
        # Generate neighbors
        neighbors = [
            (x + step_size, y),
            (x - step_size, y),
            (x, y + step_size),
            (x, y - step_size)
        ]

        # Evaluate neighbors
        neighbor_values = [func(nx, ny) for nx, ny in neighbors]

        min_value = min(neighbor_values)
        min_index = neighbor_values.index(min_value)

        # If the best neighbor is better than the current point, move to it
        if min_value < best_value:
            x, y = neighbors[min_index]
            best_value = min_value
            best_x = x
            best_y = y
            
        else:
            break  # Stop if no better neighbor is found
    return best_x, best_y, best_value
# Example usage
x_start = random.uniform(0, 10)
y_start = random.uniform(0, 10)
best_x, best_y, best_value = hill_climbing(func, x_start, y_start)
print(f"Best x: {best_x}, Best y: {best_y}, Best value: {best_value}")

# Create a grid of x, y values
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

# Plot the 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Plot the best point found by hill climbing
ax.scatter(best_x, best_y, best_value, color='r', s=100, label='Best Point')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Visualization of the Function')
ax.legend()
plt.show()