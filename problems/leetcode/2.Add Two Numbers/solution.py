from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def sum_nodes(n1: ListNode, n2: ListNode, carry=0) -> ListNode:
        n3 = ListNode()
        if not n1:
            n1 = ListNode()
        if not n2:
            n2 = ListNode()

        total = n1.val + n2.val + carry
        if total > 9:
            total -= 10
            carry = 1
        else:
            carry = 0
        n3.val = total
        if n1.next or n2.next or carry != 0:
            n3.next = sum_nodes(n1.next, n2.next, carry=carry)
        return n3

    return sum_nodes(l1, l2)


def solution2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    current_l1 = l1
    current_l2 = l2
    carry = 0
    head = ListNode()
    current_node = head
    while (
        carry != 0
        or current_l1.val != 0
        or current_l2.val != 0
        or current_l1.next
        or current_l2.next
    ):
        total = current_l1.val + current_l2.val + carry
        if total > 9:
            total -= 10
            carry = 1
        else:
            carry = 0
        current_node.val = total
        current_l1 = current_l1.next or ListNode()
        current_l2 = current_l2.next or ListNode()
        if (
            current_l1.val
            or current_l2.val
            or carry != 0
            or current_l1.next
            or current_l2.next
        ):
            current_node.next = ListNode()
            current_node = current_node.next
    return head


# [1,6,0,3,3,6,7,2,0,1]
# [6,3,0,8,9,6,6,9,6,1]
if __name__ == "__main__":
    n1 = ListNode(1, ListNode(6, ListNode(0, ListNode(3))))
    n2 = ListNode(6, ListNode(3, ListNode(0, ListNode(8))))
    r = solution(n1, n2)
    a = r
    while a:
        print(a.val, end=" ")
        a = a.next
