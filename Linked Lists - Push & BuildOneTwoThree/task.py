class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    r = Node(data)
    r.next = head
    return r

def build_one_two_three():
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
