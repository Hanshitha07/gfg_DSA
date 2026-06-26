class Solution:
    def findMajority(self, arr):
        # code here
        freq={}
        
        for num in arr:
            freq[num]=freq.get(num,0)+1
            
        limit=len(arr)//3
        ans=[]
        
        for key,value in freq.items():
            if value>limit:
                ans.append(key)
        ans.sort()
        return ans