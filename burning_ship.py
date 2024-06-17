import numpy as np
import matplotlib.pyplot as plt

#formule du burning ship
def burning_ship(c, max_iter):
    z = c
    for n in range(max_iter):
        z = complex(abs(z.real), abs(z.imag)) ** 2 + c
        if abs(z) > 2:
            return n
    return max_iter

#generation du burning ship en utilisant la fotmule
def generate_burning_ship(xmin, xmax, ymin, ymax, width, height, max_iter):
    ligne = np.linspace(xmin, xmax, width)
    colmn = np.linspace(ymin, ymax, height)
    image = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            image[i, j] = burning_ship(ligne [i] + 1j * colmn [j], max_iter)
    return image

#affichage
def display_burning_ship():
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 800, 600
    max_iter = 40

    image = generate_burning_ship(xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.imshow(image, extent=[xmin, xmax, ymin, ymax], cmap='GnBu_r')
    plt.colorbar()
    plt.axis('off')
    plt.axis('equal')
    plt.title('Burning Ship Fractal')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()
