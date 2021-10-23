# remove duplicates from an unsorted list in linked list
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
    
def removeDuplicatesFromUnsortedLinkedList(head):
    current = head
    values = [current.data]
    prev = head
    while(current.next):
        if current.data in values:
            prev.next = current.next
            current = current.next
        else:
            values.append(current.data)
            prev = current
            current = current.next
        
    printALinkedList(head)
head = createALinkedList()
removeDuplicatesFromUnsortedLinkedList(head)
