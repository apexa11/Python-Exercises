#!/usr/bin/python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# make list for hold items

shopping_list = []


# print out the instruction for app

def show_help():

    print 'what is your list?'
    print 'Enter "Done" when you complete list.'
    print 'Enter "Help" for this help.'
    print 'Enter "Show" for see your list.'


def show_list():

    # print out the list

    print 'here is your list'

    for item in shopping_list:
        print item


def add_to_list(new_item):

    # add items in your list

    shopping_list.append(new_item)
    print 'Added {}. list now has {} items'.format(new_item,
            len(shopping_list))


show_help()
while True:

     # ask for new item

    new_item = input('> ')

    # able to quit app

    if new_item == 'Done':
        break
    elif new_item == 'Help':

        show_help()
        continue
    elif new_item == 'Show':
        show_list()
        continue

    add_to_list(new_item)

 
