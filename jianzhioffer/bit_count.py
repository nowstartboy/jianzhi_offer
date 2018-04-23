class Solution:
    def NumberOf2(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return sum([n >> i & 1 for i in range(32)])

    def NumberOf1(self, n):
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count

if __name__=='__main__':
    solve=Solution()
    print (solve.NumberOf1(-8))