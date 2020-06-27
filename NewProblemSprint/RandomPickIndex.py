
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