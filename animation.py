import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Formula for the Koch curve
def koch_curve(order, p1, p2):
    if order == 0:
        return [p1, p2]
    else:
        p1 = np.array(p1)
        p2 = np.array(p2)
        s = (p2 - p1) / 3
        p3 = p1 + s
        p4 = p1 + 2 * s
        p5 = p3 + np.dot([[0.5, -np.sqrt(3)/2], [np.sqrt(3)/2, 0.5]], s)
        return (koch_curve(order - 1, p1, p3) +
                koch_curve(order - 1, p3, p5) +
                koch_curve(order - 1, p5, p4) +
                koch_curve(order - 1, p4, p2))

# Initialize points and use the Koch snowflake formula
def koch_snowflake(order, scale=10):
    p1 = [0, 0]
    p2 = [scale, 0]
    p3 = [scale / 2, scale * np.sqrt(3) / 2]
    return (koch_curve(order, p1, p2) +
            koch_curve(order, p2, p3) +
            koch_curve(order, p3, p1))

# Animation update function
def update(frame):
    order = frame // 10 + 1
    snowflake = koch_snowflake(order)
    snowflake = np.array(snowflake)
    
    ax.clear()
    ax.plot(snowflake[:, 0], snowflake[:, 1], 'b-')
    ax.set_title(f'Koch Snowflake - Order {order}')
    ax.axis('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots()

# Number of orders to animate (from 1 to 8 inclusive)
max_order = 8
frames_per_order = 10
total_frames = frames_per_order * (max_order - 1)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(total_frames), repeat=False)

# Display the animation
plt.show()
