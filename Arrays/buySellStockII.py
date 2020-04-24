# buySellStockII.py


# fifth time 
def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# fourth time

def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        for i, p in enumerate(prices):
            if i > 0 and p > prices[i-1]:
                profit += p - prices[i-1]
                
        return profit

#third time

def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        for i, n in enumerate(prices):
            if i > 0 and n > prices[i-1]:
                profit += n - prices[i-1]
        
        return profit

# second time, ez now that i know its simplicity
def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit

# provided solution, stupid easy. I thought about it too hard

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
