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
    print("") # this print is added to make end work in the above print
    
def reverseALinkedList():
    head = createALinkedList()
    print("original linked list - ")
    printLinkedList(head)
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
    
if __name__ == "__main__":
    reverseALinkedList()
