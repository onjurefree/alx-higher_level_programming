#!/usr/bin/python3
"""
This is class Node and its attributes
"""


class Node:

    """This are the attributes"""

    def __init__(self, data, next_node=None):

        """
        Attributes of class node
        Attribute:
            data: data
            next_node: next_node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    """This method sets data value"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    """This method returns next_node value"""
    @property
    def next_node(self):
        return self.__next_node

    """This method sets next_node"""
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """these are attributes of this class"""

    def __init__(self):

        """ private attribute"""

        self.head = None

    """This method sorts nodes values"""
    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        curr = self.head

        while curr.next_node is not None and value > curr.next_node.data:
            curr = curr.next_node

        new_node.next_node = curr.next_node
        curr.next_node = new_node

    """This method joins the nodes"""
    def __str__(self):
        node_values = []
        curr = self.head

        while curr is not None:
            node_values.append(str(curr.data))
            curr = curr.next_node

        return "\n".join(node_values)
