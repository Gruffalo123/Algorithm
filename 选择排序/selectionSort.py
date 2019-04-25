def selectionSort(list):
    for fillsort in range(len(list)-1,0,-1):
        max_index = 0
        for location in range(1,fillsort+1):
            if list[location] > list[max_index]:
                max_index = location

        list[fillsort],list[max_index] = list[max_index],list[fillsort]

test_list = [54,26,93,17,77,31,44,55,20]
print(test_list)
selectionSort(test_list)
print(test_list)