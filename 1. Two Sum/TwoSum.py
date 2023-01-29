'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]
    return 0


def main():
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))


if __name__ == '__main__':
    main()
