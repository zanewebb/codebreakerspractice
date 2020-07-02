# i hate this problem, doesnt work
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        
        if dividend < 0 and divisor > 0:
            negative = True
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            negative = True
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend
            
        counts = []
        doubles = []
        ans = 0
        count = divisor
        doubled = 1
        while count <= dividend:
            if count > 2147483647:
                return 2147483647
            counts.append(count)
            doubles.append(doubled)
            count += count
            doubled += doubled
    
        if len(counts) > 0:
            dividend -= counts[-1]
            ans += doubles[-1]
        
        i = len(doubles) - 1
        while i >= 0:
            if counts[i] < dividend:  
                dividend -= counts[i]
                ans += doubles[i]
            i -= 1
        
        return ans if not negative else -ans



# sloppy but i solved it
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else True
        
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        
        if divisor == dividend:
            return 1 if not negative else -1
        
        cur = 0
        count = 1
        ans = 0
        
        doubles = []
        counts = []
        
        cur = divisor
        i = 0
        while cur < dividend:
            # add the new values
            doubles.append(cur)
            counts.append(count)

            # double things
            cur += cur
            count += count

            # move the iterator
            i += 1

        # subtract the doubled up to amount
        i -= 1
        if i >= 0:
            dividend -= doubles[i]
            ans += counts[i]
        else:
            return ans if not negative else -ans
        
        
        # now we continue to chip away the remainders with our already
        # calculated doubles and counts
        while i >= 0 and dividend > 0:
            # find the next biggest double that fits in our remainder
            while i >= 0 and doubles[i] > dividend:
                i -= 1
            if i >= 0:
                ans += counts[i]
                dividend -= doubles[i]
            # print("i",i, "dividend",dividend, "ans",ans)
            
        if ans > 2147483647 and not negative:
            return 2147483647
        return ans if not negative else -ans
            
            
            
        
        
        '''
        [3, 6, 12]
        [1, 2, 4 ]
        
        10
        3
        '''
        



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powersOfTwo = []

        # Nothing too exciting here, we're just making a list of doubles of 1 and
        # the divisor. This is pretty much the same as Approach 2, except we're
        # actually storing the values this time. */
        powerOfTwo = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            # Prevent needless overflows from occurring...
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor # Double divisor
            powerOfTwo += powerOfTwo

        # Go from largest double to smallest, checking if the current double fits.
        # into the remainder of the dividend.
        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                # If it does fit, add the current powerOfTwo to the quotient.
                quotient += powersOfTwo[i]
                # Update dividend to take into account the bit we've now removed.
                dividend -= doubles[i]

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return quotient if negatives != 1 else -quotient    