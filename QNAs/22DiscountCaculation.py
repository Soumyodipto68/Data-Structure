"""22.Problem Statement"""


"""
Mayuri buys "N" no of products from a shop.The Shop offers a different percentange of discount on each item. She wants to know the item that has minimum discount offer, so that she can avoid buying that and save money.

[Input Format:The first input refers to the no of items;the second input is the item name,price,and discount percentage separated by comma(,)]

Assume the minimum discount offer is in the form of integer.

Note: There can be more than one product with a minimum discount.

Sample Input 1:
4

mobile,10000,20
shoe,5000,10
watch,6000,15
laptop,35000,5

Sample Output 1:
shoe
"""

items=int(input())
itemList=[]
for i in range(items):
  itemList.append(input().split(","))
list2=[]
for i in itemList:
  i.append((int(i[1])*int(i[2]))//100)
  list2.append(i[3])
result=[]
minimum=min(list2)
for i in itemList:
  if i[3] == minimum:
    result.append(i[0])
for i in result:
  print(i)