#!/usr/bin/python3
"""
A module for sll.
"""


class Node:
    """
    Defines a Node.

    Attributes:
        __data (int): The data of the Node.
        __next_node (Node): The next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialization of a node.
        Args:
            data(int): The data.
            next_node(Node): A node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Gets the data
        Returns:
            The data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data.
        Args:
            value (int): the data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Gets the property of the nxt node.
        Returns:
            The nxt node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the nextnode.
        Args:
            value (int): Node to be setted.
        Returns:
            Mothing.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.
    """
    def __init__(self):
        """
        Initialization.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a value in a linked list in a sorted order.
        Args:
            value (int): The value to be inserted
        Returns:
            Nothing.
        """
        if self.__head is None or self.__head.data >= value:
            node = Node(value, self.__head)
            self.__head = node
            return

        curr = self.__head
        while curr.next_node:
            if curr.next_node.data >= value:
                break
            curr = curr.next_node

        node = Node(value)
        node.next_node = curr.next_node
        curr.next_node = node

    def __str__(self):
        """
        Prints the linked list.
        Returns:
            The concatenated data of the list.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
