def linked_list_from_string(s):
    lst = s.split(" -> ")
    lst_copied = lst.copy()
    head = None
    count = len(lst) - 1
    while lst_copied:
        if lst[count] != "None":
            head = Node(int(lst[count]), head)
        count -= 1
        lst_copied = lst_copied[1:]
    return head
