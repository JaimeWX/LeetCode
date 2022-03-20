# 使用字符串的replace函数

class Solution:
    def replaceSpace(self, s: str) -> str:
        for i in s:
            if i == ' ':
                s = s.replace(i,'%20')
        return s

s = "We are happy."
ans = Solution()
print(ans.replaceSpace(s))

