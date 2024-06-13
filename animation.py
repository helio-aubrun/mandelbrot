import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def update_fig(extent):
    x, y, z = mandelbrot_set(extent[0], extent[1], extent[2], extent[3], img_width, img_height, max_iter)
    ax.imshow(z.T, origin='lower', cmap='hot', extent=extent)
    return ax

fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)

xmin, xmax, ymin, ymax = -2.0, 0.5, -1.25, 1.25
width, height = 10, 10
dpi = 80
img_width = dpi * width
img_height = dpi * height
max_iter = 256

extent = [xmin, xmax, ymin, ymax]

def zoom_animation(frame):
    global extent
    zoom_factor = 0.9
    x_center = (extent[0] + extent[1]) / 2
    y_center = (extent[2] + extent[3]) / 2
    width = (extent[1] - extent[0]) * zoom_factor
    height = (extent[3] - extent[2]) * zoom_factor
    extent = [x_center - width/2, x_center + width/2, y_center - height/2, y_center + height/2]
    return update_fig(extent)

ani = animation.FuncAnimation(fig, zoom_animation, frames=30, repeat=False)
plt.show()