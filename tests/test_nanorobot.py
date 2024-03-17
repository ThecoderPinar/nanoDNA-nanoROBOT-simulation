import numpy as np
import unittest
import sys
import os

from src.nanorobot import Nanorobot

# nanorobot.py dosyasını içeren dizini Python yoluna ekleyin
mevcut_dizin = os.path.dirname(os.path.abspath(__file__))
modül_dizin = os.path.join(mevcut_dizin, '..')
sys.path.append(modül_dizin)


class TestNanorobot(unittest.TestCase):
    def setUp(self):
        self.dna_sequence = "ATCGATCGATCGATCG"
        self.nanorobot = Nanorobot(dna_sequence=self.dna_sequence)

    def test_initialization(self):
        self.assertEqual(self.nanorobot.position.tolist(), [0, 0, 0])
        self.assertEqual(self.nanorobot.history, [[0, 0, 0]])
        self.assertEqual(self.nanorobot.dna_sequence, self.dna_sequence)

    def test_move(self):
        displacement = [1, 1, 1]
        self.nanorobot.move(displacement)
        expected_position = np.array(displacement)
        self.assertTrue(np.array_equal(self.nanorobot.position, expected_position))
        self.assertTrue(np.array_equal(self.nanorobot.history[-1], expected_position))

    def test_recognize_target_sequence(self):
        target_sequence = "ATCG"
        self.assertTrue(self.nanorobot.recognize_target_sequence(target_sequence))
        invalid_sequence = "AAAA"
        self.assertFalse(self.nanorobot.recognize_target_sequence(invalid_sequence))

    def test_analyze_movement(self):
        for _ in range(10):
            self.nanorobot.move(np.random.uniform(-1, 1, size=3))
        total_distance, average_speed = self.nanorobot.analyze_movement()
        self.assertGreater(total_distance, 0)
        self.assertGreater(average_speed, 0)

if __name__ == "__main__":
    unittest.main()
