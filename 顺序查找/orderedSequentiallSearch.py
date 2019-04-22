#有序列表
def orderedSequntialSearch(list,item):
    position = 0
    found = False
    stop = False

    while position < len(list) and not found and not stop:
        if list[position] == item:
            found = True
            #stop加在这里，只能匹配一次，如果有多个匹配的item。。（自己理解的
            # stop = True
        else:
            #因为列表有序，当前值大于目标的时候，就是找不到了，可以停止循环
            if list[position] > item:
                stop = True
            else:
                position += 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(orderedSequntialSearch(testlist,3))
print(orderedSequntialSearch(testlist,13))