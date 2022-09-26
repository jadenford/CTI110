# This program calculates and displays travel expenses
# September 22,2022
# CTI-110 P1HW2 - Travel Expense
# Jaden Ford
#

#

#Input
budget = int(input('Enter budget:'))
destination = input('Enter travel destination:')
gas = int(input('Enter how much will be spent on gas:'))
accomodation = int(input('enter how much will be spent on accomodations:'))
food = int(input('Enter how much will be spent on food:'))

# Pocess

expenses = gas + accomodation + food
remains = budget - expenses


# Ouput

print('---------Travel Expenses---------')
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
print()
print('Remaining Balance:', remains)
