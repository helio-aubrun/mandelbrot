import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from sierpinski_triangle import display_sierpinski
from mandelbrot import display_mandelbrot
from julia import display_julia
from koch_snowflake import display_koch_snowflake
from burning_ship import display_burning_ship


root = tk.Tk()
root.title("Fractal Explorer")
root.geometry("700x600")
root.configure(bg="#1e1e2e")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14, "bold"), padding=10, background="#f0f0f5", foreground="#1e1e2e")
style.map("TButton", background=[("active", "#4f4f6f")], foreground=[("active", "#ffffff")])
style.configure("TLabel", font=("Helvetica", 18, "bold"), background="#1e1e2e", foreground="#f0f0f5")


title_label = ttk.Label(root, text="Fractal Explorer")
title_label.pack(pady=20)

#affichege de sierpinski
button_sierpinski = ttk.Button(root, text="Sierpinski Triangle", command=display_sierpinski)
button_sierpinski.pack(pady=10)

#affichege de mandelbrot
button_mandelbrot = ttk.Button(root, text="Mandelbrot Set", command=display_mandelbrot)
button_mandelbrot.pack(pady=10)

#affichege de julia
button_julia = ttk.Button(root, text="Julia Set", command=display_julia)
button_julia.pack(pady=10)

#affichege de koch
button_koch = ttk.Button(root, text="Koch Snowflake", command=display_koch_snowflake)
button_koch.pack(pady=10)

#affichege de burning_ship
button_burning_ship = ttk.Button(root, text="Burning Ship Fractal", command=display_burning_ship)
button_burning_ship.pack(pady=10)

#affichege du text en bas de l'ecran
footer_label = ttk.Label(root, text="Explore the beauty of fractals!")
footer_label.pack(pady=20)


root.mainloop()
