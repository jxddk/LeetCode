from typing import Optional

from .. import ListNode, random_list


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        head = None
        latest_node = head

        while not (l1 is None and l2 is None):
            if l1 is None:
                source_node = 2
            elif l2 is None:
                source_node = 1
            elif l1.val < l2.val:
                source_node = 1
            else:
                source_node = 2

            if source_node == 1:
                source_value = l1.val
                l1 = l1.next
            else:
                source_value = l2.val
                l2 = l2.next

            new_node = ListNode(source_value)
            if head is None:
                head = new_node
                latest_node = head
            else:
                latest_node.next = new_node
                latest_node = new_node

        return head


examples = [
    (
        (ListNode.from_list([1, 2, 4]), ListNode.from_list([1, 3, 4])),
        [1, 1, 2, 3, 4, 4],
    ),
    (
        (ListNode.from_list([]), ListNode.from_list([])),
        None,
    ),
    (
        (ListNode.from_list([]), ListNode.from_list([0])),
        [0],
    ),
]

for _ in range(256):
    random_list_a = random_list(-100, 100, 0, 50, "a")
    random_list_b = random_list(-100, 100, 0, 50, "b")
    examples.append(
        (
            (ListNode.from_list(random_list_a), ListNode.from_list(random_list_b)),
            sorted(random_list_a + random_list_b),
        )
    )
