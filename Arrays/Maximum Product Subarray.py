class Solution:
    def maxProduct(self, arr):
        max_prod = arr[0]
        min_prod = arr[0]
        ans = arr[0]

        for i in range(1, len(arr)):
            num = arr[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            ans = max(ans, max_prod)

        return ans