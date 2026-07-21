"""12.Problem Description"""
"""
Vohra went to a movie with his friends in a Wave theater and during break time he bought pizzas.puffs and cool drinks. Consider the following prices:
 - Rs 100/Pizza
 - Rs 20/puffs
 - Rs 10/cooldrink

Generate bill for What Vohra has bought. 
"""
"""
Sample Input 1:
 -Enter the no of Pizzas bought:10
 -Enter the no of puffs bought :12
 -Enter the no of cool drinks bought : 5

Sample Input 1:
 Bill Details
  -No of pizzas: 10
  -No of Puffs : 12
  -No of cooldrinks : 5
  -Total price = 1290

ENJOY THE SHOW!!!   
"""

pizza_count=int(input("Enter the no of pizza bought:"))

puffs_count=int(input("Enter the no of puffs bought:"))

drinks_count=int(input("Enter the no of cool drinks:"))

bill=pizza_count*100+puffs_count*20+drinks_count*10

print("Bills Details")
print("No of pizzas:{}".format(pizza_count))
print("No of puffs:{}".format(puffs_count))
print("No of cooldrinks:{}".format(drinks_count))
print("Total price={}".format(bill))
print("ENJOY THE SHOW!!!")