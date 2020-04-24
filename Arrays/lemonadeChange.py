# lemonadeChange.py

class Solution:

    #fourth time
    def lemonadeChange(self, bills):
        # establish cash register values (only the values usable for change)
        fives = tens = 0
        
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10 and fives > 0:
                fives -= 1
                tens += 1
            elif b == 20 and tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif b == 20 and fives > 2:
                fives -= 3
            else:
                return False
        
        return True

# third time, ez

def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        
        for bill in bills:
            if bill is 5:
                fives += 1
            elif bill is 10 and fives > 0:
                fives, tens = fives - 1, tens + 1
            elif bill is 20 and tens > 0 and fives > 0:
                fives, tens = fives - 1, tens - 1
            elif bill is 20 and fives > 2:
                fives -= 3
            else:
                return False
        return True

# second go, ez
# 98% speed percentile yea boi

    def lemonadeChange(self, bills):
        # establish cash register values (only the values usable for change)
        fives = tens = 0
        
        for i in bills:
            
            if i == 5:
                fives += 1
            elif i == 10 and fives > 0:
                fives -= 1
                tens += 1
            elif i == 20 and tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif i == 20 and fives > 2:
                fives -= 3
            else:
                return False
        
        return True


   # first try, super not optimal, 5% and 7% ouch

   #INDEX SEARCHES AND POPS KILLED IT TIME WISE
    def lemonadeChange(self, bills: List[int]) -> bool:
        # if the first bill isnt a 5 theres no way to return change with no starting change
        if bills[0] != 5:
            return False
        
        # iterate over the input array
        i = 0
        while i <= len(bills)-1:
            #print("Evaluating: ", bills[i])
            # if the input is a 5, accept, move on
                
            # if the input is a 10 
            if bills[i] == 10:
                # check if the list [0:i] contains a 5
                if 5 in bills[0:i]:
                    # if so, pop index of the 5
                    bills.pop(bills[0:i].index(5))
                    i -= 1
                # if not, false
                else:
                    print("failed check on a 10")
                    return False


            # if the input is a 20
            if bills[i] == 20:
                # check if the list [0:i] has at least a 5 and a 10 OR at least 3 5's
                # pop either the 5 and 10, or the 3 5's
                
                # we should prefer to rid ourselves of 10's
                if 10 in bills[0:i] and 5 in bills[0:i]:
                    bills.pop(bills[0:i].index(5))
                    bills.pop(bills[0:i].index(10))
                    i -= 2
                    
                elif bills[0:i].count(5) >= 3:
                    for x in range(3):
                        bills.pop(bills[0:i].index(5))
                        i -= 1
                        
                # if not, false
                else:
                    print("failed check on a 20")
                    return False
            #print("Cash Register: ", bills[0:i])
            i += 1
        
        # if the end has been reached, return True
        return True