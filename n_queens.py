from typing import List


def depth_first_search(
    possible_board: List[int],
    diagonal_right_collisions: List[int],
    diagonal_left_collisions: List[int],
    boards: List[List[str]],
    n: int,
) -> None:
    
    row = len(possible_board)

    if row == n:
        possible_board = [". " * i + "Q " + ". " * (n - 1 - i)
                          for i in possible_board]
        boards.append(possible_board)
        return

    for col in range(n):

        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )


def n_queens_solution(n: int) -> None:
    boards = []
    depth_first_search([], [], [], boards, n)

    """ Print all the boards """
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n_queens_solution(4)
