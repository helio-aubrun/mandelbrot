import matplotlib.pyplot as plt
import numpy as np

#generation
def sierpinski_triangle(order, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()
    
    # Recursive function to draw the Sierpinski triangle
    def sierpinski(order, points, colors):
        if order == 0:
            if colors:  # Check if the colors list is not empty
                triangle = plt.Polygon(points, edgecolor='k', facecolor=colors.pop())
            else:
                triangle = plt.Polygon(points, edgecolor='k', facecolor='white')  # Default color if colors is empty
            ax.add_patch(triangle)
        else:
            mid_points = [(points[i] + points[(i+1)%3]) / 2 for i in range(3)]
            sierpinski(order-1, [points[0], mid_points[0], mid_points[2]], colors[:])
            sierpinski(order-1, [points[1], mid_points[0], mid_points[1]], colors[:])
            sierpinski(order-1, [points[2], mid_points[1], mid_points[2]], colors[:])
    
    # Color generation
    colors = ['white','black'] * ((order // 3) + 1)
    
    points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    sierpinski(order, points, colors)
    plt.show()

#display
def display_sierpinski():
    sierpinski_triangle(5)