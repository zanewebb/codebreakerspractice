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