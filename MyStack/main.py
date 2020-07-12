# 题目1: 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。
class MyStack:

    def __init__(self, limit=10):
        self.data = []
        self.limit = limit  # 栈容量极限

    def r_push(self, t):
        if len(self.data) >= self.limit:
            raise IndexError('Stack Overflow Error')
            pass
        self.data.append(t)

    def l_push(self, t):
        if len(self.data) >= self.limit:
            print('Stack Overflow Error')
            pass
        self.data.insert(0, t)

    def r_pop(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError('pop from an empty stack')

    def l_pop(self):
        if self.data:
            return self.data.pop(0)
        else:
            raise IndexError('pop from an empty stack')
