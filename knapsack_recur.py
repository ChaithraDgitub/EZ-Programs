
def knapsack(n,capacity,weights,prices):
     if(n==0 or capacity==0):
         return 0 
     
     if (weights[n-1]>capacity):
         return knapsack(n-1,capacity,weights,prices)
   
     else:
         return max(prices[n-1] + knapsack(n-1,capacity-weights[n-1],weights,prices),
                    knapsack(n-1,capacity,weights,prices))
         
weights = [1,2,3,4]
prices = [50,200,150,100]
n = 4
capacity = 7
print(knapsack(n,capacity,weights,prices))