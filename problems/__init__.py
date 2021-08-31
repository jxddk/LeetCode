from importlib import import_module
from os import listdir
from os.path import abspath, basename, dirname, getmtime, isfile, join
from random import randint, seed
from string import digits
from typing import Generator, Optional, Union


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

    def as_ascii(self, draw_null_children: bool = False) -> str:
        return tree_to_ascii(self, "val", ("left", "right"), draw_null_children)

    def _iter_levels(self) -> Generator[tuple["TreeNode", int], None, None]:
        queue = [(self, 0)]
        while len(queue) > 0:
            node, level = queue.pop(0)
            yield node, level
            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

    def _get_values(self) -> list:
        values = [n.val if n else None for n in self]
        while values[-1] is None:
            values.pop(-1)
        return values

    def __repr__(self):
        return f"TreeNode({str(self)})"

    def __str__(self):
        return str(self._get_values())

    def __iter__(self) -> Generator["TreeNode", None, None]:
        for node, level in self._iter_levels():
            yield node

    def __cmp__(self, other: Union["TreeNode", list]):
        return self.as_list() == (
            other if type(other) == type(self) else other.as_list()
        )


def tree_to_ascii(
    tree: object,
    val_attr: str,
    child_attrs: tuple[str, ...],
    show_null_children: bool = False,
) -> str:
    # this is hidden away here in the utility functions, but I must admit I am proud
    # of how quickly I managed to figure out a tree-to-ascii printer
    if tree is None:
        return " "
    margin = 3
    value = str(tree.__getattribute__(val_attr))
    children = [tree.__getattribute__(child) for child in child_attrs]
    if not show_null_children:
        children = [c for c in children if c is not None]

    if len([c for c in children if c is not None]) <= 0:
        return value

    child_trees = [
        tree_to_ascii(child, val_attr, child_attrs, show_null_children).split("\n")
        for child in children
    ]

    if len(child_trees) <= 0:
        return value

    child_value_indexes = []
    child_lengths = []
    child_heights = []
    for child_index, child in enumerate(child_trees):
        prev_length = 0 if child_index == 0 else child_lengths[-1]
        offset = prev_length + (margin * len(child_lengths))
        child_lengths.append(len(child[0]))
        child_heights.append(len(child))
        child_value_indexes.append((len(child[0]) // 2) + offset)

    total_child_length = sum(child_lengths) + (margin * (len(child_lengths) - 1))
    max_child_head = max(child_heights)

    output = []
    for line in [value, "|"]:
        counter = 0
        while len(line) < total_child_length:
            counter += 1
            if counter % 2 == 0:
                line = line + " "
            else:
                line = " " + line
        output.append(line)
    line_start = min(child_value_indexes)
    line_end = max(child_value_indexes)
    line_line = ""
    for index in range(total_child_length):
        if index in child_value_indexes:
            if index == line_start == line_end:
                line_line += "|"
            elif index == line_start:
                line_line += "/"
            elif index == line_end:
                line_line += "\\"
            else:
                line_line += "|"
        elif line_start <= index <= line_end:
            line_line += "-"
        else:
            line_line += " "
    output.append(line_line)

    for line_index in range(max_child_head):
        child_line = []
        for child in child_trees:
            if line_index >= len(child):
                line = " " * len(child[0])
            else:
                line = child[line_index]
            child_line.append(line)
        output.append((" " * margin).join(child_line))

    return "\n".join(output)


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
