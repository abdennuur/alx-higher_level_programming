#!/usr/bin/python3

"""Define the classes for  singly-linked list"""


class Node:
    """Represent a node in singly-linked list"""

    def __init__(self, data, next_node=None):
        """the Initialize new Node

        Args:
            data (int): The data of new Node
            next_node (Node): next node of  new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get set the next_node of Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """to Represent singly-linked list"""

    def __init__(self):
        """to Initalize new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node to SinglyLinkedList

        node is inserted into the list at correct
        ordered numerical position

        Args:
            value (Node): new Node to insert
        """
        nw = Node(value)
        if self.__head is None:
            nw.next_node = None
            self.__head = nw
        elif self.__head.data > value:
            nw.next_node = self.__head
            self.__head = nw
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            nw.next_node = temp.next_node
            temp.next_node = nw

    def __str__(self):
        """Define print() representation of SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
