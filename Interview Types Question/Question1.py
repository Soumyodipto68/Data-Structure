"""
There is a JAR full of candidates for sale at a mall counter. JAR has the capacity N. that is JAR can contain maximum N candies when JAR is full. At any point of time. JAR can have M numbers of Candies where M<=N. Candies are served to the customers.JAR is never remain empty when last k candies are left. JAR if refilled with new candies in such a way that JAR get full .


write a code to implement above scenario. Display JAR at counter with available number of candies.Input should be the number of candies one customer can oder at point of time. Update the JAR after each purchase and display JAR at Counter


Given,
N=10, where N is NUMBER OF CANDIES AVAILABLE
K=<5, where k is number of minimum candies that must be inside JAR ever

Example 1:(N=10,k=<5)

Input Value
  3
Output Value
  Number of candies sold 3
  Number of candies available 7

"""

N = 10 #TOTAL NUMBER OF CANDIES
K = 5  #MINIMUM NO OF CANDIES
M = int(input())
if N in range(1,K+1):
  print(f"NO OF CANDIES SOLD {M}")
  print(f"NO OF CANDIES LEFT {N-M}")
else:
  print("INVALID INPUT")