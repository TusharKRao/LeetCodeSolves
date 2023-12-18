def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    num1 = 0
    num2 = 0
    i = 0
    while True:
        num1 = num1 + l1.val*pow(10,i)
        if l1.next == None:
            i = 0
            break
        l1 = l1.next
        i += 1
    while True:
        num2 = num2 + l2.val*pow(10,i)
        if l2.next == None:
            i = 0
            break
        l2 = l2.next
        i += 1
    N = num1 + num2
    L =  ListNode(N%10)
    root = L
    N = N / 10
    while N != 0:
        L.next = ListNode(N%10)
        L = L.next
        N = N/10
    return root