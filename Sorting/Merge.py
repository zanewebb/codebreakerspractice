

class Solution:


    #executed the solution i found, was not as clean as i had seen it before 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # track ends of each array (m-1, n-1)
        
        # while theyre both above zero
        while m > 0 or n > 0:
            # if one or the other are zero, that means that the rest of the remaining
            # from the other array must be less than the bottom of the other array
            if m == 0: 
                nums1[n-1] = nums2[n-1]
                n -= 1
            elif n == 0:
                break
            # check if the one in nums1 is > the one in nums2
            elif nums1[m-1] >= nums2[n-1]:
                # whichever is greater, place that in m + n -1, then decrement n or m
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            elif nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

   # found a slick solution (not mine) the trick was to fill in from right to left using m and n. I was caught up on filling left to right 

   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1


   # annnnd turns out I HAVE to do it in place, this solution wont submit because i just reassigned nums1 to temp
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = n2 = 0
        
        temp = []
        
        while n1 < m or n2 < n:
            if n1 >= m: 
                temp.append(nums2[n2])
                n2 += 1
            elif n2 >= n: 
                temp.append(nums1[n1])
                n1 += 1
            else:
                if nums1[n1] < nums2[n2]:
                    temp.append(nums1[n1])
                    n1 += 1
                else:
                    temp.append(nums2[n2])
                    n2 += 1
        print(temp)
        nums1 = temp

   # cant figure out how to do it in O(m+n) time and O(1) space so im going to build a O(m+n) and O(m+n) solution
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = n2 = 0
        
        # [1,2,2,3,[0],0] n1 = 4
        # [2,[5],6] n2 = 1
        
        # [1,2,[3],0,0,0]
        # [[2],5,6]
        
        # [[1],2,3,0,0,0]
        # [[2],5,6]
        
        while n2 < len(nums2):
            # if the index is greater than the starting nums1 size then 
            # we've already compared everything within the original nums1, so just fill in the rest
            if n1 >= m:
                nums1[n1] = nums2[n2]
                n1 += 1
                n2 += 1
            elif nums2[n2] < nums1[n1] :
                nums1[n1], nums2[n2] = nums2[n2], nums1[n1]
                n1 += 1               
            else:
                