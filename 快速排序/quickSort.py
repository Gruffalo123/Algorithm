def quickSort(list,first_position,last_position):

    if first_position >= last_position:
        return
    mid_value = list[first_position]

    low_index = first_position
    high_index = last_position
    
    while low_index < high_index:
        #high_index左移
        while low_index < high_index and list[high_index] >= mid_value:
            high_index -= 1
        list[low_index] = list[high_index]

        while low_index <high_index and list[low_index] < mid_value:
            low_index += 1
        list[high_index] = list[low_index]

    #从循环退出时，low_index == high_index
    list[low_index] = mid_value

    #对low_index左边的列表执行快速排序
    quickSort(list,first_position,low_index-1)

    #对high_index右边的列表执行快速排序
    quickSort(list,low_index+1,last_position)

if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print(test_list)
    quickSort(test_list,0,len(test_list)-1)
    print(test_list)
