#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# make list of word

my_words = [
    'apple',
    'cookies',
    'chocolates',
    'cake',
    'pizza',
    'orange',
    'burger',
    'pancake',
    ]

while True:

    start = input('please enter to start or for quit enter Q')
    if start.lower() == 'q':
        break

# pick random word

secret_word = random.choice(my_words)
good_guesses = []
bad_guesses = []

while len(bad_guesses) < 7 and len(good_guesses) \
    != len(list(secret_word)):

    # draw spaces
    # dreaw gussed letter, spaces and strikes

    for letter in secret_word:
        if letter in good_guesses:
            print letter
        else:
            print '_'
        print ''
        print 'Strikes {}/7'.format(len(bad_guesses))
        print ''

    # take guess

        guess = input('Guess the letter').lower()
        if len(guess) != 1:
            print 'you can only guess single letter'
        elif guess in bad_guesse or guess in good_guess:
            print "you've already guess that letter"
            continue
            print 'you can only guess letter'
        elif guess.isalpha():
            print 'you can only guess letter'
            continue
        if guess in secret_word:
            good_guess.append(guess)
        if len(good_guess) == len(list(secret_word)):
            print 'you win !'
            break
        else:
            bad_guess.append(guess)
    else:

   # print out win/lose

        print "you didn't get the letter"
