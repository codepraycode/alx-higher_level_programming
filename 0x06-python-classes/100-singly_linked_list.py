#!/usr/bin/python3
"""SingleList and Node of a singly linked list"""


class Node(object):
    """A Node class"""

    def __init__(self, data, next_node=None):
        """Initialize Node class"""

        # Validate and set the initialization parameter
        self.__set_data(data)
        self.__set_next_node(next_node)

    def __set_data(self, value):
        """Validate and update node data"""
        #: str: Default error message
        msg = "data must be an integer"

        # Validate is value is int
        if not isinstance(value, int):
            raise TypeError(msg)

        #: int: private class attribute
        self.__data = value

    def __set_next_node(self, node):
        """Validate and update next_node data"""
        #: str: Default error message
        msg = "next_node must be a Node object"

        # Validate node is an instance of Node
        if node and not isinstance(node, self):
            raise TypeError(msg)

        #: next_node: private class attribute
        self.__next_node = node

    @property
    def data(self):
        """int: node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of node

        Args:
            value(int): value to set as node's data.

        Raises:
            TypeError: if `value` is not an integer.
        """
        self.__set_data(value)

    @property
    def next_node(self):
        """Node: node data"""
        return self.__next_node

    @data.setter
    def next_node(self, node):
        """Set the next_node of node instance

        Args:
            node(node): Next node to set node's next_node.

        Raises:
            TypeError: if `next_node` is not an instance of Node.
        """
        self.__next_node(node)

    def __str__(self):
        """String representation of Node instance
        Returns:
            str: The node's data
        """

        return str(self.__data)


class SinglyLinkedList(object):
    """A SinglyLinkedList class"""

    def __init__(self):
        """Initialize Node class"""
        self.__head = None

    def __update_singly_list(self, value, head=None):
        """Update the list by inserting node and sorting nodes"""

        # If no node, insert the new node at the very end.
        if not head:
            head = Node(value)
            return
        # If the next node data is greater than the new node value
        # replace the current node with the new node
        # set the current node to the next_node of the new node
        if value < head.data:
            node = Node(value)
            node.next_node = head
            head = node
            return
        # Otherwise,
        # continue the recursion with the next_node of the current head
        return self.__update_singly_list(value, head.next_node)

    def __compile_singly_list(self, head, compilation=[]):
        """Recursively compile the list data and return
        Returns:
            str: A compilation of the instance nodes data
        """
        if not head:
            return compilation

        compilation.append(str(head))
        print(f"Head: {head}")
        print(compilation)
        return self.__compile_singly_list(head.next_node, compilation)

    def sorted_insert(self, value):
        """Insert a new node with `value` as data into list
        The list is inserted in an increasing sorted order.

        Args:
            value(int): Value of node to be inserted
        """

        # Recursively update list
        return self.__update_singly_list(value, self.__head)

    def __str__(self):
        """Print the entire SinglyLinkedList
        Print the entire instance node to stdout
        """
        #: list of str: list of node numbers
        compilation = self.__compile_singly_list(self.__head)
        return "\n".join(compilation)

