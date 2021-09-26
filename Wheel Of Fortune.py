#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import csv
wheellist = [100,100,150,200,200,250,300,350,400,450,500,500,550,600,650,700,750,800,800,850,900,900,'Bankrupt','Lose a Turn']
def spin():
    wheelspin = random.random() * 23
    return wheellist[int(wheelspin)]
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def conscheck(guess):
    if guess in consonants:
        return True
    else:
        return False
def fill(phrase, fillin, letter):
    hardphrase = phrase
    if letter in phrase.lower():
        for l in phrase:
            if letter in hardphrase.lower():
                index = hardphrase.lower().find(letter)
                hardphrase = hardphrase[:index] + '_' + hardphrase[index + 1:]
                fillin = fillin[:index] + letter + fillin[index + 1:]
    return fillin
    
#make list of phrases
categorylist = []
phraselist = []
with open(r'C:\Users\slygu\downloads\Wheel of Fortune Phrases Database.csv',encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        categorylist.append(str(line[0]))
        phraselist.append(str(line[1]))
categorylist.pop(0)
phraselist.pop(0)
#create round 1 phrase
round1index = random.random() * 47447
round1phrase = phraselist[int(round1index)]
round1category = categorylist[int(round1index)]
round1fillin = '_' * len(round1phrase)
#clean fillin for spaces
softphrase = round1phrase
for char in round1phrase:
    if char == ' ':
        index = softphrase.find(char)
        round1fillin = round1fillin[:index] + ' ' + round1fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == '-':
        index = softphrase.find(char)
        round1fillin = round1fillin[:index] + '-' + round1fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == "'":
        index = softphrase.find(char)
        round1fillin = round1fillin[:index] + "'" + round1fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
print(round1phrase)
print(round1category)
player1bank = 0
player2bank = 0
player3bank = 0
round1 = True
#manualspin = str(input('spin wheel? [y/n]: '))
#if manualspin == 'y':
    #print(str(spin()))
while round1:
    print('Round 1')
    print('=======')
    print(round1fillin)
    print('"{}" is the category'.format(round1category))
    if round1fillin.lower() == round1phrase.lower():
        round1 = False
    if round1 == False:
        break
    player1turn = True
    print('Player 1 is up!')
    print('===============')
    player1spin = spin()
    while player1turn:
        print('Player 1 has ${} in their bank'.format(player1bank))
        if type(player1spin) == int:
            print('The wheel has landed on ${}'.format(player1spin))
            player1cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player1cons):
                if player1cons in round1phrase.lower():
                    round1fillin = fill(round1phrase, round1fillin, player1cons)
                    print(round1fillin)
                    player1bank += player1spin
                    print('Player 1 bank: ${}'.format(player1bank))
                    player1choice = str(input('Player 1, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player1choice.lower() == 'vowel':
                        player1bank -= 250
                        while True:
                            player1vowel = str(input('Enter the vowel you would like to guess: '))
                            if player1vowel.lower() in vowels:
                                round1fillin = fill(round1phrase,round1fillin,player1vowel)
                                print(round1fillin)
                                player1turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player1choice.lower() == 'guess':
                        player1phrase = str(input('Enter your guess for the phrase: '))
                        if player1phrase.lower() == round1phrase.lower():
                            print('Congrats, you got it!')
                            round1 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player1phrase))
                            player1turn = False
                    if player1choice.lower() == 'end':
                        player1turn = False
                else:
                    print('Letter is not in phrase :(')
                    player1turn = False
            else:
                print('Is not a consonant please try again')
        if player1spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player1spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
    if round1fillin.lower() == round1phrase.lower():
        round1 = False
    if round1 == False:
        break
    player2turn = True
    print('Player 2 is up!')
    print('===============')
    player2spin = spin()
    while player2turn:
        if type(player2spin) == int:
            print('The wheel has landed on ${}'.format(player2spin))
            player2cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player2cons):
                if player2cons in round1phrase:
                    round1fillin = fill(round1phrase, round1fillin, player2cons)
                    print(round1fillin)
                    player2bank += player2spin
                    print('Player 2 bank: ${}'.format(player2bank))
                    player2choice = str(input('Player 2, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player2choice.lower() == 'vowel':
                        player2bank -= 250
                        while True:
                            player2vowel = str(input('Enter the vowel you would like to guess: '))
                            if player2vowel.lower() in vowels:
                                round1fillin = fill(round1phrase,round1fillin,player2vowel)
                                print(round1fillin)
                                player2turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player2choice.lower() == 'guess':
                        player2phrase = str(input('Enter your guess for the phrase: '))
                        if player2phrase.lower() == round1phrase.lower():
                            print('Congrats, you got it!')
                            round1 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player2phrase))
                            player2turn = False
                    if player2choice.lower() == 'end':
                        player2turn = False
                else:
                    print('Letter is not in phrase :(')
                    break
            else:
                print('Is not a consonant please try again')
        if player2spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player2spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
    if round1fillin.lower() == round1phrase.lower():
        round1 = False
    if round1 == False:
        break
    player3turn = True
    print('Player 3 is up!')
    print('===============')
    player3spin = spin()
    while player3turn:
        if type(player3spin) == int:
            print('The wheel has landed on ${}'.format(player3spin))
            player3cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player3cons):
                if player3cons in round1phrase:
                    round1fillin = fill(round1phrase, round1fillin, player3cons)
                    print(round1fillin)
                    player3bank += player3spin
                    print('Player 3 bank: ${}'.format(player3bank))
                    player3choice = str(input('Player 3, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player3choice.lower() == 'vowel':
                        player3bank -= 250
                        while True:
                            player3vowel = str(input('Enter the vowel you would like to guess: '))
                            if player3vowel.lower() in vowels:
                                round1fillin = fill(round1phrase,round1fillin,player3vowel)
                                print(round1fillin)
                                player3turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player3choice.lower() == 'guess':
                        player3phrase = str(input('Enter your guess for the phrase: '))
                        if player3phrase.lower() == round1phrase.lower():
                            print('Congrats, you got it!')
                            round1 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player3phrase))
                            player3turn = False
                    if player3choice.lower() == 'end':
                        player3turn = False
                else:
                    print('Letter is not in phrase :(')
                    break
            else:
                print('Is not a consonant please try again')
        if player3spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player3spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
