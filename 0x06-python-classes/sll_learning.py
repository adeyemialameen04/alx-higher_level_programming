#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.data = data

        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next_node

    def inser_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        curr = self.head
        while curr.next_node:
            curr = curr.next_node

        curr.next_node = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for item in data_list:
            self.inser_at_end(item)

    def length(self):
        i = 0

        curr = self.head
        while curr:
            i += 1
            curr = curr.next_node
        return i

    def remove_at(self, idx):
        if idx < 0 or idx > self.length():
            print("Out of bounds")
            raise Exception("Invalid index")

        if idx == 0:
            self.head = self.head.next_code
            return

        count = 0
        curr = self.head
        while curr:
            if count == idx - 1:
                curr.next_node = curr.next_node.next_node
                break
            curr = curr.next_node
            count += 1

    def remove_by_val(self, data):
        if self.head is None:
            raise Exception("Empty list lol")

        curr = self.head
        while curr:
            if curr.data == data:
                curr.next_node = curr.next_node.next_node
            curr = curr.next_node


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(23)
    ll.insert_at_beginning(50)
    ll.inser_at_end(32)
    print("===========")
    ll.print()
    print("------------")
    ll.remove_by_val(23)
    print("==============")
    ll.print()
    print("-------------")
