print('Welcome to bank of spain ATM')
restart=('y')
chances = 3
balance = 1000000
while chances >= 0:
    pin = int(input('please enter four digit pin:'))
    if pin == (1234):
        print('you entered your pin correctly\n')
        while restart not in ('n','No','no','N'):
            print('please press 1 for your balance')
            print('please press 2 to make a withdraw')
            print('please press 3 to pay in')
            print('please press 4 to return card')
            option = int(input('what would you like to choose?'))
            if option == 1:
                print('your balance is $',balance,'\n')
                restart = input('would you like to go back?')
                if restart in ('n','No','no','N'):
                    print('thankyou')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('how much you would like to withdraw?\n$10/$20/$30/$40/$60/$80/$100'))
                if withdrawl in [10,20,30,40,60,80,100]:
                    balance = balance - withdrawl
                    print('\nyour balance is now $',balance)
                    restart = input('would you like to go back?')
                    if restart in ('n', 'No', 'no', 'N'):
                        print('thankyou')
                        break
                elif withdrawl != [10,20,30,40,60,80,100]:
                    print('invalid Amount, please re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter desired amount:'))

            elif option == 3:
                pay_in = float(input('how much would you like to pay in?'))
                balance = balance + pay_in
                print('\nyour balance now in $',balance)
                restart = input('would you like to go back?')
                if restart in ('n', 'No', 'no', 'N'):
                    print('thankyou')
                    break
            elif option == 4:
                print('please wait while your card is returning....\n')
                print('thank you')
                break
            else:
                print('please enter the correct number.\n')
                restart = ('y')
    elif pin != ('1234'):
        print('incorrect password')
        chances = chances -1
        if chances == 0:
            print('\nno more tries')
            break




                    
                    
                




