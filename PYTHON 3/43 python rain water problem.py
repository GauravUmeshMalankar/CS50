"""
# Python3 implementation of the approach
  
# Function to return the maximum
# water that can be stored
def maxWater(arr, n):
  
    # To store the maximum water
    # that can be stored
    res = 0
  
    # For every element of the array
    for i in range(1, n - 1):
  
        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
  
        # Find the maximum element on its right
        right = arr[i]
  
        for j in range(i + 1, n):
            right = max(right, arr[j])
  
        # Update the maximum water
        res = res + (min(left, right) - arr[i])
  
    return res
  
  
# Driver code
if __name__ == "__main__":
  
    arr = [4,2,0,3,2,5]
    n = len(arr)
  
    print(maxWater(arr, n))
  
# This code is contributed by AnkitRai01
"""

class Solution(arr, n):
    def trap(arr, n):

        water = 0

        for i in range(1,n-1):

            left = arr[i]
            for j in range(i):
                left = max(left, arr[j])

            
            right = arr[i]
            for j in range(i+1,n):
                left = max(right, arr[j])
            
            water = water + (min(left, right)-arr[i])
        
        return water

if __name__ == "__main__":

    arr = [4,2,0,3,2,5]
    n = len(arr)

    print(Solution(arr, n))  
    
    Solution.trap() 
