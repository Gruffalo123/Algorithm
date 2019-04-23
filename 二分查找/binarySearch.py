def binarySearch(list,item):
    found = False
    first = 0
    last = len(list) - 1

    while first <= last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1

    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binarySearch(test_list,2))
print(binarySearch(test_list,4))