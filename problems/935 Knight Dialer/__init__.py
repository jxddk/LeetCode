class Solution:
    _numbers = set([_ for _ in range(10)])
    _board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
    _knight = (2, 1)

    _hops: dict[int, set[int]] = {n: set() for n in _numbers}
    _cache: dict[int, dict[int, int]] = {}

    def knightDialer(self, n: int) -> int:
        self._precache_dials(max_n=n)
        return sum(v for v in self._dial_data(n).values()) % ((10**9) + 7)

    def __init__(self):
        self._precache_hops()
        self._precache_dials()

    # calculate the possible from each possible starting position,
    # and cache the results to speed up later calculations.
    def _precache_hops(self):
        deltas: set[tuple[int, int]] = set()
        xk, yk = self._knight
        for dx in [xk, -xk]:
            for dy in [yk, -yk]:
                deltas.add((dx, dy))
                deltas.add((dy, dx))
        for xi in range(len(self._board)):
            for yi in range(len(self._board[xi])):
                if self._board[xi][yi] not in self._numbers:
                    continue
                for dx, dy in deltas:
                    x = dx + xi
                    y = dy + yi
                    try:
                        if x < 0 or y < 0 or self._board[x][y] not in self._numbers:
                            continue
                        self._hops[self._board[xi][yi]].add(self._board[x][y])
                    except IndexError:
                        continue

    # maximum recursion depth got you down? try this one weird trick!
    def _precache_dials(self, step=500, max_n=5000):
        for n in range(step, max_n, step):
            if n in self._cache:
                continue
            self._cache[n] = self._dial_data(n)

    def _dial_data(self, n: int) -> dict[int, int]:
        if n == 1:
            return {i: 1 for i in self._numbers}
        if n in self._cache:
            return self._cache[n]
        previous = self._dial_data(n - 1)
        new = {i: 0 for i in self._numbers}
        for number in previous:
            for hop in self._hops[number]:
                new[hop] += previous[number]
        return new

    # always fun to implement a little BFS. Also useful for checking results.
    def _brute_force(self, n: int) -> int:
        total = 0
        queue = {(n,) for n in self._numbers}
        while len(queue) > 0:
            i = queue.pop()
            if len(i) == n:
                total += 1
                continue
            for hop in self._hops[i[-1]]:
                queue.add(i + (hop,))
        return total


examples = [
    ((1,), 10),
    ((2,), 20),
    ((3,), 46),
    ((4,), 104),
    ((5,), 240),
    ((6,), 544),
    ((7,), 1256),
    ((3131,), 136006598),
]
