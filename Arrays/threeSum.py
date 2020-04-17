# threeSum.py

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