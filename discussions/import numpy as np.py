import numpy as np
arr = np.array([0, 1])
print(arr)

#adding arrays

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3= array1+array2
print(array3) #remember for things to be seen happen you have to print)

#appending arrays: combines them

array4= np.append(array1, array2)
print(array4)

#subtracting arrays
array5= array2-array1
print(array5)

#indexing arrays: for one value 
array8 = array1[1]
print(array8)

#slicing arrays: with: colon 

my_arr = np.array([10, 20, 30, 40, 50,60])
array9 = my_arr[4:6]
print(array9)

#summing sliced arrays
sum = np.sum(my_arr)
print(sum)

#standard deviation 
std= np.std(my_arr)
print(std)

#practice
    #for loop 
total_sum = 0 
for i in range(1,101): #(start, stop)
    total_sum += i 
print(total_sum)
    #array
numbers = np.arange(1, 101)
my_sum = np.sum(numbers)
print(my_sum)

#1D array and 2D array
one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d)

