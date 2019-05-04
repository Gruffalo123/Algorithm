def insert2(list):
    n = len(list)
    for j in range(1,n):
        i = j
        while i > 0:
            if list[i] < list[i-1]:
                list[i],list[i-1] = list[i-1],list[i]
                i -= 1#这就是为什么要引入 j
            else:
                break
    return list

test_list = [54,26,93,17,77,31,44,55,20]
print(insert2(test_list))