class Node:
    def addData(self, next=None):
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
                # self.printAllNode()

    def addNewNode(self):
        c = Node()
        try:
            if self.linkedList[0] == None:
                pass
            else:
                c.addData()
                placeOfNewNode = int(input("Enter the node data before the new node: "))
                for index, value in enumerate(self.linkedList):
                    if value.data == placeOfNewNode:
                        self.linkedList[index].next = c
                        c.next = self.linkedList[index+1]
                        self.linkedList.insert(index+1, c)
                        # self.printAllNode()

        except IndexError:
            c.addData()
            print("linked list is empty pls enter new node")
            self.linkedList.append(c)
            print(f"data: {self.linkedList[-1].data} is added")

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
while True:
    print("###################################### SINGLY LINKED LIST #####################################################")
    print("1. add node to linked list")
    print("2. add new node in a middle of a linked list")
    print("3. delete a node")
    print("4. Show all node")
    print("5. Exit")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        sll.addNode()
    elif choice == 2:
        sll.addNewNode()
    elif choice == 3:
        sll.deleteNode()
    elif choice == 4:
        sll.printAllNode()
    elif choice == 5:
        break

