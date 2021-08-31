from typing import Optional

from .. import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        final_head = head

        current_element = head
        previous_element = None
        previous_previous_element = None

        index = 0
        while current_element.next is not None:
            index += 1
            previous_previous_element = previous_element
            previous_element = current_element
            current_element = current_element.next

            if index % 2 == 1:
                previous_element.next = current_element.next
                current_element.next = previous_element
                if previous_previous_element is None:
                    final_head = current_element
                else:
                    previous_previous_element.next = current_element
                current_element = previous_element

        return final_head


examples = [
    (
        (ListNode.from_list([1, 2, 3, 4]),),
        [2, 1, 4, 3],
    ),
    (
        (ListNode.from_list([1]),),
        [1],
    ),
    (
        (ListNode.from_list([]),),
        None,
    ),
    (
        (ListNode.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),),
        [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 13],
    ),
]
