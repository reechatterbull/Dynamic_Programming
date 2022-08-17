""" This is a program to find possible combinations of all elements that add up to a sum (Leetcode - 494) - using caching """

class Dynamic_Sum:
  def __init__(self,nums,target):
    self.arr = nums
    self.target = target

  def findTargetSumWays(self):
    dp = {} #Creating a hash map to map the (index,total) so far --> no of ways

    def backtrack(index,total):
      if index == len(self.nums):
        return 1 if total == self.target else 0
      if (index,total) in dp: #Note that (index,total) is the key and the sum is the value
        return dp[(index,total)]
      
      dp[(index,total)] = (backtrack(index+1,total+self.nums[index]) + 
                           backtrack(index+1,total - self.nums[index])
      

  