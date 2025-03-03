class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  # Board to store the positions of queens.
        self.solutions = []  # List to store solutions.

    # Backtracking solution
    def solve_backtracking(self):
        self._solve_backtracking(0)
        return self.solutions

    def _solve_backtracking(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])  # A valid solution
            return True

        for col in range(self.n):
            if self._is_safe(row, col):
                self.board[row] = col
                if self._solve_backtracking(row + 1):
                    return True  # Continue with the next row if it's valid
                self.board[row] = -1  # Backtrack if no valid position is found

        return False  # No solution found in this configuration

    def _is_safe(self, row, col):
        # Check if the column is already occupied
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    # Branch and Bound solution
    def solve_branch_and_bound(self):
        self.solutions.clear()
        self._solve_branch_and_bound(0)
        return self.solutions

    def _solve_branch_and_bound(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])
            return True

        for col in range(self.n):
            if self._is_safe(row, col):
                self.board[row] = col
                if self._bound_check(row):  # Bound check
                    self._solve_branch_and_bound(row + 1)
                self.board[row] = -1
        return False

    def _bound_check(self, row):
        # A simple bound check: Return True if it is possible to place queens
        # up to this row (this can be enhanced for more efficient pruning).
        for i in range(row):
            if self.board[i] == self.board[row]:  # Same column
                return False
            if abs(self.board[i] - self.board[row]) == row - i:  # Same diagonal
                return False
        return True

    def print_solution(self, solutions):
        for solution in solutions:
            for row in solution:
                board_row = ['Q' if col == row else '.' for col in range(self.n)]
                print(' '.join(board_row))
            print()


if __name__ == '__main__':
    n = int(input("Enter the value of n (number of queens): "))
    n_queens = NQueens(n)

    print("\nSolving using Backtracking:")
    backtracking_solutions = n_queens.solve_backtracking()
    n_queens.print_solution(backtracking_solutions)

    print("\nSolving using Branch and Bound:")
    branch_bound_solutions = n_queens.solve_branch_and_bound()
    n_queens.print_solution(branch_bound_solutions)
