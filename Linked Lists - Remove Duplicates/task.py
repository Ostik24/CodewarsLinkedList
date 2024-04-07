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

def remove_duplicates(head):
    probe = head
    if probe:
        set_uniquess = set()
        set_uniquess.add(probe.data)
        while probe.next:
            if probe.next.data not in set_uniquess:
                set_uniquess.add(probe.next.data)
                probe = probe.next
            else:
                probe.next = probe.next.next
    return head
