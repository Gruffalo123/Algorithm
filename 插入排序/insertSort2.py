def insertSort(list):
    for index in range(1,len(list)):

        currentvalue = list[index]
        position = index

        while position>0 and list[position-1] > currentvalue:
            list[position] = list[position-1]
            position -= 1

        #1，如果执行了while，则position= position-1  2，如果没有执行while，还是当前位置
        list[position] = currentvalue


if __name__ == '__main__':
    test_list = [54,26,93,17,77,31,44,55,20]
    print(test_list)
    insertSort(test_list)
    print(test_list)

