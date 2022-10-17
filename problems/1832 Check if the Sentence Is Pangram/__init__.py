from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {l: False for l in ascii_lowercase}
        for letter in sentence:
            if not letters[letter]:
                letters[letter] = True
                valid = True
                for value in letters.values():
                    if not value:
                        valid = False
                        break
                if valid:
                    return True
        return False

    # this is by far the easiest and fastest for Python, but it feels like cheating
    def _lazyCheckIfPangram(self, sentence: str) -> bool:
        return set(ascii_lowercase) == set(sentence)


examples = [
    (("thequickbrownfoxjumpsoverthelazydog",), True),
    (("leetcode",), False),
]
