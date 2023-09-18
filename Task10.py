print('введите количество монеток')

n = int(input())
minRevol = 0
count0 = 0
count1 = 0
for i in range(n):
    print('введите сторону монетки: 0 - решка, 1 - орел')
    sideCoin = int(input())
    if sideCoin == 0:
        count0 += 1

    else:
        count1 += 1

if count0 >= count1:
    minRevol = count1
else:
    minRevol = count0

print(f'{minRevol} монеток нужно перевернуть')