import random
n = 20
to_be_gussed = int(n * random.random()) + 1
guess = 0
while guess != to_be_gussed:
    guess = int(input('new number:'))
    if guess > 0:
        if guess > to_be_gussed:
            print('number too large')
    elif guess < to_be_gussed:
        print('number too small')
    else:
        print('sorry that you are giving up!')
        break

else:
    print('congo,you made it!')

