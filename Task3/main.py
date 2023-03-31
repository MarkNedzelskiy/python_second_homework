#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N: "))

count = 2
i = 1

while True:
    count_power = count ** i
    if count_power >= n:
        break
    print(f"{count_power} ", end ='')
    i += 1