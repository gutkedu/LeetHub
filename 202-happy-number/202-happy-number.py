class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()
        
        while True:
            if n == 1:
                return True
            
            currentSum = 0
            num = n
            
            while num:
                currentSum += (num % 10) ** 2
                num = num // 10
                
            if currentSum not in hashmap:
                hashmap.add(currentSum)
                n = currentSum
            
            else:
                return False
        