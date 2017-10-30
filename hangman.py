#!/usr/bin/python3.5
# hangman.py - traditional hangman game
# coded by taladan At gmail Dot com

import random, os, time


def find_occurances(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def ask(stat):
    ask = input('You %s play again? ' % stat)
    if ask.lower() in 'yes':
        exitcode = 'PLAY'
    else:
        exitcode = 'QUIT'

    return exitcode


def graphic(num):
    pic = {0:'''
                        ______
                       |      |
                       |
                       |
                       |
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           1:'''
                        ______
                       |      |
                       |      O
                       |
                       |
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           2:'''
                        ______
                       |      |
                       |      O
                       |      T
                       |
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           3:'''
                        ______
                       |      |
                       |      O
                       |     /T
                       |
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           4:'''
                        ______
                       |      |
                       |      O
                       |     /T\\
                       |
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           5:'''
                        ______
                       |      |
                       |      O
                       |     /T\\
                       |     /
                    ___|________
                    | |      | |
                    | |      | |
           ''',
           6:'''
                        ______
                       |      |
                       |      O
                       |     /T\\
                       |     / \\
                    ___|________
                    | |      | |
                    | |      | |
           '''
           }
    return pic.get(num)

def display():
    mydisplay = '''Welcome to HangPy!

    Word: %s                      Incorrect Guesses Remaining: %d




                       %s





    Currently Guessed: %s
    Total wrong guesses: %d

        '''
    wrong_num = 0
    guess_limit = 6
    guessed = []
    choice = random.choice(open('hangman_file.txt').read().split()).strip()
    masklen = '*'*len(choice)
    secret = list(masklen)

    while True:
        remaining = guess_limit - wrong_num
        character_range = range(ord('a'), ord('z'))
        if remaining == 0:
            exitcode = ask('lose!')
            print(mydisplay % (''.join(secret), remaining, graphic(wrong_num),
                               guessed, wrong_num))
            break

        if ''.join(secret) == choice:
            exitcode = ask('win!')
            print(mydisplay % (''.join(secret), remaining, graphic(wrong_num),
                               guessed, wrong_num))
            break
        else:
            os.system('clear')
            print(mydisplay % (''.join(secret), remaining, graphic(wrong_num),
                               guessed, wrong_num))
            pick = input('Please enter a letter (QUIT to exit): ')
            if pick == 'QUIT':
                exitcode = 'QUIT'
                break
            elif ord(pick.lower()) not in character_range:
                print('Please enter a letter!')
                time.sleep(1)
            elif pick.lower() in guessed:
                print('You already picked %s!' % (pick))
                time.sleep(1)
            elif pick.lower() in choice:
                guessed.append(pick)
                position = find_occurances(choice, pick)
                for i in secret:
                    for pl in position:
                        if i == secret[pl]:
                            secret[pl] = pick
                print('Correct!')
                time.sleep(1)
            else:
                guessed.append(pick)
                wrong_num += 1
                print('%s is incorrect.  You have %d guesses remaining' %
                      (pick, remaining-1))
                time.sleep(1)
    return exitcode


def main():
    os.system('clear')
    code = 'PLAY'
    while code != 'QUIT':
        code = display()
    os.system('clear')


main()
