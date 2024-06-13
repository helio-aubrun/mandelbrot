import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def sierpinski_triangle(order, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()
    
    def sierpinski(order, points):
        if order == 0:
            triangle = plt.Polygon(points, edgecolor='k', facecolor='white')
            ax.add_patch(triangle)
        else:
            mid_points = [(points[i] + points[(i+1)%3]) / 2 for i in range(3)]
            sierpinski(order-1, [points[0], mid_points[0], mid_points[2]])
            sierpinski(order-1, [points[1], mid_points[0], mid_points[1]])
            sierpinski(order-1, [points[2], mid_points[1], mid_points[2]])

    points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    sierpinski(order, points)
    plt.show()

sierpinski_triangle(order=5)
