import math
import matplotlib.pyplot as plt
import numpy as np

def cycloid(t, r=1):
    x = r * (t - np.sin(t))
    y = r * (1 - np.cos(t))
    return x, y

def plot_cycloid(t_values, r=1):
    x_values, y_values = cycloid(t_values, r)
    plt.plot(x_values, y_values, label='Cycloid')
    plt.scatter([x_values[0], x_values[-1]], [y_values[0], y_values[-1]], color='red', marker='o', label='Start/End Point')
    plt.title('Cycloid Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# 예시
t_values = np.linspace(0, 6 * math.pi, 1000)  # 0부터 6π까지의 값으로 t를 생성
plot_cycloid(t_values)
