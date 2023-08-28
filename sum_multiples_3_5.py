tally = 0
sum = 0
for i  in range(1, 1000):
    if (i % 3 == 0):
        tally += i
        continue
    if (i % 5 == 0):
        tally += i
print(tally)    
    