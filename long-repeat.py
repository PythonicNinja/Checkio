def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """

    if len(line) == 0:
        return 0

    cnt = 1
    tempCnt = 1
    char = line[0]
    for i in range(1, len(line)):
        if char == line[i]:
            tempCnt += 1
        else:
            char = line[i]
            tempCnt = 1
        if cnt < tempCnt:
            cnt = tempCnt
    return cnt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
