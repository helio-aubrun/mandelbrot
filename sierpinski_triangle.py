import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(order, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()
    
    # Fonction récursive pour dessiner le triangle de Sierpinski
    def sierpinski(order, points, colors):
        if order == 0:
            if colors:  # Vérifie si la liste colors n'est pas vide
                triangle = plt.Polygon(points, edgecolor='k', facecolor=colors.pop())
            else:
                triangle = plt.Polygon(points, edgecolor='k', facecolor='white')  # Couleur par défaut si colors est vide
            ax.add_patch(triangle)
        else:
            mid_points = [(points[i] + points[(i+1)%3]) / 2 for i in range(3)]
            sierpinski(order-1, [points[0], mid_points[0], mid_points[2]], colors[:])
            sierpinski(order-1, [points[1], mid_points[0], mid_points[1]], colors[:])
            sierpinski(order-1, [points[2], mid_points[1], mid_points[2]], colors[:])
    
    # Génération des couleurs
    colors = ['white','black'] * ((order // 3) + 1)
    
    points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    sierpinski(order, points, colors)
    plt.show()

def display_sierpinski():
    sierpinski_triangle(5)

display_sierpinski()