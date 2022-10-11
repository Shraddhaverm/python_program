number = int(input('Enter number: '))
copy = number
digit_sum = 0
while number:
    digit_sum += number%10
    number //= 10

if copy%digit_sum == 0:
    print('%d is Harshad Number' % (copy))
else:
    print('%d is Not Harshad Number' % (copy))
    