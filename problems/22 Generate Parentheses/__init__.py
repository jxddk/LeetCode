class Solution:
    _cached = {}

    def generateParenthesis(self, n: int) -> list[str]:
        if n in self._cached:
            return self._cached[n]
        results = set()
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            for i in range(1, n):
                for first in self.generateParenthesis(i):
                    for second in self.generateParenthesis(n - i):
                        results.add(first + second)
                        if i == 1:
                            results.add(f"({second})")
        self._cached[n] = sorted(list(results))
        return self._cached[n]


examples = [
    (
        (5,),
        sorted(
            [
                "((((()))))",
                "(((()())))",
                "(((())()))",
                "(((()))())",
                "(((())))()",
                "((()(())))",
                "((()()()))",
                "((()())())",
                "((()()))()",
                "((())(()))",
                "((())()())",
                "((())())()",
                "((()))(())",
                "((()))()()",
                "(()((())))",
                "(()(()()))",
                "(()(())())",
                "(()(()))()",
                "(()()(()))",
                "(()()()())",
                "(()()())()",
                "(()())(())",
                "(()())()()",
                "(())((()))",
                "(())(()())",
                "(())(())()",
                "(())()(())",
                "(())()()()",
                "()(((())))",
                "()((()()))",
                "()((())())",
                "()((()))()",
                "()(()(()))",
                "()(()()())",
                "()(()())()",
                "()(())(())",
                "()(())()()",
                "()()((()))",
                "()()(()())",
                "()()(())()",
                "()()()(())",
                "()()()()()",
            ]
        ),
    ),
    (
        (4,),
        sorted(
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ]
        ),
    ),
    ((3,), sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])),
    ((2,), sorted(["(())", "()()"])),
    ((1,), sorted(["()"])),
]