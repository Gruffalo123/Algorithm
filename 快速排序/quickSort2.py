def quickSort2(list,first_position,last_position):

    if first_position >= last_position:
        return
    mid_value = list[first_position]

    low_index = first_position
    high_index = last_position

    while low_index < high_index:

        while low_index < high_index and list[high_index] >= mid_value:
            high_index -= 1
        list[low_index] = list[high_index]

        while low_index < high_index and list[low_index] < mid_value:
            low_index += 1
        list[high_index] = list[low_index]

    list[low_index] = mid_value

    quickSort2(list,first_position,low_index-1)
    quickSort2(list,low_index+1,last_position)

    return list


test_list = [54,26,93,17,77,31,44,55,20]
print(quickSort2(test_list,0,len(test_list)-1))

