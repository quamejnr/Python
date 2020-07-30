
def share_diagonal(x1, y1, x2, y2):
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
    return dy == dx


def col_clash(ac, c):
    for i in range(c):
        if share_diagonal(i, ac[i], c, ac[c]):
            return True
    return False


def has_clash(board):
    for col in range(1, len(board)):
        if col_clash(board, col):
            return True
    return False


def similar(new_lst, *lists):
    if len(*lists) != 0:
        for i in range(len(*lists)):
            if lists[0][i] == new_lst:
                return True
    return False


def queens_puzzle(rng, solution):
    import random

    data = list(range(rng))
    record = []
    num_of_solution = 0
    num_of_tries = 0

    while num_of_solution < solution:
        random.shuffle(data)
        num_of_tries += 1
        if not has_clash(data) and not similar(data, record):
            record.append(data[:])
            print(f'Found solution {data} in {num_of_tries} tries')
            num_of_tries = 0
            num_of_solution += 1


queens_puzzle(8, 10)

