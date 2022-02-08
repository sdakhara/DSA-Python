class Node:
    last = None
    data = None
    next = None

    def addData(self, last=None, next=None):
        self.last = None
        self.data = int(input("Enter the Data of node: "))
        self.next = None


class Dll:
    linkedlist = []

    def addNode(self):
        NewNode = Node()
        NewNode.addData()
        try:
            if self.linkedlist[0] == 'wrong':
                pass
            else:
                NewNode.last = self.linkedlist[-1]
                self.linkedlist[-1].next = NewNode
                self.linkedlist.append(NewNode)
                print("Node Inserted")
        except IndexError:
            self.linkedlist.append(NewNode)
            print("Node Inserted")

    def printAllNode(self):
        print("###########################################")
        for index, value in enumerate(self.linkedlist):
            print("index ", index, end=" - ")
            print("last ", value.last, end=" - ")
            print("current ", value, end=" - ")
            print("data ", value.data, end=" - ")
            print("next", value.next)


dll = Dll()
dll.addNode()
dll.addNode()
dll.addNode()
dll.addNode()
dll.printAllNode()
