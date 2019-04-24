# 特别地，如果在遍历期间没有交换，则我们知道该列表已排序。
# 如果发现列表已排序，可以修改冒泡排序提前停止。
# 这意味着对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点。

def shortBubbleSort(list):
    exchanges = True
    passnum = len(list)-1

    while passnum > 0 and exchanges:
        #如果没有交换，就是False，已经排序，可以提前停止
        exchanges = False

        for i in range(passnum):
            if list[i] > list[i+1]:
                exchanges = True
                list[i], list[i + 1] = list[i + 1], list[i]

        passnum -= 1
