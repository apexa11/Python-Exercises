import random

  #generate a number between 1 and 10
secret_num = random.randint(1,10)

while True:
    #get a number guess from user
    my_num =int(input("Guess number between 1 and 10:"))

    #compare guess to secret number
    if my_num == secret_num:
        print("You got it!!my number was {}".format(secret_num))
        break
    else:
              print("That's not it!!")
