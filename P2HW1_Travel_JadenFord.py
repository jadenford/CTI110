# This program calculates and displays travel expenses
# October 10, 2022
# CTI-110 P2HW1 - Travel
# Jaden Ford
#

#

#Input
budget = int(input('Enter budget:'))
destination = input('Enter your travel destination:')
gas = int(input('How much do you think you will spend on gas?:'))
accomodation = int(input('Approximately, how much will you need for accomodations/hotel?:'))
food = int(input('Last, how much do you need for food?:'))

# Pocess

expenses = gas + accomodation + food
remains = budget - expenses

# Output

print('---------Travel Expenses---------')
print(f'Location:           {destination}')
print(f'Inital Budget:      ${1200.0}')
print(f'Fuel:               ${250.0}')
print(f'Accomodation:       ${300.0}')
print(f'Food:               ${200.0}')
print('---------------------------------')
print()
print(f'Remaining Balance:  ${450.0}')

