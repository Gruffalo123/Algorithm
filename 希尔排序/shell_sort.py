def shell_sort(list):
    n = len(list)

    gap = n //2
    while gap>0:
        for j in range(gap,n):
            i = j
            while i>0:
                if list[i] < list[i-gap]:
                    list[i],list[i-gap] = list[i-gap],list[i]
                    i -= gap
                else:
                    break
        gap = gap//2

if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print(test_list)
    shell_sort(test_list)
    print(test_list)