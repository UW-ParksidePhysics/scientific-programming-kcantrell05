import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation



# Function definition

def wave_function(x, t, alpha, f, k, w):

    return np.exp(-(alpha*x - f*t)**2) * np.sin(k*x - w*t)



if __name__ == "__main__":

    alpha = 0.5

    f = 3

    k = 3 * np.pi

    w = 3 * np.pi



    x_values = np.linspace(-6, 6, 1001)

    t_values = np.linspace(-1, 1, 61)



    fig, ax = plt.subplots()

    line, = ax.plot([], [])

    ax.set_xlim(-6, 6)

    ax.set_ylim(-1, 1)

    ax.set_xlabel('x')

    ax.set_ylabel('f(x, t)')

    ax.set_title('Wave Function Animation')



    def update(frame):

        t = t_values[frame]

        y_values = wave_function(x_values, t, alpha, f, k, w)

        line.set_data(x_values, y_values)

        return line,



    ani = animation.FuncAnimation(fig, update, frames=len(t_values), interval=1000/6)



    writer = animation.PillowWriter(fps=6)

    ani.save('wave_animation.gif', writer=writer)



    # Display the saved GIF separately

    print("Animation saved as wave_animation.gif")

