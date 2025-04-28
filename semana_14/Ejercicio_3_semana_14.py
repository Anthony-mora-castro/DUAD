class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):

        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_recursive(current_node.right_child, value)
    
    def print_tree(self):

        if self.root is not None:
            self._print_in_order(self.root)
        else:
            print("El árbol está vacío")
    
    def _print_in_order(self, current_node):

        if current_node is not None:
            self._print_in_order(current_node.left_child)
            print(str(current_node.value), end=' ')
            self._print_in_order(current_node.right_child)
    
    def print_tree_structure(self):

        if self.root is not None:
            self._print_structure(self.root, 0)
        else:
            print("El árbol está vacío")
    
    def _print_structure(self, current_node, indent_level):

        if current_node is not None:
            self._print_structure(current_node.right_child, indent_level + 1)
            print('    ' * indent_level + str(current_node.value))
            self._print_structure(current_node.left_child, indent_level + 1)

tree = BinaryTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Valores del árbol en orden:")
tree.print_tree()  

print("\nEstructura del árbol:")
tree.print_tree_structure()