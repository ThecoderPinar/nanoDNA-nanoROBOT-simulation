import unittest
from src.simulation import Simulation


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation()

    def test_initialization(self):
        self.assertIsInstance(self.simulation, Simulation)
        self.assertEqual(self.simulation.total_moves, 0)

    def test_move(self):
        initial_position = self.simulation.position
        self.simulation.move([1, 2, 3])
        new_position = self.simulation.position
        self.assertNotEqual(initial_position, new_position)


if __name__ == "__main__":
    unittest.main()
