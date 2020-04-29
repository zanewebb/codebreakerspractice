
# one pass in place solution

# pretty smart, not mine. 
# track 3 pointers, they indicate where the next value of each bucket should go
# the white pointer is your decision maker
   # if you find a 0, swap the values at the red and white pointers, move the red AND white pointers outwards
   # if you find a 1, move just the white pointer outwards
   # if you find a 2, swap the values at white and blue, move the blue pointer inwards
def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


# first try, nice
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # not space efficient but here we go
        
        # build "map" with 3 buckets for  0, 1 and 2
        # values will be empty lists
        mapColors = {
            0: [],
            1: [],
            2: []
        }
        
        # iterate over nums, copy each num into its respective bucket
        for n in nums:
            mapColors[n].append(n)
        # iterate over each list from 0 to 1 to 2 to overwrite what was given in the input array
        ind = 0
        for n in mapColors[0]:
            nums[ind] = n
            ind += 1
        for n in mapColors[1]:
            nums[ind] = n
            ind += 1
        for n in mapColors[2]:
            nums[ind] = n
            ind += 1