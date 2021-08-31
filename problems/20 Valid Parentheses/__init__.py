class Solution:
    def isValid(self, s: str) -> bool:
        open_queue = []
        for c in s:
            is_open = c in "({["
            if c in "()":
                kind = "("
            elif c in "[]":
                kind = "["
            elif c in "{}":
                kind = "{"
            else:
                raise ValueError()
            if is_open:
                open_queue.append(kind)
            else:
                if len(open_queue) < 1:
                    return False
                if open_queue.pop(-1) != kind:
                    return False
        return len(open_queue) == 0


examples = [
    (("()",), True),
    (("(){}[]",), True),
    (("(]",), False),
    (("{[]}",), True),
    (("([)]",), False),
    (("(",), False),
    ((")",), False),
    (("{[}]",), False),
]
