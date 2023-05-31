import random


def quick_sort(values):
    if 1 >= len(values):
        return values
    rand_idx = random.randint(0, len(values) - 1)
    pivot = values[rand_idx]
    first_value = values[0]
    values[0] = pivot
    values[rand_idx] = first_value
    less_than_pivot = []
    greater_than_pivot = []
    for v in values[1:]:
        if v <= pivot:
            less_than_pivot.append(v)
        else:
            greater_than_pivot.append(v)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


list = [6, 3, 8, 4, 9, 0, 7, 5, 2, 1]
print(quick_sort(list))
