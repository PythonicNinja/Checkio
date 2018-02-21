VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

from re import split

def checkio(text):

    text = split('[ ,.?!]', text)
    text = [i for i in text if len(i) > 1]

    print(text)

    result = 0
    for i in text:
        try:
            if i[0].upper() in VOWELS:
                cnt = 0
            elif i[0].upper() in CONSONANTS:
                cnt = 1
            else:
                raise ValueError

            for j in i[1:]:
                if cnt % 2 == 0:
                   if j.upper() not in CONSONANTS:
                       raise ValueError
                elif cnt % 2 == 1:
                    if j.upper() not in VOWELS:
                        raise ValueError
                cnt += 1
        except ValueError:
            pass
        else:
            result += 1

    # print(result)
    return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("1st 2a ab3er root rate") == 1, "nalesnik"
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
