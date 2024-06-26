class Node(object):
    def __init__(self, data):
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

def sorted_insert(head, data):
    probe = head
    count = 0
    if probe:
        if data < probe.data:
            r = Node(data)
            r.next = probe
            return r
        while probe and probe.data < data:
            probe = probe.next
            count += 1
        r = Node(data)
        r.next = probe
        count -= 1
        prob = head
        while count:
            count -= 1
            prob = prob.next
        prob.next = r
        return head
    r = Node(data)
    r.next = head
    return r
