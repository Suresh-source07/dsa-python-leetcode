"""
Problem: Contains Duplicate (LeetCode 217)
Approach: Set comparison
Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
