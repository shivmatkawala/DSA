def recu_binary_search(array, left, right, num):
    while left <= right:
        mid = int((left + (right-1)) // 2)

        if array[mid] == num:
            return mid

        elif array[mid] > num:
            return recu_binary_search(array, left, mid-1, num)

        else:
            return recu_binary_search(array, mid+1, right, num)
    return -1


if __name__ == "__main__":
    arr_1 = [1, 20, 33, 45, 57, 69, 71, 89]
    n = len(arr_1)
    l = 0
    r = n - 1
    data = 69

    result = recu_binary_search(arr_1, l, r, data)
    if result != -1:
        print(f"{data} is available at index: {result}")

    else:
        print(f"{data} is not found..")

