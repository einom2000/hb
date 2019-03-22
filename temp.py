num = input('Please input: ')
total = 0
for i in range(int(num.split(',')[0]), int(num.split(',')[1]) + 1):
    total += i
print(total)

