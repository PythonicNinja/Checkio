def checkio(game_result):
    if "XXX" in game_result:
        return "X"
    elif "OOO" in game_result:
        return "O"

    for i in range(3):
        temp = game_result[0][i] + game_result[1][i] + game_result[2][i]
        if temp in "XXX/OOO":
            return temp[0]

    temp = game_result[0][0] + game_result[1][1] + game_result[2][2]
    if temp in "XXX/OOO":
        return temp[0]

    temp = game_result[0][2] + game_result[1][1] + game_result[2][0]
    if temp in "XXX/OOO":
        return temp[0]

    return "D"





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

