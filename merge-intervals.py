def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    result = []

    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            low = result[-1]
            if interval[0] <= low[1] + 1:
                result[-1] = (low[0], max(low[1], interval[1]))
            else:
                result.append(interval)

    # print(result)

    return result




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
