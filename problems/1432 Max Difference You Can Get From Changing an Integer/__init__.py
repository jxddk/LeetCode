class Solution:
    def maxDiff(self, num: int) -> int:
        return abs(self._repl_number(num, True) - self._repl_number(num, False))

    def _repl_number(self, num: int, high: bool) -> int:
        n = str(num)
        seen = set()
        for index in range(len(n)):
            c = n[index]
            if c in seen:
                continue
            seen.add(c)
            v = None

            if high:
                if c == "9":
                    continue
                v = "9"
            else:
                if index == 0:
                    if c == "1":
                        continue
                    v = "1"
                else:
                    if c == "0":
                        continue
                    v = "0"

            if v is not None:
                return int(n.replace(c, v))
        return num


# fmt: off
examples: list[tuple[tuple[int], int]] = [
    ((555, ), 888),
    ((9, ), 8),
    ((123456, ), 820000),
    ((10000, ), 80000),
    ((9288, ), 8700),
    ((111, ), 888),
]
# fmt: on
