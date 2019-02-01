#martingaleProj.py

''' Takes four positive integers as inputs:
-percent chance of winning (between 0 and 100)
-stakes
-a winnings / loss threshhold
-maximum number of rounds

Prints the net profit of the Martingale gambling system with the given stakes run until
exceeding the threshhold or maximum number of rounds along the highest and lowest points.
Returns a list of net profit at all points of the run.
'''

import random


def martingale(percentwin, stakes, maxloss, maxround):
    wincount = 0
    losscount = 0
    count = 0
    roundnum = 0

    while roundnum < maxround:
        if random.randrange(0, 100) > percentwin:
            print('win')
            wincount += 1
            count+=1
            stakes*=2
        else:
            print('lose')
            losscount += 1
            count += 1
            stakes/=2
            if losscount == maxloss:
                print('That\'s enough gambling for you poor boy!')
                break
        print(stakes)
        print(count)
        roundnum+=1

    print('Your Results!\n''Number of gambles: ' + str(count) + '\nLosses: ' + str(losscount) + '\nWins: ' + str(wincount) + '\nNet Earnings: ' + str(stakes))

def runMartingale():
    a = int(input('Please type in your chances of winning (%): '))
    b = int(input('Please type in the amount you want to bet each turn ($): '))
    c = int(input('Please type in your maximum number of losses: '))
    d = int(input('Please type in the number of rounds you want to play: '))
    martingale(a, b, c, d)
    print('Do you want to play again? (type \'yes\' or \'no\')')
    
    while True:
        x=input()
        if x == 'yes':
            print('Alright, good luck!')
            runMartingale()
        if x == 'no':
            print('Alright, hope to take your money ag- see you soon!')
            break
        else:
            print('I don\'t know what you said but are we playing?')
            
runMartingale()




    
