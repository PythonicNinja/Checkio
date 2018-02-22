from collections import defaultdict

def checkio(data):

    graphs = defaultdict(set)
    elements = set([char for i in data for char in i])
    result = []

    # make topology
    for s in data:
        chars = [c for c in s]
        for i in range(len(chars)):
            [graphs[c].add(chars[i]) for c in s[i+1:] if c != chars[i]]

    while elements:
        roots = sorted([c for c in elements if len(graphs[c]) == 0])
        root = roots[0]

        result.extend(root)
        elements.difference_update(root)
        [graphs[c].discard(root) for c in elements]

    return ''.join(result)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
