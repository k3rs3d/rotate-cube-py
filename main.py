import time
import os
import math

# Define the ASCII characters for rendering lines
LINE_CHAR = "*"

# Define the terminal dimensions (adjust based on your terminal size)
TERMINAL_WIDTH = 40
TERMINAL_HEIGHT = 20
# Define the margin size (in terminal cells) around the cube
MARGIN_X = 2
MARGIN_Y = 1

# Define the vertices of a cube
vertices = [
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1),
    (-1, 1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (1, 1, -1),
    (1, 1, 1),
]

# Define the edges of the cube
edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

# Define rotation angles (in radians)
angle_x = 0
angle_y = 0
angle_z = 0


# Map 3D coordinates to terminal grid
def map_to_terminal(vertex, width, height):
    x, y, z = vertex

    # Normalize the coordinates to the range [-1, 1]
    normalized_x = (x + 1) / 2
    normalized_y = (1 - y) / 2

    # Calculate terminal coordinates
    terminal_x = int(normalized_x * width)
    terminal_y = int(normalized_y * height)

    return terminal_x, terminal_y


# Rotation function using rotation matrices
def rotate_vertex(vertex, angle_x, angle_y, angle_z):
    x, y, z = vertex
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)

    new_x = x * cos_y * cos_z - y * cos_y * sin_z + z * sin_y
    new_y = x * (cos_x * sin_z + sin_x * sin_y * cos_z) + y * (
                cos_x * cos_z - sin_x * sin_y * sin_z) - z * sin_x * cos_y
    new_z = x * (sin_x * sin_z - cos_x * sin_y * cos_z) + y * (
                sin_x * cos_z + cos_x * sin_y * sin_z) + z * cos_x * cos_y

    return new_x, new_y, new_z


# Function to render lines between terminal coordinates
def render_line(start, end, width, height):
    start_x, start_y = start
    end_x, end_y = end

    # Calculate the change in x and y
    dx = end_x - start_x
    dy = end_y - start_y

    if dx == 0 and dy == 0:
        return  # Skip rendering if the points are the same

    # Determine the number of steps needed
    steps = max(abs(dx), abs(dy))

    # Calculate step increments
    x_step = dx / steps
    y_step = dy / steps

    # Calculate the offset to center the cube
    offset_x = (width - 2 * MARGIN_X) / 2
    offset_y = (height - 2 * MARGIN_Y) / 2

    # Create an empty line
    line = [" "] * (steps + 1)

    # Populate the line with the line character
    for i in range(steps + 1):
        x = int(start_x + i * x_step + offset_x + MARGIN_X)
        y = int(start_y + i * y_step + offset_y + MARGIN_Y)
        line[i] = f"\033[{y};{x}H{LINE_CHAR}"  # Store line character

    # Print the entire line at once
    print("".join(line))


# Animation loop
while True:
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Apply rotation to each vertex
    rotated_vertices = [rotate_vertex(vertex, angle_x, angle_y, angle_z) for vertex in vertices]

    # Display ASCII representation of the cube
    for edge in edges:
        v1 = rotated_vertices[edge[0]]
        v2 = rotated_vertices[edge[1]]

        terminal_v1 = map_to_terminal(v1, TERMINAL_WIDTH, TERMINAL_HEIGHT)
        terminal_v2 = map_to_terminal(v2, TERMINAL_WIDTH, TERMINAL_HEIGHT)

        render_line(terminal_v1, terminal_v2, TERMINAL_WIDTH, TERMINAL_HEIGHT)  # Pass terminal dimensions

    # Update rotation angles for the next frame
    angle_x += 0.02
    angle_y += 0.03
    angle_z += 0.04

    # Control frame rate
    time.sleep(0.1)

