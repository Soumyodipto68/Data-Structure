"""23.Problem Description"""

"""
Raj wants to know the maximum marks scored by him in each semester.The marks should be between 0 to 100, If goes beyond this range display  You have entered invalid marks.


Sample Input 1:
Enter the number of semesters: 3
Enter no of subjects in semester 1: 3
Enter no of subjects in semester 2: 4
Enter no of subjects in semester 3: 4

Marks of semester 1: 90,80,70
Marks of semester 2: 100,90,80,70
Marks of semester 3: 90,80,70,60

Sample Output 1:
Maximum marks scored in semester 1: 90
Maximum marks scored in semester 2: 100
Maximum marks scored in semester 3: 90
"""

no_of_semesters = int(input("Enter the number of semesters: "))
list1 = []
for i in range(no_of_semesters):
    print(f"Enter no of subjects in semester {i + 1}: ", end="")
    list1.append(list(range(int(input()))))
for i in range(no_of_semesters):
    print(f"Marks of semester {i + 1}: ")
    for j in range(len(list1[i])):
        list1[i][j] = int(input())
        if list1[i][j] < 0 or list1[i][j] > 100:
            print("You have entered invalid marks.")
            exit()
count = 1 
for i in list1:
    print(f"Maximum marks scored in semester {count}: {max(i)}")
    count += 1