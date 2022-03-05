# 难点在于if的判断条件
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
        return self.stack1



    def deleteHead(self) -> int:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return -1

        if len(self.stack2) == 0:
            while(len(self.stack1)>0):
                value = self.stack1.pop()
                self.stack2.append(value)
            # print("2="+str(self.stack2))

        if len(self.stack2) > 0:
            return self.stack2.pop()


# ["CQueue","deleteHead","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","appendTail","deleteHead","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","appendTail","deleteHead","appendTail","appendTail"]
# [[],[],[97],[],[],[],[],[15],[],[1],[43],[],[],[],[18],[],[],[],[],[36],[69],[21],[91],[],[],[22],[40],[],[],[],[81],[65],[],[77],[],[63],[96],[5],[],[],[35],[90],[],[],[],[],[77],[83],[],[],[52],[],[2],[66],[87],[90],[],[2],[],[],[33],[16],[72],[],[],[14],[78],[8],[],[],[],[],[3],[83],[],[],[13],[],[79],[44],[],[],[33],[],[55],[76],[12],[],[91],[24],[49],[47],[],[],[],[85],[],[69],[],[94],[52]]

obj = CQueue()
print(obj.deleteHead())
print(obj.appendTail(97))
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.appendTail(15))
print(obj.deleteHead())
print(obj.appendTail(1))
print(obj.appendTail(43))
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.appendTail(18))
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.appendTail(36))
print(obj.appendTail(69))
print(obj.appendTail(21))
print(obj.appendTail(91))
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.appendTail(22))
print(obj.appendTail(40))
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())




