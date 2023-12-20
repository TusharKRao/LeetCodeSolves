def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    size = 1
    root = head
    while root.next != None:
        root = root.next
        size += 1
    pos = size - n
    counter = 1
    flag = 0
    root = head
    while root.next != None:
        if counter == pos:
            root.next = root.next.next
            flag = 1
            break
        root = root.next
        counter += 1
    if flag == 1:
        return head
    else:
        head = head.next
        return head