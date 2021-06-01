number = int(input('Please enter a number that all odds and even numbers can be sumec upto: '))
odd_total = 0
even_total = 0

for n1 in range(1, (number + 1), 2):
    odd_total += n1

for n2 in range(2, (number + 1), 2):
    even_total += n2
  
print('The Sume of even Numbers upto {} is ={} and sum of even is ={}'.format(number, even_total, odd_total))
