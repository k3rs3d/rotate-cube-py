# Rotating 3D ASCII Cube

This Python script generates a rotating 3D ASCII cube in the terminal.

## How it Works

The script uses basic 3D geometry and rotation matrices to calculate the positions of the cube's vertices as it rotates around different axes. These 3D coordinates are then mapped to terminal coordinates to render the cube using ASCII characters.

The cube is centered within the terminal window, leaving a margin around it to help it remain fully visible. The rotation angles are incrementally updated in a loop to create the animation effect.

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python: `python main.py`

## Customization

- You can adjust the `TERMINAL_WIDTH` and `TERMINAL_HEIGHT` variables to match your terminal's dimensions.
- The `MARGIN_X` and `MARGIN_Y` variables define the margin around the cube within the terminal window.
- Feel free to experiment with different ASCII characters for rendering lines and explore variations to enhance the visual representation.

## Note

Keep in mind that the appearance of the cube will vary drastically depending on your terminal's font and settings.

Happy rotating!