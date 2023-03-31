#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

coins_count = int(input("Введите количество монеток: "))
coins_head_count = randint(0, coins_count)
coins_tails_count = coins_count - coins_head_count

print(f"Орлом упало {coins_head_count} монет, а решкой {coins_tails_count}.")

if coins_head_count == coins_tails_count:
    print("На столе равное количество орлов и решек!!")
elif coins_head_count > coins_tails_count:
    print(f"Орлов больше, надо перевернуть решки ({coins_tails_count}шт).")
else:
    print(f"Решек больше, надо перевернуть орлов ({coins_head_count}шт).")