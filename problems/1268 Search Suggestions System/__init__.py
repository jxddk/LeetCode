class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        products.sort()
        results = [[] for _ in range(len(searchWord))]
        for word in products:
            for index in range(min(len(searchWord), len(word))):
                if searchWord[index] == word[index]:
                    if len(results[index]) < 3:
                        results[index].append(word)
                else:
                    break
        return results


examples: list[tuple[tuple[list[str], str], list[list[str]]]] = [
    (
        (["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"),
        [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ],
    ),
    (
        (["havana"], "havana"),
        [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
    ),
    (
        (["bags", "baggage", "banner", "box", "cloths"], "bags"),
        [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"],
        ],
    ),
    ((["havana"], "tatiana"), [[], [], [], [], [], [], []]),
]
