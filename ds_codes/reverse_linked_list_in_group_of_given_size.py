# Given a linked list of size N. The task is to reverse every k
# nodes(where k is an input to the function) in the linked list. 
# If the number of nodes is not a multiple of k then left-out
# nodes, in the end, should be considered as a group and must be
# reversed.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def createALinkedList():
    print("input linked list values separated by space")
    linkedListValues = list(map(int, input().split()))
    head = None
    current = None
    for values in linkedListValues:
        node = Node(values)
        if(head):
            current = head
            while(current.next):
                current = current.next
            current.next = node
        else:
            head = node
    return head
    
def printLinkedList(head):
    current = head
    while(current):
        print(current.data, end=" ")
        current = current.next
    print("") #this print is added to make 'end' work in the above print

def traverseToEnd(head):
    while(head.next):
        head = head.next
    return head
    
def connectLinkedLists(listOfLinkedLists):
    tail = traverseToEnd(listOfLinkedLists[0])
    for index in range(1, len(listOfLinkedLists)):
        tail.next = listOfLinkedLists[index]
        tail = traverseToEnd(listOfLinkedLists[index])
    return listOfLinkedLists[0]
    
def chunkList(k):
    print(k)
    head = createALinkedList()
    print(head)
    current = head
    listOfLinkedLists = []
    while(current):
        present_head = current
        for counter in range(k-1):
            if current.next:
                current = current.next
                next_node = current
            else:
                break
        next_head = current.next
        current.next = None
        printLinkedList(present_head)
        new_head = reverseALinkedList(present_head)
        listOfLinkedLists.append(new_head)
        current = next_head
    values = connectLinkedLists(listOfLinkedLists)
    printLinkedList(values)
    
def reverseALinkedList(head):
    current = head
    while(current):
        current_next = current.next
        if current == head:
            current.next = None
        else:
            current.next = prev
        prev = current
        current = current_next
    head = prev
    print("reversed linked list - ")
    printLinkedList(head)
    return head
    
if __name__ == "__main__":
    k = int(input())
    chunkList(k)
