def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    cnt = 0
    for i in range(len(text)):
        if text[i] == symbol:
            cnt += 1
            if cnt == 2:
                return i

    if cnt == 0:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
