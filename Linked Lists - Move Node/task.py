class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source and dest:
        head = source.next
        probe = Node(source.data)
        probe.next = dest
        return Context(head, probe)
    raise ValueError