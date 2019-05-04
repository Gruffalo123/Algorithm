def bubble_sort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list

alist = [54,26,93,17,77,31,44,55,20]
print(bubble_sort(alist))