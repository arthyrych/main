print('Homework 6\n')

print('Function 1\n')
# Создать функцию, которая:
# Принимает последовательность чисел
# Превращает ее в список
# Выводит первый и последний элемент списка
my_list = []


def first_last():
    while True:
        x = input('Enter a number to add to the list or enter EXIT to exit:\n')
        if x == 'EXIT':
            break
        else:
            my_list.append(x)


first_last()
print('You\'ve created this list:', my_list)
print('The first value in the list is', my_list[0], 'and the last value in the list is', my_list[-1])
