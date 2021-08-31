class Solution:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        index = 0
        previous = None
        while index <= len(s):
            v = None
            if index < len(s):
                v = self.symbols[s[index]]

            if previous is not None and v is not None:
                if previous / v in [0.1, 0.2, 0.5]:
                    total += v - previous
                    previous = None
                else:
                    total += previous
                    previous = v
            elif previous is not None:
                total += previous
                previous = v
            else:
                previous = v

            index += 1
        return total


examples = [
    (("III",), 3),
    (("IV",), 4),
    (("IX",), 9),
    (("V",), 5),
    (("LVIII",), 58),
    (("MCMXCIV",), 1994),
    (("M",), 1000),
    (("I",), 1),
    (("VIII",), 8),
]
