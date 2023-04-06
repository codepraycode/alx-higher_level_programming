#!/usr/bin/python3
"""Module to solve N Queens problem

References:
    - Queens: https://intranet.alxswe.com/rltoken/dAQmi8RxMnLH-iHBzkz-lw
    - Backtracking algorithm:
        https://intranet.alxswe.com/rltoken/TGXZXdY2Awg8m4mSjlrjjA
"""


class Queen(object):
    """Queen class to solve the Queens problem
        using backtracking algorithm
    """

    # ===== Magic Methods =======
    def __init__(self, N=0):
        """Initialize Queen class instance
        Args:
            N(int): required!

        Raises:
            TypeError: if N is not a number
                exception message could be `N must be a number`
            ValueError: if N is less than 4
                exception message could be `N must be at least 4`

        Note:
            - Exceptions are controlled.
        """
        try:
            self.N = N
        except (TypeError, ValueError) as error:
            print(error)
            sys.exit(1)

    # ===== Getters and Setters =======
    @property
    def N(self):
        """int: value of N"""
        return self.__N

    @N.setter
    def N(self, value):
        """Set value of N

        Args:
            value(int): value to set for N

        Raises:
            TypeError: if N is not a number
                exception message could be `N must be a number`
            ValueError: if N is less than 4
                exception message could be `N must be at least 4`
        """
        # ===== Check TypeError =====
        try:
            value = int(value)
        except Exception:
            raise TypeError("N must be a number")
        # ===== Check ValueError =====
        if value < 4:
            raise ValueError("N must be at least 4")

        self.__N = value

    # ===== Private Methods =======
    def __backtracking(self, q_pos, q_i):
        """Recursively execute backtracking algorithm
            and print possible solution to problem.

        Args:
            q_pos(list): array of queen's path
            q_i(int): queen's index
        """

        if q_i is len(q_pos):
            return self.__print(q_pos, q_i)

        q_pos[q_i] = -1

        while(q_pos[q_i] < len(q_pos) - 1):
            q_pos[q_i] += 1

            if self.__is_safe(q_pos, q_i) is True:
                if q_i is not len(q_pos):
                    self.__backtracking(q_pos, q_i + 1)

    def __is_safe(self, q_pos, q_i):
        """Checks if queens can check each other.

        Args:
            q_pos(list): array of queen's path
            q_i(int): queen's index

        Returns:
            bool: True if any queen can check another queen
                false otherwise.
        """
        for i in range(q_i):
            if q_pos[i] == q_pos[q_i]:
                return False

            if abs(q_pos[i] - q_pos[q_i]) == abs(i - q_i):
                return False

        return True

    def __print(self, q_pos, q_i):
        """Prints queens path as a list.

        Args:
            q_pos(list): array of queen's path
            q_i(int): queen's index
        """
        _response = [[i, q_pos[i]] for i in range(q_i)]

        print(_response)

    # ===== Static Methods =======
    def solve(self, N=None):
        """Soves the challenge using backtracking algorithm

        Args:
            N(int, optional): defaults to instance value of N
        """
        try:
            self.N = N if N is not None else self.N
        except (TypeError, ValueError) as error:
            print(error)
            sys.exit(1)
            return

        q_pos = [-1 for _ in range(self.N)]

        # Solve!
        self.__backtracking(q_pos, 0)


# If this file is executed as a script
if __name__ == "__main__":
    """Running as script

    Usage: `nqueens N`
        If user calls the program with the wrong number of arguments,
        `Usage: nqueens N` is printed, and exits with status code of 1.
    """
    import sys

    # Checking and validating user arguments
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    value = sys.argv[1]

    q = Queen(value)

    q.solve()
