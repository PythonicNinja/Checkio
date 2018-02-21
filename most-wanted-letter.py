
from string import ascii_lowercase
def checkio(text):

    text = text.lower()
    tempText = ''
    for i in text:
        if i in ascii_lowercase:
            tempText += i

    text = tempText

    l = list(map(lambda x: [x, text.count(x)], set(text)))

    temp = [1, 0]

    for i in l:
        if temp[1] < i[1]:
            temp = i

    tempL = []
    for i in l:
        if i[1] == temp[1]:
            tempL += [i]

    if len(tempL) == 0:
        return temp[0]
    else:
        temp = sorted(tempL)[0]
        return temp[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Lorem ipsum dolor sit amet") == "m"
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
