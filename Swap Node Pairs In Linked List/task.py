class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head and head.next:
        prevs = None
        probe = head

        while probe and probe.next:
            temp = probe.next
            probe.next = temp.next
            temp.next = probe

            if prevs:
                prevs.next = temp
            else:
                head = temp
            prevs = probe
            probe = probe.next
    return head
