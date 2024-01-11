def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    ll = set()
    root = head
    if root is None:
        return root
    if root.next is not None:
        prev = root
        ll.add(prev.val)
        root = root.next
    else:
        return root

    while root:
        if root.val not in ll:
            ll.add(root.val)
            prev = prev.next
        else:
            prev.next = root.next
        root = root.next
    return head