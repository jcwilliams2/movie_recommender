from node import *

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_head_node(self, value):
        new_head = Node(value)
        if self.head_node is not None:
            new_head.set_next_node(self.head_node)
        self.head_node = new_head

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node is not None:
                string_list += str(current_node.get_value())
            if current_node.get_next_node() is not None:
                string_list += '\n'
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, target):
        current_node = self.get_head_node()
        if current_node == target:
            self.head_node = self.head_node.get_next_node()
            return current_node
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == target:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def get_node_by_value(self, target):
        current_node = self.get_head_node()
        if current_node.get_value() == target:
            return current_node
        else:
            while current_node is not None:
                next_node = current_node.get_next_node()
                if next_node.get_value() == target:
                    return next_node
                current_node = next_node