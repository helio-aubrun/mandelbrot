import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def display(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256):
    dpi = 80
    img_width = dpi * width
    img_height = dpi * height

    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ticks = np.arange(0, img_width, 3*dpi)
    x_ticks = xmin + (xmax - xmin) * ticks / img_width
    y_ticks = ymin + (ymax - ymin) * ticks / img_width

    ax.set_xticks(ticks); ax.set_xticklabels(x_ticks)
    ax.set_yticks(ticks); ax.set_yticklabels(y_ticks)

    ax.imshow(z.T, origin='lower', cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.show()

display(-2.0, 0.5, -1.25, 1.25)
