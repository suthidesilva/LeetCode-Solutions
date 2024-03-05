class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Initial setup: factorial values and available numbers
        factorials = [1]
        numbers = [str(i) for i in range(1, n+1)]
        # Precompute the factorials
        for i in range(1, n):
            factorials.append(factorials[i-1] * i)
        
        # Adjust k to be zero-indexed
        k -= 1
        # Build the k-th permutation
        permutation = ""
        for i in range(n-1, -1, -1):
            # Determine the current digit
            index = k // factorials[i]
            k %= factorials[i]
            
            permutation += numbers[index]
            # Remove the used number
            numbers.pop(index)
        
        return permutation
