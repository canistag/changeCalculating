# Grayson Moriel
# Intro To Scripting Languages
# 11-16-2023

from decimal import Decimal
import random

#loop that accepts total,
#validates data, and returns it to main module
def pay_pleco(total):
    #pleco is a fish that cleans the tank.
    #term is used in place of data cleaning.
    
    #get input
    pay = input('Input pay.\t')
    try:
        # disallow string input
        if type(pay) == str:
            print('Type Error. Please enter a number.')
            pay = input('Input pay.\t')
    except:
            print()
    #convert to decimal object
    #placed before insufficient funds loop,
    #to disallow string statement to be passed
    #and crash program.
    pay = Decimal(f"{pay}")
    pay = pay.quantize(Decimal("1.00"))
    
    #data validation loop. disallows pay to be less than total
    while pay < total:
        print()
        print('Insufficient funds.')
        pay = input('Input pay.\t')
        pay = Decimal(f"{pay}")
        pay = pay.quantize(Decimal("1.00"))
    #otherwise return pay to main
    else:
        return pay


def main():
    #welcome statement and formatting
    print()
    print('Welcome to the Change Calculating Program.')
    print()

    #establishing variables for random generating
    lowrange = 0.01
    highrange= 20.00
    total = random.uniform(lowrange, highrange)
    total = float(round(total, 2))

    #convert to decimal object
    total = Decimal(f"{total}")
    total = total.quantize(Decimal("1.00"))
    
    #display total
    print(f"Your total is\t\t{total}")

    #get input
    pay = pay_pleco(total)
    print(f'Pay: ${pay}')

    #calculate change
    change = pay-total
    change = Decimal(f"{change}")
    change = change.quantize(Decimal("1.00"))
    
    #print change
    print(f'Change: ${change}')

    #variables to hold bills + coins
    tank20 = 0
    tank10 = 0
    tank5 = 0
    tank1 = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    #shredders
    while change >=20:
            change = change-20
            tank20 = tank20+1
    print(f'{tank20} 20 dollar bill(s)')
    while change >=10:
            change = change-10
            tank10 = tank10+1
    print(f'{tank10} 10 dollar bill(s)')
    while change >=5:
            change = change-5
            tank5 = tank5+1
    print(f'{tank5} 5 dollar bill(s)')
    while change >=1:
            change = change-1
            tank1 = tank1+1
    print(f'{tank1} 1 dollar bill(s)')
    #shredder for coin change specifically
    while change <=.99:
        change = change * 100
        while change<=99 and change>25:
            change = change-25
            quarter=quarter+1
            if change<25:
                break
        while change<=24 and change>10:
            change=change-10
            dime=dime+1
            if change<10:
                break
        while change<=9 and change>4:
            change=change-5
            nickel=nickel+1
            if change<4:
                break
        while change<=4 and change>0:
            change=change-1
            penny=penny+1
            if change == 0:
                break
        if change == 0:
                break
    print(f'{quarter} quarter(s)')
    print(f'{dime} dime(s)')
    print(f'{nickel} nickel(s)')
    print(f'{penny} penny/pennies')
    
    #test statement to make sure everything is accounted for
    #could be removed in final build
    print(f'Change remaining: ${change}')
    restart()

#restart module
def restart():
    check = input('Restart y/n.\t')
    if check == "y":
        main()
    elif check == "n":
        print('Thank you, bye.')

#call main
main()

