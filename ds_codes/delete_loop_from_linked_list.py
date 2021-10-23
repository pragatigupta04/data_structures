# Detect a loop in linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def createALinkedList():
    print("Enter the list of values - ")
    listValues = list(map(int, input().split()))
    current = Node(listValues[0], None)
    head = current
    for i in range(1, len(listValues)):
        temp = Node(listValues[i], None)
        current.next = temp
        current = current.next
    printALinkedList(head)
    return head
    
def printALinkedList(head):
    while(head):
        print(head.data, end=" ")
        head = head.next
    print("")
    
def makeALoop(head, k):
    if k == -1 or k == 0:
        return head
    current = head
    for i in range(k-1):
        current = current.next
    temp = current
    printALinkedList(current)
    while(current.next):
        current = current.next
    current.next = temp
    print(current.next.data)
    return head
    
def detectLoopLocationAndRemoveTheLoop(head):
    listOfNodes = [head]
    current = head
    while(current.next):
        prev = current
        current = current.next
        if current in listOfNodes:
            prev.next = None
            printALinkedList(head)
            print("new loop location - ")
            print(detectLoopLocationAndRemoveTheLoop(head))
            return listOfNodes.index(current) +  1
        listOfNodes.append(current)
    return 0
    
    
head = createALinkedList()
print("Enter loop position")
k = int(input())
head = makeALoop(head, k)
position = detectLoopLocationAndRemoveTheLoop(head)
if position != 0:
    print("Loop is present at position = ", position)
else:
    print("Loop is not present")
