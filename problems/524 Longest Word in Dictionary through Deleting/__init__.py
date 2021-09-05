class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        len_s = len(s)
        chars = set(s)
        max_word = None
        max_len = None
        for word in dictionary:
            word_index = 0
            checked_char = False
            len_word = len(word)
            for index in range(len_s):
                # skip this word if the current character is absent from s
                if not checked_char:
                    checked_char = True
                    if word[word_index] not in chars:
                        break
                if s[index] == word[word_index]:
                    word_index += 1
                    checked_char = False
                    # if this word is completed, see if it's the new best word
                    if word_index >= len_word:
                        if max_word is None:
                            max_word = word
                        else:
                            if len_word > max_len:
                                max_word = word
                            elif len_word == max_len:
                                max_word = min(word, max_word)
                        max_len = len(max_word)
                        break
                    # if it's not completed, but the longest word is still longer than
                    # this word has the possibility of becoming, then skip it
                    elif max_len is not None and (len_s - index) + word_index < max_len:
                        break
        return max_word if max_word else ""


# fmt: off
examples: list[tuple[tuple[str, list[str]], str]] = [
    (('abpcplea', ["apple", "ale", "monkey", "plea"]), "apple"),
    (('abpcplea', ["a", "b", "c"]), "a"),
    (('apple', ["zxc", "vbn"]), ""),
]
# fmt: on
