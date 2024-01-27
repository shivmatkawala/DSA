# Binary Search Algorithm..
# THe Time Complexity:- Best Case= O(1), Worst Case= O(log n), average Case= O(log n)

arr_1 = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

data = 840

n = len(arr_1)
l = 0
r = n - 1
while l <= r:
    mid = int((l + r) // 2)
    if data == arr_1[mid]:
        print(f"{data} is found at index number: {mid}")
        break
    elif data < arr_1[mid]:
        r = mid - 1
    else:
        l = mid + 1
else:
    print(f"{data} Not Found")
