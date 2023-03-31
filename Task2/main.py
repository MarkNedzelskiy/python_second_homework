#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
from random import randint

first_number = randint(1, 1000)
second_number = randint(1, 1000)

numbers_summ = first_number + second_number
numbers_product = first_number * second_number

print(f"Петя подсказывает сумму чисел {numbers_summ} и проиведение чисел {numbers_product}")

x = 0
y = 0

d = numbers_summ * numbers_summ - 4 * numbers_product

if d > 0:
    x = (-numbers_summ + math.sqrt(d)) / 2
    y = (-numbers_summ - math.sqrt(d)) / 2
elif d == 0:
    x = (-numbers_summ + math.sqrt(d)) / 2
    y = x


print(f"Катя посчитала, первое число равно {int(-x)}, а второе {int(-y)}")