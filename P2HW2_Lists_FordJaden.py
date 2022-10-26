mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

grade = [mod1, mod2, mod3, mod4, mod5, mod6]

print()
print('------------Results------------')
lowestGrade = min(grade)
highestGrade = max(grade)
gradesSum = sum(grade)
average = sum(grade)/len(grade)

print (f'Lowest Grade:            {lowestGrade:.2f}')
print (f'Highest Grade:           {highestGrade:.2f}')
print (f'Sum of Grade:            {gradesSum:.2f}')
print (f'Average:                 {average}')
print ('----------------------------------------')