print('Round 1 is over!')
round2index = random.random() * 47447
round2phrase = phraselist[int(round2index)]
round2category = categorylist[int(round2index)]
round2fillin = '_' * len(round2phrase)
print(round2phrase)
softphrase = round2phrase
for char in round2phrase:
    if char == ' ':
        index = softphrase.find(char)
        round2fillin = round2fillin[:index] + ' ' + round2fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == '-':
        index = softphrase.find(char)
        round2fillin = round2fillin[:index] + '-' + round2fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == "''":
        index = softphrase.find(char)
        round1fillin = round1fillin[:index] + "'" + round1fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
round2 = True
while round2:
    print('Round 2')
    print('=======')
    print(round2fillin)
    print('"{}" is the category'.format(round2category))
    if round2fillin.lower() == round2phrase.lower():
        round2 = False
    if round2 == False:
        break
    player1turn = True
    print('Player 1 is up!')
    print('===============')
    player1spin = spin()
    while player1turn:
        print('Player 1 has ${} in their bank'.format(player1bank))
        if type(player1spin) == int:
            print('The wheel has landed on ${}'.format(player1spin))
            player1cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player1cons):
                if player1cons in round2phrase.lower():
                    round2fillin = fill(round2phrase, round2fillin, player1cons)
                    print(round2fillin)
                    player1bank += player1spin
                    print('Player 1 bank: ${}'.format(player1bank))
                    player1choice = str(input('Player 1, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player1choice.lower() == 'vowel':
                        player1bank -= 250
                        while True:
                            player1vowel = str(input('Enter the vowel you would like to guess: '))
                            if player1vowel.lower() in vowels:
                                round2fillin = fill(round2phrase,round2fillin,player1vowel)
                                print(round2fillin)
                                player1turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player1choice.lower() == 'guess':
                        player1phrase = str(input('Enter your guess for the phrase: '))
                        if player1phrase.lower() == round2phrase.lower():
                            print('Congrats, you got it!')
                            round2 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player1phrase))
                            player1turn = False
                    if player1choice.lower() == 'end':
                        player1turn = False
                else:
                    print('Letter is not in phrase :(')
                    player1turn = False
            else:
                print('Is not a consonant please try again')
        if player1spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player1spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
    if round2fillin.lower() == round2phrase.lower():
        round2 = False
    if round2 == False:
        break
    player2turn = True
    print('Player 2 is up!')
    print('===============')
    player2spin = spin()
    while player2turn:
        if type(player2spin) == int:
            print('The wheel has landed on ${}'.format(player2spin))
            player2cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player2cons):
                if player2cons in round2phrase:
                    round2fillin = fill(round2phrase, round2fillin, player2cons)
                    print(round2fillin)
                    player2bank += player2spin
                    print('Player 2 bank: ${}'.format(player2bank))
                    player2choice = str(input('Player 2, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player2choice.lower() == 'vowel':
                        player2bank -= 250
                        while True:
                            player2vowel = str(input('Enter the vowel you would like to guess: '))
                            if player2vowel.lower() in vowels:
                                round2fillin = fill(round2phrase,round2fillin,player2vowel)
                                print(round2fillin)
                                player2turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player2choice.lower() == 'guess':
                        player2phrase = str(input('Enter your guess for the phrase: '))
                        if player2phrase.lower() == round2phrase.lower():
                            print('Congrats, you got it!')
                            round2 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player2phrase))
                            player2turn = False
                    if player2choice.lower() == 'end':
                        player2turn = False
                else:
                    print('Letter is not in phrase :(')
                    break
            else:
                print('Is not a consonant please try again')
        if player2spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player2spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
    if round2fillin.lower() == round2phrase.lower():
        round2 = False
    if round2 == False:
        break
    player3turn = True
    print('Player 3 is up!')
    print('===============')
    player3spin = spin()
    while player3turn:
        if type(player3spin) == int:
            print('The wheel has landed on ${}'.format(player3spin))
            player3cons = str(input('Guess a consonant: ')).lower()
            if conscheck(player3cons):
                if player3cons in round2phrase:
                    round2fillin = fill(round2phrase, round2fillin, player3cons)
                    print(round2fillin)
                    player3bank += player3spin
                    print('Player 3 bank: ${}'.format(player3bank))
                    player3choice = str(input('Player 3, would you like to buy a vowel, guess the phrase, or end. [vowel/guess/end]: '))
                    if player3choice.lower() == 'vowel':
                        player3bank -= 250
                        while True:
                            player3vowel = str(input('Enter the vowel you would like to guess: '))
                            if player3vowel.lower() in vowels:
                                round2fillin = fill(round2phrase,round2fillin,player3vowel)
                                print(round2fillin)
                                player3turn = False
                                break
                            else:
                                print('Please enter a vowel...')
                    if player3choice.lower() == 'guess':
                        player3phrase = str(input('Enter your guess for the phrase: '))
                        if player3phrase.lower() == round2phrase.lower():
                            print('Congrats, you got it!')
                            round2 = False
                            break
                        else:
                            print('{} is not the phrase!'.format(player3phrase))
                            player3turn = False
                            break
                    if player3choice.lower() == 'end':
                        player3turn = False
                else:
                    print('Letter is not in phrase :(')
                    break
            else:
                print('Is not a consonant please try again')
        if player3spin == 'Bankrupt':
            print('Uh oh you went bankrupt!')
            player1bank = 0
            break
        if player3spin == 'Lose a Turn':
            print('The wheel determined that you lose your turn. Sorry!')
            break
