"""9 Problem: Matrix Problem"""

"""
You are required to input the size of the matrix and the elements of the matrix and then you have to divide the matrix in two sub matrices (even and odd)

in such a way elements at 0 index will be in even matrix and elements at 1 index will be in odd matrix and so on.

Then you have sort even an odd matrices in asscending order then print the sum of second largest number form both the matrices.

Example:
Enter the Size of array:5
Enter the element at 0 index: 3
Enter the element at 1 index: 4
Enter the element at 2 index: 1
Enter the element at 3 index: 7
Enter the element at 4 index: 9
Sorted even array : 1 3 9
Sorted odd array  : 4 7

Output:
7
"""

array = []
evenArr = []
oddArr = []
n = int(input("Enter the size of the array:"))
for i in range(0,n):
  number = int(input("Enter Element at [] index:".format(i)))
  array.append(number)
  if i%2 == 0:
    evenArr.append(array[i])
  else:
    oddArr.append(array[i])  

evenArr = sorted(evenArr)    
print("Sorted Even Array:",evenArr[0:len(oddArr)])
print(evenArr[1]+oddArr[1])