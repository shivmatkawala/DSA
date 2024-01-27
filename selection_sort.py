arr_1 = [12, 7, 8, 3, 9, 2]

# Ascending Order..
# for i in range(len(arr_1)):
#     min_indx = i
#     for j in range(i+1, len(arr_1)):
#         if arr_1[min_indx] > arr_1[j]:
#             min_indx = j
#
#     arr_1[i], arr_1[min_indx] = arr_1[min_indx], arr_1[i]
# print(arr_1)


# Descending Order...
for i in range(len(arr_1)):
    min_indx = i
    for j in range(i+1, len(arr_1)):
        if arr_1[min_indx] < arr_1[j]:
            min_indx = j

    arr_1[i], arr_1[min_indx] = arr_1[min_indx], arr_1[i]
print(arr_1)




