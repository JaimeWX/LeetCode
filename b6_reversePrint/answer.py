class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    # 创建一个头指针为空的链表
    # 使用头节点来表示整个列表
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = ListNode(data[0])
        if len(data) > 0:
            r = self.head
            p = self.head
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
        return r

    def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val)
            node = node.next

class Solution:

    def reversePrint_recursion(self,head):
        if head != None:
            if head.next != None:
                self.reversePrint_recursion(head.next)
            # 返回 当前list + 当前节点值
            return self.reversePrint_recursion(head.next) + [head.val]
        else:
            return []

    def reversePrint_stack(self,head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        return stack[::-1]

l = LinkList()
head = [1, 3, 2]
head1 = [3,9,4]
l1 = l.initList(head)
l2 = l.initList(head1)
ans = Solution()
print(ans.reversePrint_recursion(l1))
print(ans.reversePrint_stack(l2))