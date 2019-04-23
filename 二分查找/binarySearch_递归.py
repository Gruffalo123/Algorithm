def binarySearch(list,item):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == item:
            return True
        else:
            if list[midpoint] < item:
                return binarySearch(list[midpoint+1:],item)
            else:
                return binarySearch(list[:midpoint],item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binarySearch(test_list,2))
print(binarySearch(test_list,4))