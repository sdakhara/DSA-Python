class Node:
    def addData(self, next=None):
        # self.data = 0
        self.data = int(input("add: "))
        self.next = next


class Sll(Node):
    linkedList = []
    def addNode(self):
        c = Node()
        try:
            if self.linkedList[0] == None:
                pass
            else:
                c.addData()
                self.linkedList[-1].next = c
                self.linkedList.append(c)
                print(f"data: {self.linkedList[-1].data} is added")
        except IndexError:
            c.addData()
            self.linkedList.append(c)
            print(f"data: {self.linkedList[-1].data} is added")

    def deleteNode(self):
        valtofind = int(input("Enter Value to Delete a Node: "))
        for index, value in enumerate(self.linkedList):
            if valtofind == value.data:
                self.linkedList.pop(index)
                self.linkedList[index-1].next = self.linkedList[index]
                self.printAllNode()

    def printAllNode(self):
        print("####################################################################################")
        for node in self.linkedList:
            print(" data "+str(node.data), end=" -")
            print(" current node "+str(node), end=" -")
            print(" node next "+str(node.next))

    def travesThroughLinkedList(self):
        iterableList = self.linkedList.__iter__()
        for i in self.linkedList:
            print(next(iterableList).data)


sll = Sll()
sll.addNode()
sll.addNode()
sll.addNode()
sll.addNode()
sll.addNode()
sll.deleteNode()
