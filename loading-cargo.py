from itertools import combinations

def checkio(data):

    if len(data) == 1:
        return data[0]

    bal = sum(data)/2
    half_range = range(len(data)//2+1)
    sums = [sum(val) for n in half_range for val in combinations(data, n)]
    closet = min(sums, key=lambda x: abs(bal - x))

    return 2 * abs(bal - closet)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
