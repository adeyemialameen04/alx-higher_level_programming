#!/usr/bin/python3
Node = __import__('100-singly_linked_list').Node

n1 = Node(3)
print(n1.data)

n2 = Node(-5)
print(n2.data)

n3 = Node(4)
n3.next_node = n2
print(n3.next_node.data)

try:
    n4 = Node("4")
except Exception as e:
    print(e)

try:
    n2.next_node = "Node"
except Exception as e:
    print(e)
