from random import choice, randint, seed


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend >= 0) != (divisor >= 0)
        divisor, dividend = abs(divisor), abs(dividend)

        addition_amount = divisor
        addition_count = 1
        previous_addition_amount = addition_amount
        previous_addition_count = addition_amount
        total_amount = 0
        total_count = 0

        while total_amount < dividend:
            while total_amount > dividend - addition_amount:
                addition_amount, previous_addition_amount = (
                    addition_amount - previous_addition_amount,
                    addition_amount,
                )
                addition_count, previous_addition_count = (
                    addition_count - previous_addition_count,
                    addition_count,
                )
                if addition_count < 1:
                    addition_amount = divisor
                    addition_count = 1
                    break

            if total_amount > dividend - addition_amount:
                break

            total_amount += addition_amount
            total_count += addition_count

            addition_amount, previous_addition_amount = (
                addition_amount + addition_amount,
                addition_amount,
            )
            addition_count, previous_addition_count = (
                addition_count + addition_count,
                addition_count,
            )

        if is_negative:
            total_count = 0 - total_count
        bounds = 2147483648
        return min(max(total_count, 0 - bounds), bounds - 1)


examples = [
    (
        (
            10,
            3,
        ),
        3,
    ),
    ((7, -3), -2),
    ((0, 1), 0),
    ((1, 1), 1),
    ((1, -1), -1),
    ((6, 2), 3),
    ((7, 2), 3),
    ((8, 2), 4),
    ((9, 2), 4),
    ((9, 3), 3),
    ((-2147483648, -1), 2147483647),
    ((-231, 3), -77),
]

seed(__file__)
for _ in range(2**12):
    random_signs = [1, -1]
    random_dividend = randint(0, (2**31) - 1) * choice(random_signs)
    random_divisor = randint(1, (2**8) - 1) * choice(random_signs)
    random_answer = int(random_dividend / random_divisor)
    examples.append(((random_dividend, random_divisor), random_answer))
