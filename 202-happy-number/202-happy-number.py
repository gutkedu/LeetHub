class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        
        return False
            
    def sumOfSquares(self,n:int)->int:
        num_string, n_sum = str(n), 0
        for s in num_string:
            n_sum += pow(int(s),2)
        return n_sum
        