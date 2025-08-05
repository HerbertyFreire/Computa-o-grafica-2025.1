def bresenham_line(x1, y1, x2, y2):

    
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    x, y = x1, y1

    while True:
        points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points


start_point = (1, 1)
end_point = (8, 5)

print(f"Calculando a linha entre {start_point} e {end_point} usando o algoritmo de Bresenham:")
calculated_points = bresenham_line(start_point[0], start_point[1], end_point[0], end_point[1])

print(calculated_points)