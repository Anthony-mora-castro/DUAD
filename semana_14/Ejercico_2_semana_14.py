class DequeNode:
    def __init__(self, value):
        self.stored_value = value
        self.next_node = None
        self.previous_node = None

class DoubleEndedQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.element_count = 0
    
    def add_to_front(self, value):

        new_node = DequeNode(value)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            new_node.next_node = self.front_node
            self.front_node.previous_node = new_node
            self.front_node = new_node
        self.element_count += 1
    
    def add_to_rear(self, value):
       
        new_node = DequeNode(value)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            new_node.previous_node = self.rear_node
            self.rear_node.next_node = new_node
            self.rear_node = new_node
        self.element_count += 1
    
    def remove_from_front(self):
        
        if self.is_empty():
            return None
        
        removed_node = self.front_node
        
        if self.front_node == self.rear_node:  
            self.front_node = self.rear_node = None
        else:
            self.front_node = self.front_node.next_node
            self.front_node.previous_node = None
        
        self.element_count -= 1
        return removed_node.stored_value
    
    def remove_from_rear(self):

        if self.is_empty():
            return None
        
        removed_node = self.rear_node
        
        if self.front_node == self.rear_node:  
            self.front_node = self.rear_node = None
        else:
            self.rear_node = self.rear_node.previous_node
            self.rear_node.next_node = None
        
        self.element_count -= 1
        return removed_node.stored_value
    
    def is_empty(self):

        return self.front_node is None
    
    def print_deque(self):

        if self.is_empty():
            print("Deque: <empty>")
            return None
        
        current_node = self.front_node
        values = []
        
        while current_node:
            values.append(str(current_node.stored_value))
            current_node = current_node.next_node
        
        deque_string = " - ".join(values)
        print(f"Deque: {deque_string}")
        return deque_string
    
    def get_size(self):
        return self.element_count
    
my_deque = DoubleEndedQueue()

my_deque.add_to_rear(10)
my_deque.add_to_front(5)
my_deque.add_to_rear(20)

my_deque.print_deque()  

front_value = my_deque.remove_from_front()
print(f"Removed from front: {front_value}")  

rear_value = my_deque.remove_from_rear()
print(f"Removed from rear: {rear_value}")  

my_deque.print_deque() 
print(f"Current size: {my_deque.get_size()}")  