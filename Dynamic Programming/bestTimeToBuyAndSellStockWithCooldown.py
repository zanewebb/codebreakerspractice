# Fourth time, still not quite getting it
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        didSell = -999999
        canSell = -999999
        reset = 0
        
        
        for p in prices:
            
            preSell = didSell
            
            didSell = canSell + p
            
            canSell = max(canSell, reset-p)
            
            reset = max(preSell, reset)
        
        return max(reset, didSell)


# third time? still super confusing
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # do not have stock
        didSell = -99999
        # have stock
        haveStock = -99999
        
        # do not have stock
        temp = 0
        
        for p in prices:
            yesterdaysSell = didSell
            
            # sell today with our haveStock from yesterday (only state that has stock)
            didSell = haveStock + p
            
            # to have stock today, I must have had it yesterday or purchased it today (from our backup point)
            haveStock = max(temp - p, haveStock)
            
            # we hold onto a temp (backup) that only updates when our sell earned us profit 
            temp = max(yesterdaysSell, temp)
            
        
        return max(temp, didSell)
        


# Annotated version of the LC solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp problem
        # did sell, we couldnt have already sold anything on the first day
        didSell = -9999999
        # can sell, didnt,  we couldnt have already purchased anything on the first day
        canSell = -9999999
        # wait
        waiting = 0
        
        for p in prices:
            yesterday_sold = didSell
            # Update the scenario where we sell today, for reference tomorrow
            # Status: We had stock, and have sold it. No decision to make, we progress to waiting
            # Action: SELL --> we sold
            didSell = canSell + p
            
            # either continue holding, or 
            # Status: We now have stock
            # Actions: WAIT(already have stock, continue waiting) or BUY (did not have stock)
            canSell = max(canSell, waiting - p)
            
            # is it better to have continued waiting(no stock in hand) or have sold the day before? (no stock in hand)
            # Status: We do not have stock
            # Actions: WAIT(we had no stock anyways), WAIT(must wait after selling)
            waiting = max(waiting, yesterday_sold)
            
        
        return max(waiting, didSell)

#provided solution 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)


# non working solution, close, LC provides an O(1) space solution that is very similar
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp problem
        # can buy, we waited the first day
        s1 = [None] * len(prices)
        s1[0] = -9999
        # can sell, starting val is implying we bought on the first day
        s2 = [None] * len(prices)
        s2[0] = -prices[0]
        # must wait
        s3 = [None] * len(prices)
        s3[0] = -999999
        
        i = 1
        while i < len(prices):
            # the best outcome of today, being able to now buy
            # is the better of the two ways to be in this state, from yesterday
            # that is, from being forced to wait after selling
            # or from waiting after not buying the day prior already
            s1[i] = max(s3[i-1] ,s1[i-1])
                           
            # The best outcome of today, being able to now able to sell
            # is the better outcome of the two ways to arrive at this state from yesterday
            # 1. we bought yesterday and wish to sell today
            # 2. we bought some number of days prior and can still sell today
            s2[i] = max(s1[i-1] - prices[i-1], s2[i-1])
                           
            # The best outcome of today, is either continuing to wait, or 
            # selling the day before
            s3[i] = max(s3[i-1], s2[i-1] + prices[i-1])
            
            i += 1
        
        return max(s3[-1], s1[-1])

class Solution:

   # first time, ouch this kicked my ass. Needed extensive help with the lc forums

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        canSell, canBuy, mustWait = [0] * len(prices), [0] * len(prices), [0] * len(prices)

        # set initial state
        canBuy[0] = 0
        canSell[0] = -prices[0] # investment deficit intially
        mustWait[0] = -9999999999999 # no way to have mustWait initially
        # build answer set
        # when populating each index, choose the better result of the two other states you came from
        i = 1
        while i < len(prices):
            # only could arrive to this state if you HAD to wait, or did nothing AFTER HAVING to wait 
            # is it better to have just come from a sale or to have continued to wait
            canBuy[i] = max(canBuy[i-1], mustWait[i-1])
            
            # is it better to wait, or to have bought
            canSell[i] =  max(canSell[i-1], canBuy[i-1] - prices[i])
            
            # Could only have arrived at the mustWait state by selling
            # add the price of today, move on
            mustWait[i] = canSell[i-1] + prices[i]
            
            i += 1
        return max(canBuy[-1], mustWait[-1])