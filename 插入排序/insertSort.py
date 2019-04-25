def insertSort(list):
    for j in range(1,len(list)):
        i = j
        while i>0:
            if list[i] < list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
                i -= 1
            #优化
            else:
                break

test_list = [54,26,93,17,77,31,44,55,20]
print(test_list)
insertSort(test_list)
print(test_list)