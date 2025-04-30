class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value
    
    def print_stack(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            if current.next:
                result += " -> "
            current = current.next
        print(f"Stack: {'<vacío>' if result == '' else result}")

mi_stack = Stack()

mi_stack.push(3)  
mi_stack.push(5)  
mi_stack.push(7)  

mi_stack.print_stack()  

mi_stack.pop()
mi_stack.pop()
mi_stack.pop()

mi_stack.print_stack()  
