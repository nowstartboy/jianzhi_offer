'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate2(self, numbers, duplication):
        # write code here
        collect = {}
        for num in numbers:
            if num not in collect:
                collect[num] = 1
            else:
                duplication[0] = num
                return True
        return False

    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i] !error 深层嵌套不能直接这样赋值
                tmp=numbers[i]
                numbers[i]=numbers[tmp]
                numbers[tmp]=tmp
        return False

if __name__=='__main__':
    solve=Solution()
    duplication=[-1]
    numbers=[2,3,1,0,2,5,3]
    print  (solve.duplicate(numbers,duplication))