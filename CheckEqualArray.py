from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        if Counter(a)==Counter(b):
             return True
        return False
