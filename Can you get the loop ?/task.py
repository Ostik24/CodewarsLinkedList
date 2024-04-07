def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next
    return count