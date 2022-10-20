from random import randint



def get_unique_list_numbers(num) -> list[int]:

    a = [randint(-10,10) for i in range(num + 1)]
    count=1
    while len(a) != len(set(a)):
        a = [randint(-10, 10) for i in range(num + 1)]
        count+=1
    print(count) #любопытно сколько итераций требуется данному кастылю
    return a
    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers(14)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
