class Solution:
    # this is the string manipulation solution - not very impressive, but easy!
    def _reverse_string_manipulation(self, x: int) -> int:
        result = str(x)[::-1]
        while result[0] == "0" and len(result) > 2:
            result = result[1:]
        if result[-1] == "-":
            result = "-" + result[:-1]

        result = int(result)
        bounds = 2**31
        if not -1 * bounds < result < bounds - 1:
            return 0

        return result

    # this is the more involved, mathematical solution
    def reverse(self, x: int) -> int:
        from math import log10, ceil

        # no use trying to be smart with this one
        if x == 0:
            return x
        is_negative = x < 0
        x = abs(x)

        # for each power of 10 ("place"), invert according to position in x
        max_places = ceil(log10(x + 1))
        result = 0
        # numbers less than 10 get special treatment
        if max_places == 0:
            result = x
        for place in range(max_places):
            modulated = x % (10 ** (place + 1))
            truncated = int(modulated / (10**place))
            inverted = truncated * (10 ** (max_places - place - 1))
            result += inverted

        if is_negative:
            result *= -1

        # python doesn't really have i32's, so this is the alternative
        bounds = 2**31
        if not -1 * bounds < result < bounds - 1:
            return 0

        return result


examples = [
    ((123,), 321),
    ((-123,), -321),
    ((21,), 12),
    ((120,), 21),
    ((0,), 0),
    ((1534236469,), 0),
    ((1,), 1),
    ((13,), 31),
    ((10,), 1),
]