print('Round 2 is over!')
if player1bank > player2bank and player1bank > player3bank:
    finalplayer = 'Player 1'
    finalbank = player1bank
if player2bank > player1bank and player2bank > player3bank:
    finalplayer = 'Player 2'
    finalbank = player2bank
if player3bank > player2bank and player3bank > player1bank:
    finalplayer = 'Player 3'
    finalbank = player3bank
print('============')
print('Final round!')
print('============')
print('{} has the most in their bank and advances to the final round'.format(finalplayer))
print('The guesses filled in are: R, S, T, L, N, E')
print('Player gets to guess 3 consonants and 1 vowel')
print('Player gets only one guess to win!')
finalroundhints = ['r','s','t','l','n','e']
round3index = random.random() * 47447
round3phrase = phraselist[int(round3index)]
round3category = categorylist[int(round3index)]
round3fillin = '_' * len(round3phrase)
softphrase = round3phrase.lower()
for char in round3phrase:
    if char == ' ':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + ' ' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == '-':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + '-' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == "'":
        index = softphrase.find(char)
        round1fillin = round1fillin[:index] + "'" + round1fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 'r':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 'r' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 's':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 's' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 't':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 't' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 'l':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 'l' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 'n':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 'n' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    if char == 'e':
        index = softphrase.find(char)
        round3fillin = round3fillin[:index] + 'e' + round3fillin[index + 1:]
        softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
print(round3phrase)
print(round3fillin)
round3 = True
while round3:
    cons1 = str(input('Enter your first consonant guess: '))
    cons2 = str(input('Enter your second consonant guess: '))
    cons3 = str(input('Enter your third consonant guess: '))
    vowel1 = str(input('Enter your vowel guess: '))
    for char in round3phrase:
        if char == cons1:
            index = softphrase.find(char)
            round3fillin = round3fillin[:index] + cons1 + round3fillin[index + 1:]
            softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
        if char == cons2:
            index = softphrase.find(char)
            round3fillin = round3fillin[:index] + cons2 + round3fillin[index + 1:]
            softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
        if char == cons3:
            index = softphrase.find(char)
            round3fillin = round3fillin[:index] + cons3 + round3fillin[index + 1:]
            softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
        if char == vowel1:
            index = softphrase.find(char)
            round3fillin = round3fillin[:index] + vowel1 + round3fillin[index + 1:]
            softphrase = softphrase[:index] + '_' + softphrase[index + 1:]
    print(round3fillin)
    print('==================')
    print('One guess is allowed, good luck!')
    finalguess = str(input('Enter your guess: '))
    if finalguess.lower() == round3phrase.lower():
        print('Congrats, you got it! You have won ${}'.format(finalbank))
        break
    else:
        print('That is not the phrase :(')
        print('The phrase was...')
        print(round3phrase)
        break
print('Thank you for playing... WHEEL OF FOTURNEEEEEEE')


# In[ ]:




