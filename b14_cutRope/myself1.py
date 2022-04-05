class Solution:
    def cuttingRope(self, n: int) -> int:
        # 解决绳子长度为2或3时的情况
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        # 解决绳子长度大于3时的情况(自下往上求解问题)
        products = [0 for i in range(n+1)]
        m = 0
        while m < 4:
            products[m] = m
            m += 1
        for i in range(n+1):
            if i > 3:
                j =1
                max_product = 0
                while j <= i/2:
                    products[i] = products[j] * products[i-j]
                    if max_product < products[i]:
                        max_product = products[i]
                    j += 1
                products[i] = max_product
        ans = products[n]
        return ans

n = 10
anss = Solution()
print(anss.cuttingRope(n))