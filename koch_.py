import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Classe pour générer et animer la neige de Koch
class KochSnowflake:
    def __init__(self, order, scale, interval):  # Initialisation de l'objet
        # Paramètres initiaux
        self.order = order
        self.scale = scale
        self.interval = interval
        # Création de la figure et de l'axe pour l'affichage
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')  # Assure un rapport d'aspect égal pour éviter la distorsion
        self.ax.axis('off')  # Cache les axes pour une meilleure visualisation
        self.snowflake = self.generate_snowflake()  # Génère la neige de Koch pour le niveau de zoom actuel

    # Méthode récursive pour générer une courbe de Koch
    def koch_curve(self, order, p1, p2):
        if order == 0:
            return [p1, p2]
        else:
            p1 = np.array(p1)
            p2 = np.array(p2)
            s = (p2 - p1) / 3
            p3 = p1 + s
            p5 = p1 + 2 * s
            p4 = p3 + np.array([s[0] * 0.5 - np.sqrt(3) * s[1] / 2,
                                s[1] * 0.5 + np.sqrt(3) * s[0] / 2])
            # Récursion pour construire la courbe de Koch
            return self.koch_curve(order-1, p1, p3)[:-1] + self.koch_curve(order-1, p3, p4)[:-1] + self.koch_curve(order-1, p4, p5)[:-1] + self.koch_curve(order-1, p5, p2)

    # Génère la neige de Koch en combinant plusieurs courbes de Koch
    def generate_snowflake(self):
        p1 = [0, 0]
        p2 = [self.scale, 2]
        p3 = [self.scale/2, self.scale * np.sqrt(3)/2]
        # Utilise la méthode koch_curve pour générer les trois segments de la neige de Koch
        return self.koch_curve(self.order, p1, p2)[:-1] + self.koch_curve(self.order, p2, p3)[:-1] + self.koch_curve(self.order, p3, p1)[:-1]


    # Met à jour l'affichage pour chaque frame de l'animation
    def update(self, frame):
        self.ax.clear()  # Efface l'affichage précédent
        snowflake = self.snowflake 
        x, y = zip(*snowflake)  # Sépare les coordonnées x et y
        self.ax.plot(x, y, color='blue')  # Dessine la neige de Koch
        # Ajuste les limites de l'axe pour suivre le zoom
        self.ax.set_xlim(-self.scale/(1.1**frame), self.scale/(1.1**frame))
        self.ax.set_ylim(-self.scale/(1.1**frame), self.scale * np.sqrt(3)/2/(1.1**frame))
        self.ax.axis('off')  # Cache les axes
        self.ax.set_title(f'Zoom Level: {frame}')  # Affiche le niveau de zoom actuel

    # Lance l'animation
    def animate(self):
        ani = FuncAnimation(self.fig, self.update, frames=np.arange(0, 100), interval=self.interval)
        plt.show()  # Affiche l'animation

# Exemple d'utilisation
if __name__ == "__main__":
    snowflake = KochSnowflake(order=5, scale=10, interval=100)
    snowflake.animate()