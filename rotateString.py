class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)==len(B):
            if B in A+A:
                return True
        return False
