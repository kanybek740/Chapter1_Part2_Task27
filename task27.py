numbers = input('Enter the numbers:').split(',')
negative = []
positive = []
for num in numbers:
    if int(num) > 0:
        positive.append(num)

    elif int(num) < 0:
        negative.append(num)
    else:
        continue
print(negative)
print(positive) 