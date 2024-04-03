def stringify(node):
    stringa = ""
    if not node:
        stringa += "None"
    else:
        probe = node
        while probe:
            if probe.next:
                stringa = stringa + str(probe.data) + " -> "
            else:
                stringa += str(probe.data)
            probe = probe.next
        stringa += " -> None"
    return stringa
