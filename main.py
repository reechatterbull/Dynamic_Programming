""" THIS IS A CODE TO USE DYNAMIC PROGRAMMING TO FIND THE MINIMUM NUMBER OF STEPS TO REDUCE AN INTEGER N TO 1. 
THE AVAILABLE STEPS ARE - 
1. SUBTRACT BY 1
2. DIVIDE BY 2
3. DIVIDE BY 3"""

class Min_Steps:
  #def __init__(self):
  def Minimizer(self,n: int) -> int:
    dp={} #Creating a dynamic programming hash table
    dp[0] = dp[1] = 0 #indices is the current number and value is the min number of steps to reduce the index to 1
    if n == 1:
      return dp[n]

    dp[n] = 1 + self.Minimizer(n-1)
    if n%2 == 0:
      dp[n] = min(dp[n],self.Minimizer(n/2)+1) 
    if n%3 == 0:
      dp[n] = min(dp[n],self.Minimizer(n/3)+1)

    return dp[n]
    
    
Solution = Min_Steps()
print(Solution.Minimizer(7))
    
      
     
    
    
    
    
      