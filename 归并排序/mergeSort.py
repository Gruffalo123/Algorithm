def mergeSort(list):
    n = len(list)
    if n <=1:
        return list
    mid = n//2

    #采用归并排序后形成的有序的新的列表
    left_li = mergeSort(list[:mid])
    right_li = mergeSort(list[mid:])

    #将两个有序的子序合并为一个新的整体
    left_point,right_point = 0,0
    result = []

    while left_point < len(left_li) and right_point < len(right_li):
        if left_li[left_point] < right_li[right_point]:
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1

    
    result += left_li[left_point:]
    result += right_li[right_point:]
    return result

if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print(test_list)
    end_list = mergeSort(test_list)
    print(test_list)
    print(end_list)