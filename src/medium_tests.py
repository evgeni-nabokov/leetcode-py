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

    def test_productExceptSelf(self):
        test_cases = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ]
        for nums, expected in test_cases:
            self.assertEqual(expected, Solution.productExceptSelf(nums))

    def test_shortestBridge(self):
        test_cases = [
            ([[0, 1], [1, 0]], 1),
            ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
            ([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], 1)
        ]
        for a, expected in test_cases:
            self.assertEqual(expected, Solution.shortestBridge(a))

    def test_shortestPathBinaryMatrix(self):
        test_cases = [
            ([[0]], 1),
            ([[0, 1], [1, 0]], 2),
            ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
            ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
            ([
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 0]
            ], 25),
            ([
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0]
            ], -1)
        ]
        for a, expected in test_cases:
            self.assertEqual(expected, Solution.shortestPathBinaryMatrix(a))


if __name__ == '__main__':
    unittest.main()
