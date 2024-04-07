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
