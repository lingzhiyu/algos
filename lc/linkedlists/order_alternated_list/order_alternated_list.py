"""
Given a linked list where every odd element is in ascending order
whilst every even element is in descending order.

Sort the linked list using an in-place algorithm.

xs = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val


def construct_ll_from_list(xs):
    dummy = curr = Node(0)
    for i in xs:
        curr.next = Node(i)
        curr = curr.next
    return dummy.next


def get_ll_as_list(head):
    """Convert LinkedList to a list.

    This is to make use of python's list equality.
    """
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def solve(head):
    if not head or not head.next:
        return head

    odd = fst = head
    even = snd = head.next
    while snd:
        fst.next = snd.next
        fst = snd
        snd = snd.next

    prev, curr = None, even
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    even = prev

    dummy = curr = Node(0)
    while odd and even:
        if odd.val <= even.val:
            curr.next = odd
            odd = odd.next
        else:
            curr.next = even
            even = even.next
        curr = curr.next
    rem = odd or even
    curr.next = rem
    return dummy.next
