from typing import Optional, Union

from .. import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self._calculate_zigzag(root, None, 0, 0)

    def _calculate_zigzag(
        self,
        node: Optional[TreeNode],
        is_left: Union[bool, None],
        zigzagging: int,
        max_zag: int,
    ) -> int:
        for is_right, child in [(False, node.left), (True, node.right)]:
            if child is None:
                continue
            new_zigzag = zigzagging
            if is_left != is_right:
                new_zigzag = 0
            new_zigzag += 1
            max_zag = max(
                new_zigzag,
                max_zag,
                self._calculate_zigzag(child, not is_right, new_zigzag, max_zag),
            )
        return max(max_zag, zigzagging)


# fmt: off
examples: list[tuple[tuple[TreeNode], int]] = [
    ((TreeNode.from_list([1, None, 1, 1, None, 1, 1, None, 1, None, 1]),), 3),
    ((TreeNode.from_list([1, 1]),), 1),
    ((TreeNode.from_list([1]),), 0),
    ((TreeNode.from_list([1, 1, 1, 1, None, None, 1]),), 1),
    ((TreeNode.from_list([1, 1, 1, None, 1, None, None, 1, 1, None, 1]),), 4),
    ((TreeNode.from_list([1, 1, None, 1, 1, None, None, 1, 1, 1]),), 3),
    ((TreeNode.from_list([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]),), 3,),
    ((TreeNode.from_list([1, 1, 1, None, 1, None, None, 1, 1, None, 1]),), 4),
]
# fmt: on
