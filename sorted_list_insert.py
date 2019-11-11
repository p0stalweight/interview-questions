#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    insert_node = DoublyLinkedListNode(data)
    cur = head

    # Find the location that the node needs to be inserted to
    if cur.data > insert_node.data:
       insert_node.next = cur
       cur.prev = insert_node
       return insert_node

    while cur.data < insert_node.data and cur.next != None:
        # iterate through until node data is ahead
        cur = cur.next

    if cur.data > insert_node.data or cur.next != None:
        prev = cur.prev
        prev.next = insert_node
        insert_node.prev = prev
        insert_node.next = cur
        cur.prev = insert_node
        return head
    else:
        cur.next = insert_node
        insert_node.prev = cur
        return head


    


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
