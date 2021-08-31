from typing import List, Optional

from .. import ListNode, random_list


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        available_indexes = set([i for i in range(len(lists)) if lists[i] is not None])

        head = None
        latest_node = head

        while len(available_indexes) > 0:
            smallest_value = None
            chosen_index = None
            for index in available_indexes:
                if chosen_index is None:
                    chosen_index = index
                    smallest_value = lists[index].val
                    continue
                if lists[index].val < smallest_value:
                    chosen_index = index
                    smallest_value = lists[index].val

            new_node = ListNode(smallest_value)
            if head is None:
                head = new_node
                latest_node = head
            else:
                latest_node.next = new_node
                latest_node = latest_node.next

            lists[chosen_index] = lists[chosen_index].next
            if lists[chosen_index] is None:
                available_indexes.remove(chosen_index)

        return head


examples = [
    (
        ([ListNode.from_list(i) for i in [[1, 4, 5], [1, 3, 4], [2, 6]]],),
        [1, 1, 2, 3, 4, 4, 5, 6],
    ),
    (
        ([ListNode.from_list([])],),
        None,
    ),
    (
        ([],),
        None,
    ),
]


for _ in range(5):
    random_lists = [random_list(-100, 100, 0, 50, __file__) for i in range(250)]
    examples.append(
        (
            ([ListNode.from_list(i) for i in random_lists],),
            sorted([i for sublist in random_lists for i in sublist]),
        )
    )
