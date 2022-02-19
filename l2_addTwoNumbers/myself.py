# 解题思路：以[2,4,3]和[5,6,4]为例
# step1 反向得到数字342和465，然后得到它们的和807
# step2 用取余数%和整数除//拆分807分别为7，0，8, 然后以此顺序加入到一个空列表中得到[7,0,8]
# step3 用列表[7,0,8]构造一个单链表[7,0,8]

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
    def addTwoNUmbers(self,l1,l2):
        number1 = self.getNumber(l1)
        number2 = self.getNumber(l2)
        number = number1 + number2
        print(number1)
        print(number2)
        print(number)
        list = []
        if number == 0:
            list.append(0)
        else:
            while number > 0:
                list.append(number % 10)
                # // 为整数除
                number = number // 10
        ans = LinkList()
        ans.printlist(ans.initList(list))
        return ans

    def getNumber(self, singlyLinkedList):
        p = singlyLinkedList
        number = 0
        length = self.countLength(singlyLinkedList)
        pos = 0
        while p != None:
            if pos <= length:
                number += p.val * pow(10,pos)
                p = p.next
                pos += 1
        return number

    def countLength(self, singlyLinkedList):
        p = singlyLinkedList
        linkLength = 0
        while p != None:
            linkLength = linkLength + 1
            p = p.next
        return linkLength

l = LinkList()
data1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
data2 = [5,6,4]
l1 = l.initList(data1)
l2 = l.initList(data2)
ans = Solution()
print(ans.addTwoNUmbers(l1,l2))