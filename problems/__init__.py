from importlib import import_module
from os import listdir
from os.path import abspath, basename, dirname, getmtime, isfile, join
from random import randint, seed
from string import digits
from typing import Optional, Union


def import_problem(
    problem_number: Union[str, int, None]
) -> tuple[object, str, str, list[tuple]]:
    problems_dir = abspath(dirname(__file__))
    # determine which module to import
    if problem_number is None:
        # get latest edited Python file
        module_file_path = sorted(
            [
                abspath(join(problems_dir, directory, "__init__.py"))
                for directory in listdir(problems_dir)
                if directory[0] in digits
            ],
            key=lambda p: getmtime(p) if isfile(p) else -1,
        )[-1]
    else:
        problem_number = str(int(problem_number))
        module_file_path = [
            abspath(join(problems_dir, directory, "__init__.py"))
            for directory in listdir(problems_dir)
            if directory.split(" ")[0] == problem_number and directory[0] in digits
        ][0]
    imported_package = basename(dirname(module_file_path))
    # load the module, the solution function, and the examples
    module = import_module("." + imported_package, "problems")
    # noinspection PyUnresolvedReferences
    solution = module.Solution()
    solution_function_name = [
        f
        for f in dir(solution)
        if callable(getattr(solution, f)) and not f.startswith("_")
    ][0]
    if hasattr(module, "examples"):
        examples = module.examples
        if (
            type(examples) != list
            or type(examples[0]) != tuple
            or type(examples[0][0]) != tuple
        ):
            raise Exception("Invalid example values")
    else:
        examples = []
    return solution, imported_package, solution_function_name, examples


class ListNode:
    def __init__(self, val: Optional[int] = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node

    @classmethod
    def from_list(cls, source_list):
        if source_list is None or len(source_list) == 0:
            return None
        node = ListNode(None, None)
        head = node
        for index, item in enumerate(source_list):
            node.val = item
            if index == len(source_list) - 1:
                break
            new_node = ListNode()
            node.next = new_node
            node = new_node
        return head

    def as_list(self) -> list:
        return self._get_values()

    def _get_values(self) -> list:
        return [i for i in self]

    def __repr__(self):
        return f"ListNode({str(self)})"

    def __str__(self):
        return str(self._get_values())

    def __eq__(self, other: "ListNode"):
        if type(other) == list:
            return self._get_values() == other
        return self._get_values() == other._get_values()

    def __len__(self):
        return len(self._get_values())

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, source_list: list, index=0) -> Optional["TreeNode"]:
        if index >= len(source_list):
            return None
        root = TreeNode(source_list[index])
        queue = [root]
        index = 0
        while len(queue) > 0:
            n = queue.pop(0)
            for attr in ["left", "right"]:
                index += 1
                if index >= len(source_list):
                    continue
                value = source_list[index]
                if value is None:
                    n.__setattr__(attr, value)
                    continue
                node = TreeNode(value)
                queue.append(node)
                n.__setattr__(attr, node)
        return root

    def as_list(self) -> list:
        return self._get_values()

    def _get_values(self) -> list:
        values = [n.val if n else None for n in self]
        while values[-1] is None:
            values.pop(-1)
        return values

    def __repr__(self):
        return f"TreeNode({str(self)})"

    def __str__(self):
        return str(self._get_values())

    def __iter__(self):
        queue = [self]
        while len(queue) > 0:
            n = queue[0]
            yield n
            if n:
                queue.append(n.left)
                queue.append(n.right)
            queue.pop(0)

    def __cmp__(self, other: Union["TreeNode", list]):
        return self.as_list() == (
            other if type(other) == type(self) else other.as_list()
        )


def random_list(
    min_value: int = 0,
    max_value: int = 10,
    min_length: int = 0,
    max_length: int = 50,
    random_seed: Union[str, int, float] = __file__,
) -> list[int]:
    seed(random_seed)
    return sorted(
        [randint(min_value, max_value) for _ in range(randint(min_length, max_length))]
    )
