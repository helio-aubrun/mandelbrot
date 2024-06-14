import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10, color='darkblue'):
    def koch_snowflake_complex(order):
        if order == 0:
            return np.array([0, 1, 0.5 + 0.5j*np.sqrt(3), 0])
        else:
            ZR = 0.5 - 0.5j*np.sqrt(3)/3
            p = koch_snowflake_complex(order - 1)
            p = np.concatenate([p/3,
                                p/3 + (ZR-p/3)*np.exp(2j*np.pi/3),
                                p/3 + (ZR-p/3)*np.exp(-2j*np.pi/3),
                                p/3 + 2*p/3])
            return p

    p = scale * koch_snowflake_complex(order)
    plt.plot(p.real, p.imag, color=color)
    plt.axis('equal')
    plt.axis('off')

def display_koch_snowflake():
    fig, ax = plt.subplots(figsize=(10, 10))
    koch_snowflake(5)
    plt.title("Koch Snowflake", fontsize=20)
    plt.show()
