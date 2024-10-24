# Maze-solver
This is my term project for the course Artificial intelligence. This project implements a maze generator and solver using Python and Pygame. It allows you to generate a maze using recursive algorithms and provides functionality to solve the maze by visualizing the solution path.

# Features
- Maze Generation: Generates random mazes of different sizes using recursive algorithms.
- Maze Solving: Visualizes the solution path using backtracking and displays the progress in real-time.
- Difficulty Levels: Supports multiple difficulty levels—easy, medium, and hard—by varying the maze size.
- Pygame Visualization: Uses Pygame to display the maze generation and solution steps with a graphical interface.

# Files
maze_generation.py:

Implements the core maze generation algorithm using recursive methods.
Generates a maze grid with walls and randomly selects a starting and ending point for the maze.
The class Cell represents each individual cell in the maze, with attributes for walls, visited status, neighbors, and solution steps.

Visualization.py:

Handles the graphical display of the maze and its solution using Pygame.
Provides functionality to draw the grid, walls, and highlight the solution path from the starting point to the end.
Includes the function to display progress as the maze is being solved in real-time.

Testing.py:

Contains unit tests for various components of the visualization and maze-solving process.
Tests the maze difficulty selection, grid initialization, resetting of visited attributes, and solution visualization using the unittest framework.

## How to Run

1. **Install the required libraries**:
   ```bash
   pip install pygame numpy

2. **Run the main visualization script**:
   ```bash
   python Visualization.py

- Choose the difficulty level by entering 1 (easy), 2 (medium), or 3 (hard) when prompted.
- Watch the maze being generated and solved.

# How It Works
- Maze Generation:
   The maze is generated using a depth-first recursive backtracking algorithm. Each cell is connected to its neighbors by breaking walls between them.
   The algorithm continues until all cells are visited, ensuring a fully connected maze with a single solution.
- Maze Solving:
  The solver uses a backtracking algorithm to find a path from the start cell to the end cell.
  As the solver progresses, the visited cells are displayed in real-time, and once the solution is found, the path is highlighted.
Visualization
- Maze Display:
   The maze is displayed using a grid layout. Each cell has walls on its top and right edges, which are removed during the generation process.
- Solution Path: The solver colors the correct solution path and visualizes its steps in real-time.
# Unit Testing
Unit tests are provided in Testing.py to ensure that:

- Maze difficulty is correctly selected.
- Cells are properly reset after the maze is generated.
- The maze-solving algorithm finds the correct solution.
# Example
After running the script, you will see something like this:

A grid-based maze will be generated and displayed.
The maze-solving algorithm will be shown step-by-step until the solution is found.
