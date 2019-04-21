def sequentialSearch(list,item):
    position = 0
    found = False

    while position < len(list) and not found:
        if list[position] == item:
            found = True
        else:
            position += 1

    # 每调用一次，循环结束，return直接退出函数
    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print(sequentialSearch(test_list,2))
print(sequentialSearch(test_list,0))
print(sequentialSearch(test_list,-2))