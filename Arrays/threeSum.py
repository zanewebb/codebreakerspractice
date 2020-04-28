# threeSum.py

# fifth time, finally remembered

def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # sort nums
        nums = sorted(nums)
        # create set
        ans = {}
        
        for i in range(0,len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                tempSum = nums[i] + nums[l] + nums[r]
                #print(tempSum)
                if tempSum < 0:
                    l += 1
                elif tempSum > 0:
                    r -= 1
                else:
                    #print("adding solution "+ str(nums[i]) + str(nums[l]) + str(nums[r]) )
                    ans[str(nums[i]) + str(nums[l]) + str(nums[r])] = [nums[i], nums[l], nums[r]]
                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
        
        #print(ans.values())
        return ans.values()

# fourth time

# really need to remember that there needs to be two sub loops within the sub while loop that allow the sub loop (for moving l and r) to exit its condition.
# if we dont have those loops to move the l and r until theyre different values, and move them one further, then it will keep trying to add the same answer infinitely

def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        # create set
        ans = {}
        
        # iterate over nums until i > 0
        i = 0
        while i < len(nums)-2 and nums[i] <= 0:
            # assign l and r to i + 1 and len(nums) - 1
            l, r = i+1, len(nums)-1
            
            # while l < r
            while l < r:
                # move l and r towards each other depending on sum of three positions
                # if the sum == 0 
                if nums[i] + nums[l] + nums[r] == 0:
                    # add the three values to the set
                    ans[str(nums[i]) + str(nums[l]) + str(nums[r])] = [nums[i], nums[l], nums[r]]
                    
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1 
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            
            i += 1
                
        # return answer set
        return ans.values()

# third time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        
        # track answer set
        ans = {}
        
        # iterate over the list until nums[i] > 0 or i >= len(nums)-2
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:
            # track left and right
            l, r = i+1, len(nums)-1
            
            # while l < r
            while l < r:
                # if the sum of values at i, l, and r is greater than 0
                if nums[i] + nums[l] + nums[r] > 0:
                    # decrement r
                    r -= 1
                
                # elif the sum of values at i, l, and r is less than 0
                elif nums[i] + nums[l] + nums[r] < 0:   
                    # increment l
                    l += 1
                    
                # else 
                else:
                    # add [i, l, r] to the set of answers
                    ans[str(nums[i])+str(nums[l])+str(nums[r])] = [nums[i], nums[l], nums[r]]

							# THIS IS THE CRITICAL PART 
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1                    
            # increment i
            i += 1
        
        return ans.values()


# second time, sloppy, needed help
def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        ans = {}
        
        # iterate over the nums
        for i in range(len(nums)-2):
            # if i is > 0, break
            if nums[i] > 0:
                break
            
            # two iterators, left(i) and right(len - 1)
            left = i+1
            right = len(nums) -1
            
            # while left is less than right
            while left < right:
                # if greater than 0, move right inwards
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                    
                # if less than 0, move left inwards
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                
                # store the sum if zero
                else:
                    if str(nums[i])+str(nums[left])+str(nums[right]) not in ans:
                        ans[str(nums[i])+str(nums[left])+str(nums[right])] = [nums[i], nums[left], nums[right]]
                        
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                        
                
        
        return ans.values()

# real solution
def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in xrange(length-2): #[8]
			if nums[i]>0: break #[7]
			if i>0 and nums[i]==nums[i-1]: continue #[1]

			l, r = i+1, length-1 #[2]
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: #[3]
					l+=1
				elif total>0: #[4]
					r-=1
				else: #[5]
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: #[6]
						l+=1
					while l<r and nums[r]==nums[r-1]: #[6]
						r-=1
					l+=1
					r-=1
		return res

# throwaway solution 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        nums = sorted(nums)
        # recursive search to find all possible (this could be very messy)
        return self.findTriples(nums, left, mid, right)
    
    def findTriples(self, nums: List[int], left: int, mid: int, right: int) -> List[List[int]]:
        
        # this wont work without checking the indicies to make sure they arent matching or out of bounds
        
        
        if nums[left] + nums[mid] + nums[right] == 0:
            return [[left,mid,right]]
        elif nums[left] + nums[mid] + nums[right] > 0:
            return findTriples(nums, left-1, mid, right) + findTriples(nums, left, mid-1, right) + findTriples(nums, left, mid, right-1)
        elif nums[left] + nums[mid] + nums[right] < 0:
            return findTriples(nums, left+1, mid, right) + findTriples(nums, left, mid+1, right) + findTriples(nums, left, mid, right+1)