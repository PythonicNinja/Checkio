def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))


def recall_password(cipher_grille, ciphered_password):
    result = ''

    for n in range(4):
        for g, p in zip(cipher_grille, ciphered_password):
            for i, j in zip(g, p):
                if i =='X':
                    result += j

        cipher_grille = rotate_matrix(cipher_grille)

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
