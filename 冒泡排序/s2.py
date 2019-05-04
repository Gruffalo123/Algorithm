def s2(list):
    num = len(list)-1
    exchanges = True
    while num > 0 and exchanges:
        exchanges = False
        for i in range(num):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                exchanges = True
        num -= 1
    return list

alist = [54,26,93,17,77,31,44,55,20]
print(s2(alist))