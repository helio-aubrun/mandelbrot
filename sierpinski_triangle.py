import numpy as np
import matplotlib.pyplot as plt

def sierpinski_triangle(order, ax, color='darkblue'):
    def sierpinski(coords, order):
        if order == 0:
            ax.fill(coords[:, 0], coords[:, 1], color)
        else:
            for i in range(3):
                sierpinski((coords + coords[[i-1]] + coords[[i]]) / 2, order - 1)
    
    coords = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    sierpinski(coords, order)
    ax.set_aspect('equal')
    ax.axis('off')

def display_sierpinski_triangle():
    fig, ax = plt.subplots(figsize=(8, 8))
    sierpinski_triangle(5, ax)
    plt.title("Sierpinski Triangle", fontsize=20)
    plt.show()
