import numpy as np

def coordinates(serial=7347):
    def power(x, y):
        rack = (x + 1) + 10
        power = rack * (y + 1)
        power += serial
        power *= rack
        return (power // 100 % 10) - 5

    grid = np.fromfunction(power, (300, 300))

    m = (0, (0, 0, 0))
    for width in range(3, 300):
        windows = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
        maximum = int(windows.max())
        location = np.where(windows == maximum)

        if width == 3:
            print(maximum, (location[0][0] + 1, location[1][0] + 1, width))

        m = max(m,
                (maximum, (location[0][0] + 1, location[1][0] + 1, width)),
                lambda x: x[0])

        if maximum < 0:
            break  # once it becomes negative, it won't be positive anymore.
    print(m)

coordinates()
