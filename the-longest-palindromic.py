def longest_palindromic(text):
    maxLength = 1

    begin = 0
    end = len(text)

    low = 0
    high = 0

    for i in range(1, end):

        low = i-1
        high = i
        while low >= 0 and high < end and text[low] == text[high]:
            if high - low + 1 > maxLength:
                begin = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < end and text[low] == text[high]:
            if high - low + 1 > maxLength:
                begin = low
                maxLength = high - low + 1
            low -= 1
            high += 1


    return text[begin:begin+maxLength]



if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
