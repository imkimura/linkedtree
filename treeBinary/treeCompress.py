from node import Node

class TreeCompressed:
    def __init__(self):
        self.head = None

    def pushNode(self, elem):
        if self.head:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
    
    def printNode():
        print(head)
    
if __name__ == "__main__":
    TreeCompressed()
    