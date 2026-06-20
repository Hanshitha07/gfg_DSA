class Solution:
    def maxCircularSum(self, arr):
        # code here
        curr_max=arr[0]
        max_sum=arr[0]
        for num in arr[1:]:
            curr_max=max(num,curr_max+num)
            max_sum=max(max_sum,curr_max)
        
        if max_sum<0:
            return max_sum
        total = sum(arr)
        
        curr_min=arr[0]
        min_sum=arr[0]
        
        for num in arr[1:]:
            curr_min=min(num,curr_min+num)
            min_sum=min(min_sum,curr_min)
        
        circular_sum=total-min_sum
        
        return max(max_sum,circular_sum)
        