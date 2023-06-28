#!/usr/bin/python3
class Node:
    """Type class node"""
    def __init__(self, data, next_node=None):
        """Init the the node class
        Args:
        param1: data of the node
        param2: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data of the node"""
        return (self.__data)

    @property
    def next_node(self):
        """get the next node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Type class singly linked list"""
    def __init__(self):
        """Init the singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert the node sorted
        Args:
        param1: Value of the node
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            while (temp_node.next_node is not None and
                   temp_node.next_node.data < value):
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    def __str__(self):
        """Convert the object into a string"""
        values = []
        temp_node = self.__head
        while temp_node is not None:
            values.append(str(temp_node.data))
            temp_node = temp_node.next_node
        return ('\n'.join(values))
