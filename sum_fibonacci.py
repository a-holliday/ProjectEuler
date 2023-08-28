sum = 0
n = 1
previous_n = 0
while n < 4000000:
    temp = n
    n = previous_n + n 
    if n % 2 == 0:
        sum += n
    previous_n = temp


print(sum)