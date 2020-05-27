
def solution(nums):
   numsDict = set(nums)
   # print(numsDict)

   for n in range(1,nums[-1] + 1):
      if n not in numsDict:
         return n
   
   return nums[-1] + 1



if __name__ == "__main__":
   print(solution([1,2,3,4,6,7,8,9,10,11,12]))
   
   print(solution([1,2,3,4,5,6,7,8,9,10,11,12]))