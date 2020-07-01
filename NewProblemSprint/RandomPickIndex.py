
# second
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                res = i if random.randint(1, count) == 1 else res

        return res



# had a solution, went wrong somehow
# this one is from the discussion boards
# "reservoir sampling", pretty neat
def __init__(self, nums):
    self.nums = nums
    
def pick(self, target):
    res = None
    count = 0
    for i, x in enumerate(self.nums):
        if x == target:
            count += 1
            chance = random.randint(1, count)
            if chance == count:
                res = i
    return res