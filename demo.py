import random
#githun upload
a = random.randint(1,999)
b = int(input('input a number from 1 to 999:'))
while True:
    if a>b:
        b = (int(input('less than the number,keep on input!:')))
    elif a<b:
        b = (int(input('more than the number,keep on input!:')))
    else:
        print('you r right!,the number is:',a)
        break