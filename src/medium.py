from queue import Queue

class Solution:

    # 79. Word Search.
    # https://leetcode.com/problems/word-search/
    def exist(board: list[list[str]], word: str) -> bool:
        # Moving directions. First number - row addition, second number - column addition.
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Keeps track of visited cells.
        visited = [[False for c in range(len(board[0]))] for r in range(len(board))]

        # Keeps the result of a backtracking attempt for specific grid cell and specific letter of the word.
        # None - result is unknown yet - keep moving.
        # False - result is known - stop moving in this direction.
        # True is not kept because we immediately exit from the function.
        # The third dimention is len(word) - 1, not len(word) because we don't need to memorize the result for the last letter.
        memo = [[[None for i in range(len(word) - 1)] for c in range(len(board[0]))] for r in range(len(board))]

        # i - letter index in the word.
        # r - row index in the grid.
        # c - column index in the grid.
        def bt(i: int, r: int, c: int) -> bool:
            # Trivial checks if we're legit to continue.
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or visited[r][c] or word[i] != board[r][c]:
                return False

            # We went through all the letters and we checked the last one is the same. We can exit.
            if i == len(word) - 1:
                return True

            # Check if we're trying to go the path we went though unsuccessfully before. This check makes the solution 10 times faster.
            if memo[r][c][i] == False:
                return False

            visited[r][c] = True

            # Try to move in 4 directions.
            for dr, dc in dirs:
                if bt(i + 1, r + dr, c + dc):
                    return True

                # Don't forget to reset just visited grid cell.
            visited[r][c] = False

            # Memorize this path is unsuccessful.
            memo[r][c][i] = False

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if bt(0, r, c):
                    return True

        return False

    # 238. Product of Array Except Self.
    # https://leetcode.com/problems/product-of-array-except-self/
    # Time complexity: O(N).
    # Space complexity: O(1).
    def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)

        res = [1]
        for i in range(1, n):
            res.append(res[i - 1] * nums[i - 1])

        prod = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * prod
            prod *= nums[i]

        return res

    # 934. The Shortest Bridge.
    # https://leetcode.com/problems/shortest-bridge/
    def shortestBridge(a: list[list[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rl = len(a)
        cl = len(a[0])

        def get_start_point() -> tuple[int, int]:
            for r in range(rl):
                for c in range(cl):
                    if a[r][c] == 1:
                        return r, c

        def fill(r: int, c: int) -> None:
            if not (0 <= r < rl) or not (0 <= c < cl) or a[r][c] != 1:
                return

            queue.put((r, c))
            a[r][c] = 2

            for dr, dc in dirs:
                fill(r + dr, c + dc)

        queue = Queue()
        sr, sc = get_start_point()
        fill(sr, sc)

        step = 0
        while queue:
            ql = queue.qsize()
            for i in range(ql):
                r, c = queue.get()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rl and 0 <= nc < cl:
                        if a[nr][nc] == 1:
                            return step
                        elif a[nr][nc] == 0:
                            a[nr][nc] = 2
                            queue.put((nr, nc))
            step += 1

        return step

    # 1091. Shortest Path in Binary Matrix.
    # https://leetcode.com/problems/shortest-path-in-binary-matrix/
    # Time complexity: O(M x N), where M and N are grid dimensions.
    # Space complexity: O(1).
    def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        if n == 1 and grid[0][0] == 0:
            return 1

        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        queue = [(0, 0)]
        grid[0][0] = 1
        step = 1
        while queue:
            step += 1
            ql = len(queue)
            for i in range(ql):
                r, c = queue.pop(0)
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr == n - 1 and nc == n - 1:
                        return step
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 1

        return -1
