def iterate_submatrix(matrix):
    submat = [row for row in matrix]
    for r in submat:
        yield tuple(r)
    for c in range(0, len(matrix[0])):
        yield tuple(r[c] for r in submat)
    yield tuple(submat[rc][rc] for rc in range(0, len(matrix[0])))
    yield tuple(submat[rc][len(matrix[0])-1-rc] for rc in range(0, len(matrix[0])))
    for r in range(1, len(matrix)-3):
        yield tuple(submat[rc+r][rc] for rc in range(0, len(matrix[0])-r))
    for c in range(1, len(matrix)-3):
        yield tuple(submat[rc][rc+c] for rc in range(0, len(matrix[0])-c))
    for r in range(1, len(matrix) - 3):
        yield tuple(submat[rc+r][len(matrix[0])-1-rc] for rc in range(0, len(matrix[0])-r))
    for c in range(1, len(matrix) - 3):
        yield tuple(submat[rc][len(matrix[0])-1-rc-c] for rc in range(0, len(matrix[0])-c))


def checkio(matrix):

    for item in iterate_submatrix(matrix):
        # print(item)
        for i in range(len(item)-3):
            if item[i] == item[i+1] == item[i+2] == item[i+3]:
                return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
