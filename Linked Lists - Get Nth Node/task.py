class Node(object):
    """Node class for reference"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node:
        probe = node
        count = 0
        while probe and count != index:
            probe = probe.next
            count += 1
        if probe:
            return probe
    raise ValueError
