class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        stringa = ""
        if not self:
            stringa += "None"
        else:
            probe = self
            while probe:
                if probe.next:
                    stringa = stringa + str(probe.data) + " -> "
                else:
                    stringa += str(probe.data)
                probe = probe.next
            stringa += " -> None"
        return stringa

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    print(head)
    probe = head
    if probe and probe.next:
        lst = []
        while probe:
            lst.append(probe.data)
            probe = probe.next
        lst = lst[::-1]
        first, second = None, None
        for ind, data in enumerate(lst):
            r = Node(data)
            if ind%2:
                if len(lst) %2:
                    r.next = second
                    second = r
                else:
                    r.next = first
                    first = r
            else:
                if len(lst) %2:
                    r.next = first
                    first = r
                else:
                    r.next  = second
                    second = r
        return Context(first, second)
    raise ValueError
