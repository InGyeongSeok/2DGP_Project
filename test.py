import numpy as np
import matplotlib.pyplot as plt

def cycloid(t, r, x_offset, y_offset):
    x = r * (t - np.sin(t)) + x_offset
    y = r * (1 - np.cos(t)) + y_offset
    return x, y

def generate_diagonal_cycloid(start, end, r=1):
    x_start, y_start = start
    x_end, y_end = end

    # Calculate the angle parameter corresponding to the start and end points using arctan
    t_start = np.arctan2(y_start - y_end, x_start - x_end)
    t_end = np.arctan2(y_end - y_start, x_end - x_start)

    # Generate points along the cycloid between the specified angle range
    t_values = np.linspace(t_start, t_end, 100)
    x_values, y_values = cycloid(t_values, r, x_start, y_start)

    return x_values, y_values

# Set the start and end points
start_point = (0, 0)
end_point = (10, 10)

# Set the radius of the cycloid
radius = 1

# Generate diagonal cycloid points
x_cycloid, y_cycloid = generate_diagonal_cycloid(start_point, end_point, radius)

# Plot the results
plt.plot(x_cycloid, y_cycloid, label='Diagonal Cycloid')
plt.scatter([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='red', marker='o', label='Start/End Points')
plt.title('Diagonal Cycloid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
