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

def reverse(head):
    probe = head
    if probe:
        new = Node(probe.data)
        while probe.next:
            probe = probe.next
            r = Node(probe.data)
            r.next = new
            new = r
        return new
    return None
