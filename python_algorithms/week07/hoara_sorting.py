# Сортировка Хоара

from random import randint, shuffle, choice

SIZE = 9
array = [randint(0, 10) for i in range(SIZE)] # массив из рандомных чисел (возможны повторения чисел)

#array = [i for i in range(SIZE)]
#shuffle(array)
print(array)

def quick_sort(array):

    if len(array) <= 1: # base case for recursion
        return array

    pivot = choice(array)
    s_ar = [] # small array
    m_ar = [] # medium array
    l_ar = [] # large array

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Error comes up')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

print(quick_sort(array))