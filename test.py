"""
i = 0
while i < 1:
    user_name = input('Please enter the user name: ')
    if user_name == 'ahmad':
        y = 0
        while y < 1:
            user_pass = input('Please enter the password: ')
            if user_pass == '123':
                print('welcom')
                y = 2
                i = 2
            else:
                print('wrong password')
    else:
        print('Wrong user name')
"""
# factorial
"""
n = int(input('Please enter number to calculate factorial: '))
r = 0
for i in range(n):
    i = i * (i + 1)
    r = i
print(r)
"""
# pandas graph
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
"""
# prints odd number.

final_num = int(input('Please enter the final number to see odds number upto :'))
for x in range(1, final_num + 1):
    if (x % 2) == 1:
        print(x)
    else:
        continue
    
    
# home work find duplicates, sum of odds and sum of even nums