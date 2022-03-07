# 总结：
#   队列：先进先出意味着pop(deque模拟为popleft())最左端的元素(队头元素)
#   栈：先进后出意味着pop最右端的元素
#   list的pop()正常pop()最右端的元素

from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while(len(self.queue1)>1):
            self.queue2.append(self.queue1.popleft())
        stackTail = self.queue1.popleft()
        while(len(self.queue2)>0):
            self.queue1.append(self.queue2.popleft())
        return stackTail

    def top(self) -> int:
        indexMax = len(self.queue1) - 1
        return self.queue1[indexMax]

    def empty(self) -> bool:
        if(len(self.queue1) == 0):
            return True
        else:
            return False


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.top())
print(obj.empty())

