def packBag(maxWeight, w, p, n): 
  
    if n == 0 or maxWeight == 0 : 
        return 0
  
    # If weight is greater than max weight, dont include and go to next bag
    if (w[n-1] > maxWeight): 
        return packBag(maxWeight , w , p , n-1) 
  
   # weight is not greater, return the optimal of the two
    else: 
        return max(p[n-1] + packBag(maxWeight-w[n-1] , w , p , n-1), 
                   packBag(maxWeight , w , p , n-1)) 
  

prices = [250, 175, 400, 200, 500, 125, 500, 250, 175, 250, 100] 
weights = [3.5, 2, 5, 3, 5.5, 1.5, 6, 4, 2.5, 4.5, 1] 
maxWeight = 20
n = len(prices) 
print(packBag(maxWeight, weights, prices, n)) 