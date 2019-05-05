def mergerSort2(list):
    n = len(list)
    if n <= 1:
        return list
    mid = n//2

    left_li = mergerSort2(list[:mid])

    right_li = mergerSort2(list[mid:])

    left_index,right_index = 0,0
    result = []

    while left_index < len(left_li) and right_index < len(right_li):
        if left_li[left_index] < right_li[right_index]:
            result.append(left_li[left_index])
            left_index += 1
        else:
            result.append(right_li[right_index])
            right_index += 1
    result += left_li[left_index:]
    result += right_li[right_index:]
    return result

test_list = [54,26,93,17,77,31,44,55,20]
print(mergerSort2(test_list))