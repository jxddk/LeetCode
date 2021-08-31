from typing import Optional

from .. import TreeNode, random_list


class Solution:
    _cached = {}
    _checked = 0

    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root in self._cached:
            return self._cached[root]
        self._checked += 1
        maximum_value = 0
        for steal in [True, False]:
            children = (
                self._get_grandchildren(root) if steal else self._get_children(root)
            )
            additional_value = root.val if steal else 0
            new_value = sum([self.rob(child) for child in children]) + additional_value
            maximum_value = max(new_value, maximum_value)
        self._cached[root] = maximum_value
        return maximum_value

    def _get_children(self, node: TreeNode):
        return [n for n in [node.left, node.right] if n is not None]

    def _get_grandchildren(self, node: TreeNode):
        return [
            n for child in self._get_children(node) for n in self._get_children(child)
        ]


examples: list[tuple[tuple[TreeNode], int]] = [
    ((TreeNode.from_list([3, 2, 3, None, 3, None, 1]),), 7),
    ((TreeNode.from_list([3, 4, 5, 1, 3, None, 1]),), 9),
    ((TreeNode.from_list(random_list(0, 10 ** 4, 10 ** 4, 10 ** 4)),), 39906791),
]
