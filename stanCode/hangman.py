"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    pre: 創造答案隱藏字串 e.g.'-----'
    post: 輸入字母並查詢字母是否在字串裡
    """
    ans = random_word()
    print('The word likes this: ' + random_word_2(ans))
    ans_str = random_word_2(ans)
    game = game_start(ans_str, ans)


def game_start(ans_str, ans):
    for i in range(7):
        print('You have ' + str(7 - i) + ' wrong guesses left.')
        a = input('Yor guess: ')
        a = a.upper()
        while not a.isalpha():
            print('Illegal format')
            a = input('Yor guess: ')
            a = a.upper()
        while len(a) > 1:
            print('Illegal format')
            a = input('Yor guess: ')
            a = a.upper()
        else:
            if ans.find(a) == -1:
                print('There is no ' + str(a) + ' in the world')
            while ans.find(a) != -1:
                find = ''
                print('You are correct!')
                for j in range(len(ans)):
                    result = ans[j]
                    if result != a:
                        find = find + ans_str[j]
                    else:
                        find = find + a
                print('The word looks like: ' + str(find))
                ans_str = find
                a = input('Yor guess: ')
                a = a.upper()
            if ans_str == ans:
                print('You win!!')
                print('The words was: ' + str(ans))
                break
        if 6 - i == 0:
            print('The words was: '+str(ans))
            print('You are completely hung :(')
    return


def random_word_2(ans):
    ch = ''
    for i in range(len(ans)):
        ch += '-'
    #return 'The word likes this: ' + ch
    return ch


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
