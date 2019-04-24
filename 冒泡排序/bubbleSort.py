def bubbleSort(list):
    #每一次都少一项排序，
    for passnum in range(len(list)-1,0,-1):
    #range(9-1,0,-1)=[8,7,6,5,4,3,2,1]
        #第一次，range(8),[0~7],8项，n-1=8,以此类推
        for i in range(passnum):
            if list[i] > list[i+1]:

                # 执行同时赋值
                # list[i],list[i+1] = list[i+1],list[i]

                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

test_list = [54,26,93,17,77,31,44,55,20]
bubbleSort(test_list)
print(test_list)