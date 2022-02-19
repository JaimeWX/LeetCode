class ListNode:
    def __init__(self,val=0):
        self.val = val
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            print(total%10)
            remainder = total//10
            print(remainder)

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder : curr.next = ListNode(remainder)
        return result.next

l = LinkList()
data1 = [2,4,3]
data2 = [5,6,4]
l1 = l.initList(data1)
l2 = l.initList(data2)
ans = Solution()
ans.addTwoNumbers(l1,l2)
