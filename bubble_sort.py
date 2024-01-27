# Bubble Sort..
# time complexity:- best case= O(n), worst case= O(n**2)

arr_1 = [15, 16, 6, 8, 5]
n = len(arr_1)

for i in range(0, n-1):
    flag = 0
    for j in range(0, n-1-i):
        if arr_1[j] > arr_1[j+1]:
            temp = arr_1[j]
            arr_1[j] = arr_1[j+1]
            arr_1[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr_1)


