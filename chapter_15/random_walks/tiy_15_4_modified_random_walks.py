# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-03
# --------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

from tiy_15_5_refactoring import RandomWalk

# Keep making new walks as long as the program is active.
while True:

    # Make a random walk
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # PLot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize first and last points
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
               s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # keep_running = input('Make another walk? (y/n): ')
    keep_running = 'n'
    if keep_running.lower() == 'n':
        break
