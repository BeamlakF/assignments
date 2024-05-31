class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtPos(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        count = 1

        while current and count != position:
            prev = current
            current = current.next
            count += 1

        if count != position:
            print(" out of bounds position")
            return
        prev.next = new_node
        new_node.next = current
    def deleteAtPosition(self, position):
        if self.head == None:  
            print(" Empty List ")
            return
        if position == 1:  
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 1
        while current and count != position:
            prev = current
            current = current.next
            count += 1

        if not current :  
            print("Position out of bounds")
            return

        prev.next = current.next
    def deleteAfterNode(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("Given node is None")
            return

        node_to_delete = prev_node.next
        prev_node.next = node_to_delete.next
    def searchNode(self, value):
        current = self.head
        position = 1
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
            return -1 
class Stack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top is None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.top.data
stack= Stack()
# Create a LinkedList instance
linked_list = LinkedList()

# Insert nodes at various positions
linked_list.insertAtPos(5, 1)
linked_list.insertAtPos(7, 2)
linked_list.insertAtPos(10, 3)


# Delete a node at position 3
linked_list.deleteAtPosition(3)


# Search for a node with value 8
position = linked_list.searchNode(8)
if position != -1:
    print(f"Node with value 8 found at position {position}")
else:
    print("Node with value 8 not found")

# Create a Stack instance
stack = Stack()

# Push elements into the stack
stack.push(3)
stack.push(4)
stack.push(5)

# Display the stack
print("Stack:")
while not stack.isEmpty():
    print(stack.pop())
