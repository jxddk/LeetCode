class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        index = 0
        valid = True
        while valid:
            character = None
            for s in strs:
                if index >= len(s):
                    valid = False
                    break
                if character is None:
                    character = s[index]
                if character != s[index]:
                    valid = False
                    break
            if character is None or not valid:
                break
            prefix += character
            index += 1
        return prefix


examples = [
    ((["flower", "flow", "flight"],), "fl"),
    ((["dog", "racecar", "car"],), ""),
    (([""],), ""),
    ((["", "test"],), ""),
]
