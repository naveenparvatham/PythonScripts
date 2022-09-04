# Q(6): Create a numpy array and filter the elements greater than 5.
import numpy as np

# npy_arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# npy_lst = []
# for n in range(len(npy_arr)):
#     for n1 in range(len(npy_arr[n])):
#         if npy_arr[n][n1] > 5:
#             npy_lst.append(npy_arr[n][n1])
# print("Elements greater than 5:", npy_lst)

# Q(7): Create a numpy array having NaN (Not a Number) and print it.

# npy_arr_nan = ([np.nan, 1., 2., np.nan, 3., 4., 5.])
# add_arr = []
# add_arr1 = []
# for nan_value in range(len(npy_arr_nan)):
#     add_arr.append(npy_arr_nan[nan_value])
# for nan_value1 in range(len(npy_arr_nan)):
#     add_arr1.append(nan_value1)
# print(add_arr)
# print(add_arr1)


# Q(8): Create a 10x10 array with random values and find the minimum and maximum values.

# npy_mat = np.random.randint(10, size=(10, 10))
#
# for min_val in range(10):
#     min_value = np.amin(npy_mat[min_val])
#     max_value = np.amax(npy_mat[min_val])
#     print("Array Index %d : Min Value || %d Max Value || %d"
#           % (min_val, min_value, max_value))

# Q(10): Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9

# npy_mat_1 = np.random.randint(10, size=(1, 10))
# npy_ar = np.negative(npy_mat_1)
# x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
# print("Original array:")
# print(x)
# print("Replace the negative values of the said array with 0:")
# x[x < 0] = 0
# print(x)
# print(npy_mat_1)


# Q(11): Create a random array of 3 rows and 3 columns and sort it according to 1st column 2nd column or 3rd column.

# npy_arr = np.random.randint(10, size=(3, 3))
# npy_sort = np.sort(npy_arr)
# print("Original Numpy Array: \n ", npy_arr)
# print("Sorted Numpy Array: \n ", npy_sort)


# Q(12): Create a four dimensions array get sum over the last two axis at once.

# npy_arr = np.random.randint(10, size=(4, 4, 4))
# arr_sum = npy_arr.sum(axis=(1, 2))
# print(npy_arr)
# print(arr_sum)

# Q(13): Create a random array and swap two rows of an array.

# npy_mat2 = np.random.randint(10, size=(4, 4))
# arr_sum11 = np.swapaxes(npy_mat2, 0, 1)
# print("Original Array : \n", npy_mat2)
# print("\nSwapped Array : \n", arr_sum11)


# Q(14): Create a random matrix and Compute a matrix rank.

npy_mat3 = np.random.randint(10, size=(4, 4))
npy_mat4 = np.matrix.view(npy_mat3)
print("", npy_mat3, "\n")
print(npy_mat4)













