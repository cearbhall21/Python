#!/usr/bin/python

import time

#NewLine
def newline():
    time.sleep(1)
    print ('\n')

#Enter correct value
def errorstatement():
    print ('You must put a yes or no value in')

#Correct val
def incomeerror():
    print ('You must select "weekly", "bi-weekly", "monthly", or "salary"')
    time.sleep(2)

 
def income():
    while budget == 'yes':   
        print ('First, we need your monthly income after taxes')
        print ('Are your paychecks weekly, bi-weekly or monthly? Or are you salary?')
        answer1 = raw_input()
        if answer1 == str('weekly'):
            while True:
                print ('Okay, how much do you make per week?')
                try:
                    answer2 = int(raw_input("enter number: ")) * 4
                    print ('Okay, you make '+ str(answer2) + ' a month.')
                    break
                except ValueError:
                    print("You must enter an integer")
        elif answer1 == str('bi-weekly'):
            while True:
                print ('Okay, how much do you make bi-weekly?')
                try:
                    answer2 = int(raw_input("enter number: ")) * 2
                    print ('Okay, you make '+ str(answer2) + ' a month.')
                    break
                except ValueError:
                    print("You must enter an integer")
        elif answer1 == str('monthly'):
            while True:
                print ('Okay, how much do you make per month?')
                try:
                    answer2 = int(raw_input("enter number: "))
                    print ('Okay, you make '+ str(answer2) + ' a month.')
                    break
                except ValueError:
                    print("You must enter an integer")
        elif answer1 == str('salary'):
            while True:
                print ('What is your annual salary after taxes are taken out?')
                try:
                    answer2 = int(raw_input("enter number: ")) / 12
                    print ('Okay, you make '+ str(answer2) + ' a month.')
                    break
                except ValueError:
                    print("You must enter an integer")
        else:
            incomeerror()
            income()
        #Expenses
        while budget == 'yes':
            while True:
                print ('How much do you pay per month in rent?')
                try:
                    rent = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for education/tuition?')
                try:
                    education = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay in credit card payments?')
                try:
                    creditcard = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay in car payments?')
                try:
                    car = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay in other loans?')
                try:
                    loan = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for car insurance?')
                try:
                    carins = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for public transportation')
                try:
                    publictrans = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for cellphone/telephone service?')
                try:
                    telephone = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for cable/tv')
                try:
                    cable = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for heat/electricity?')
                try:
                    heatelec = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for water/sewer/garbage?')
                try:
                    water = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for gasoline?')
                try:
                    gasoline = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for groceries?')
                try:
                    groceries = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you spend eating out a month?')
                try:
                    eating = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for subscriptions like magazines or Netflix?')
                try:
                    subs = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much do you pay for memberships?')
                try:
                    memberships = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            while True:
                print ('How much are your other miscellaneous expenses?')
                try:
                    miscellaneous = int(raw_input("enter number: "))
                    break
                except ValueError:
                    print("You must enter an integer")
            expenses = rent + education + creditcard + car + loan + carins + telephone + cable + heatelec + water + gasoline + publictrans + groceries + eating + subs + memberships + miscellaneous
            print ('Your monthly expenses are ' + str(expenses))
            monthly=answer2-expenses
            if monthly > 500:
                print ('Nicely done.')
            elif monthly < 500:
                print ('You may need to lower your expenses.')
            print ('Your available budget is: ' + str(monthly))
            return

name = raw_input('Hello, what is your name? ')
budget = 'yes'
print ('Hi ' + name + " Let's calculate your budget")
newline()


income()


