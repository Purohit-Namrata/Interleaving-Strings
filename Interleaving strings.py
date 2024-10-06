class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
 
        if not s3:
            return False
 
        if s1 and s3[0]==s1[0]:
            return s.isInterleave(s1[1:], s2, s3[1:])
 
        if s2 and s3[0]==s2[0]:
            return s.isInterleave(s1, s2[1:], s3[1:])
 
        return False

s=Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Expected output: False
print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Expected output: False
print(s.isInterleave("", "", ""))  # Expected output: True