def checkio(n, m):
    bin1 = '0{0:b}'.format(n)
    bin2 = '0{0:b}'.format(m)

    if len(bin1) < len(bin2):
        temp = '0' * (len(bin2) - len(bin1))

        bin1 = temp + bin1
    elif len(bin1) > len(bin2):
        temp = '0' * (len(bin1) - len(bin2))

        bin2 = temp + bin2

    result = [i != j for i, j in zip(bin1, bin2)]


    cnt = 0
    for i in result:
        if i:
            cnt += 1
    return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
