import numpy


def image_tracing(points):
    def lagrange_interpolation(x, y, current_x):
        y_new = 0
        for j in range(len(y)):
            numerator, denominator = 1, 1
            for i in range(len(x)):
                if i != j:
                    numerator *= (current_x - x[i])
                    denominator *= (x[j] - x[i])
            y_new += y[j] * numerator / denominator
        return y_new

    x_coords = [coords[0] for coords in points]
    y_coords = [coords[1] for coords in points]
    if min(x_coords) == max(x_coords):
        points = []
        for y_coord in range(round(min(y_coords)), round(max(y_coords)) + 1):
            points.append((x_coords[0], y_coord))
        return points
    new_x_coords = numpy.linspace(min(x_coords), max(x_coords), 100)
    new_y_coords = [lagrange_interpolation(x_coords, y_coords, current_x) for current_x in new_x_coords]
    return list(zip(new_x_coords, new_y_coords))