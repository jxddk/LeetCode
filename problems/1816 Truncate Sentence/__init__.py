class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # `return " ".join(s.split(" ")[:k])` is probably more performant, but it
        # feels like cheating
        spaces = 0
        output = ""
        for char in s:
            if char == " ":
                spaces += 1
            if spaces >= k:
                break
            output += char
        return output


examples = [(("Hello how are you Contestant", 4), "Hello how are you")]
