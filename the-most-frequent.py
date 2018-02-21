def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    result = []


    for i in set(data):
        result.append([i, data.count(i)])



    return sorted(result, key=lambda x: x[1], reverse=True)[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
