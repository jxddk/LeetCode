class Solution:
    def longestWord(self, words: list[str]) -> str:
        longest_word = ""

        words.sort(key=lambda w: len(w))

        queue: list[tuple[str, int]] = [("", -1)]
        seen_indexes = set()

        while len(queue) > 0:
            string, start_index = queue.pop(0)
            seen_indexes.add(start_index)
            for index in range(start_index, len(words)):
                if index in seen_indexes:
                    continue
                if len(words[index]) <= len(string):
                    continue
                elif len(words[index]) > len(string) + 1:
                    break
                if not words[index].startswith(string):
                    continue
                if len(words[index]) > len(longest_word):
                    longest_word = words[index]
                elif len(words[index]) == len(longest_word):
                    longest_word = min(longest_word, words[index])
                queue.append((words[index], index))

        return longest_word


# fmt: off
examples: list[tuple[tuple[list[str]], str]] = [
    ((["w", "wo", "wor", "worl", "world"], ),  "world"),
    ((["a", "banana", "app", "appl", "ap", "apply", "apple"], ), "apple"),
    ((["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"], ), "latte"),
]
# fmt: on
