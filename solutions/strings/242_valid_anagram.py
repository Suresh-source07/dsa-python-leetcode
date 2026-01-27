         
"""
Problem: Valid Anagram (LeetCode 242)
Approach: Frequency Hash Map
Time Complexity: O(n)
Space Complexity: O(1)  (since alphabet size is fixed)
"""

def is_anagram(s, t):
    hashmap = {}
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in hashmap:
            hashmap[s[i]] += 1
        else: 
            hashmap[s[i]] = 1

    for i in range(len(t)):
        if t[i] in hashmap:
            hashmap[t[i]] -= 1
        else: 
            return False
    
    for i in hashmap.values(): 
        if i != 0: 
            return False 
    return True


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
