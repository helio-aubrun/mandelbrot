import matplotlib.pyplot as plt
import numpy as np

#formule de snowflake de koch
def koch_curve(order, p1, p2):
    if order == 0:
        return [p1, p2]
    else:
        p1 = np.array(p1)
        p2 = np.array(p2)
        s = (p2 - p1) / 3
        p3 = p1 + s
        p4 = p1 + 2 * s
        p5 = p3 + np.dot([[0.5, -np.sqrt(3)/2], [np.sqrt(3)/2, 0.5]], s)
        return (koch_curve(order - 1, p1, p3) +
                koch_curve(order - 1, p3, p5) +
                koch_curve(order - 1, p5, p4) +
                koch_curve(order - 1, p4, p2))
    
#initialisation des point et utilisation de la formule de snowflake de koch
def koch_snowflake(order, scale=10):
    p1 = [0, 0]
    p2 = [scale, 0]
    p3 = [scale / 2, scale * np.sqrt(3) / 2]
    return (koch_curve(order, p1, p2) +
            koch_curve(order, p2, p3) +
            koch_curve(order, p3, p1))

#affichage du snowflake
def display_koch_snowflake(order = 5):
    snowflake = koch_snowflake(order)
    snowflake = np.array(snowflake)
    
    plt.plot(snowflake[:, 0], snowflake[:, 1], 'b-')
    plt.title(f'Koch Snowflake - Order {order}')
    plt.axis('equal')
    plt.show()


