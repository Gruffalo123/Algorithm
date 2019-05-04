def select2(list):
    n = len(list)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if list[min_index] > list[i]:
                min_index = i
        list[j],list[min_index] = list[min_index],list[j]
    return list

test_list = [54,26,93,17,77,31,44,55,20]
print(select2(test_list))