"""
Problem: Two Sum (LeetCode 1)
Approach: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
