import random

# second time

def sortArray(nums):
        # quicksort
        random.shuffle(nums)
        quickSort( nums, 0, len(nums)-1)
        return nums
def quickSort( nums, left, right):
    # if the length of the list given is 0 then return
    if right - left <= 0:
        return

    # place the first index of this partition
    partIndex = place(nums, left, right)

    # using the index returned from the placement, partition the halves further
    quickSort(nums, left, partIndex-1) # left
    quickSort(nums, partIndex+1, right) # right

def place( nums, left, right):
    # print("Before swap\n",nums, "left", left, "right", right)
    placeVal = nums[left]
    swapIndex = left + 1
    i = left

    # find the swap index and certify that all vals less than the value being swapped are
    # left of the swap index
    while i <= right:
        if nums[i] < placeVal:
            nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
            swapIndex += 1
        i += 1

    # Perform the swap
    nums[left], nums[swapIndex-1] = nums[swapIndex-1], nums[left]

    # print("Placed ",placeVal ," at ", swapIndex)
    # print(nums)

    return swapIndex - 1

if __name__ == '__main__':
    arr = [10,9,8,7,6,5,8,7,4,110,4,3,2,1,14,13]
    sortArray(arr)
    print(arr)

    arr = [10,9,8,7,6,5,4,3,2,1]