import unittest
from unittest.mock import patch, MagicMock
import pygame
import numpy as np
from Visualization import select_difficulty, display, reset_visited_attributes, init_solve, solve_maze


class TestVisualization(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_select_difficulty_easy(self, mock_input):
        # Use mock_input to avoid the warning
        mock_input()  # Accessing mock_input
        self.assertEqual(select_difficulty(), (25, 25))

    @patch('builtins.input', side_effect=['2'])
    def test_select_difficulty_medium(self, mock_input):
        mock_input()  # Accessing mock_input
        self.assertEqual(select_difficulty(), (50, 50))

    @patch('builtins.input', side_effect=['3'])
    def test_select_difficulty_hard(self, mock_input):
        mock_input()  # Accessing mock_input
        self.assertEqual(select_difficulty(), (75, 75))

    @patch('builtins.input', side_effect=['4'])
    def test_select_difficulty_invalid(self, mock_input):
        mock_input()  # Accessing mock_input
        self.assertEqual(select_difficulty(), (25, 25))

    def test_reset_visited_attributes(self):
        mock_grid = [[MagicMock(visited=True)
                      for _ in range(3)] for _ in range(3)]
        reset_visited_attributes(mock_grid)
        for row in mock_grid:
            for cell in row:
                self.assertFalse(cell.visited)

    def test_init_solve(self):
        mock_grid = [[MagicMock(x=i, y=j, visited=True, open_neighbors=[])
                      for j in range(3)] for i in range(3)]
        init_solve(mock_grid)
        for row in mock_grid:
            for cell in row:
                self.assertFalse(cell.visited)
                self.assertTrue(cell.open_neighbors)

    @patch('pygame.display.update')
    @patch('pygame.draw.rect')
    def test_display(self, mock_draw_rect, mock_display_update):
        mock_display_update()  # Accessing mock_display_update
        screen = MagicMock()
        mock_grid = [[MagicMock(top=True, right=True, x=i, y=j, visited=False, start=False,
                                end=False, solution=False) for j in range(3)] for i in range(3)]
        display(screen, mock_grid, color_squares=True)
        self.assertTrue(mock_draw_rect.called)

    @patch('pygame.display.update')
    @patch('pygame.draw.rect')
    @patch('pygame.time.delay')
    def test_solve_maze(self, mock_delay, mock_draw_rect, mock_display_update):
        mock_display_update()  # Accessing mock_display_update
        screen = MagicMock()
        mock_grid = [[MagicMock(x=i, y=j, visited=False, open_neighbors=[
        ], end=False, solution=False) for j in range(3)] for i in range(3)]
        start_cell = mock_grid[0][0]
        start_cell.end = True
        self.assertTrue(solve_maze(screen, mock_grid, start_cell))


if __name__ == '__main__':
    unittest.main()
