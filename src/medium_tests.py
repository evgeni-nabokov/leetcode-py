import unittest
from medium import Solution


class SolutionTest(unittest.TestCase):
    def test_exist(self):
        test_cases = [
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
            ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB", True),
            ([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCEFSADEESE", True),
            ([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]], "aaaaaaaaaaaaa", False)
        ]
        for board, word, expected in test_cases:
            self.assertEqual(expected, Solution.exist(board, word))


if __name__ == '__main__':
    unittest.main()
