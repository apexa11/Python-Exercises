
# make list for hold items

shopping_list = []

# print 

print 'what is your list?'
print 'Enter DONE when you complete list'

while True:

     # ask for new item

    new_item = input("> ")

    #able to quit app
    if new_item == "Done":
        break
    
    #add items in your list
    shopping_list.append(new_item)

    #print out the list
    print 'here is your list'

    for item in shopping_list:
        print item

    

     
 
 
