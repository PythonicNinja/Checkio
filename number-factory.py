def checkio(number):

    nums = []

    while number > 9:
        found = False
        for i in range(9, 1, -1):
            if number % i == 0:
                found = True
                nums.append(i)
                number = number // i
                break

        if found is False:
            return 0

    nums.append(number)

    rt = ""
    for num in sorted(nums):
        rt += str(num)

    return int(rt)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
