import numpy as np
import matplotlib.pyplot as plt

#formule 
def julia(c, max_iter):
    def julia_iter(z):
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter
    
    return np.vectorize(julia_iter)

#generation 
def julia_set(xmin,xmax,ymin,ymax,width,height,max_iter,c):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    julia_fractal = julia(c, max_iter)
    return julia_fractal(Z)

#affichage
def display_julia():
    xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
    width, height, max_iter = 800, 800, 256
    c = complex(-0.7, 0.27015)

    julia_fractal = julia_set(xmin, xmax, ymin, ymax, width, height, max_iter, c)

    plt.figure(figsize=(10, 10))
    plt.imshow(julia_fractal, extent=[xmin, xmax, ymin, ymax], cmap='viridis')
    plt.colorbar()
    plt.title("Julia Set", fontsize=20)
    plt.axis('off')
    plt.show()
