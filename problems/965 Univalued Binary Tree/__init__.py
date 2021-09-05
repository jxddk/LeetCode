from typing import Optional

from .. import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v = None
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                continue
            if v is None:
                v = node.val
            if v != node.val:
                return False
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return True


# fmt: off
examples: list[tuple[tuple[TreeNode], bool]] = [
    ((TreeNode.from_list([1, 1, 1, 1, 1, None, 1]),), True),
    ((TreeNode.from_list([2, 2, 2, 5, 2]),), False),
]
# fmt: on
