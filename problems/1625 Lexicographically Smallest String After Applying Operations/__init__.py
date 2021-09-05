class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        tried_options: set[str] = set()

        queue: list[str] = [s]
        while len(queue) > 0:
            n = queue.pop(0)
            added = "".join(
                [
                    str((int(i) + a) % 10) if index % 2 == 1 else i
                    for index, i in enumerate(n)
                ]
            )
            rotated = n[b:] + n[:b]
            for new in [rotated, added]:
                if new in tried_options:
                    continue
                queue.append(new)
            tried_options.add(n)

        return str(min(tried_options, key=lambda x: int(x)))


# fmt: off
examples: list[tuple[tuple[str, int, int], str]] = [
    (("5525", 9, 2), "2050"),
    (("74", 5, 1), "24"),
    (("0011", 4, 2), "0011"),
    (("43987654", 7, 3), "00553311"),
]
# fmt: on
