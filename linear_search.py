# Linear Search...
# Time Complexity:- best case= O(1), worst case= O(n)

arr_1 = [15, 5, 20, 35, 2, 42, 67, 17]
n = len(arr_1)
data = 17

for i in range(0, n):
    if (arr_1[i] == data) and (i != n-1):
        print(f"{data} is available at index: {i}")
        break
    elif (arr_1[i] == data) and (i == n-1):
        print(f"{data} is available at index: {i}")
    elif (arr_1[i] != data) and (i == n-1):
        print(f"{data} is not available. ")
    else:
        pass
