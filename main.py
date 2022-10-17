#!bin/usr/python

from copy import deepcopy
from sys import argv
from traceback import format_exc
from time import time

from problems import import_problem

if __name__ == "__main__":
    try:
        solution, problem_name, solution_function_name, examples = import_problem(
            argv[1] if len(argv) > 1 else None
        )
    except Exception as e:
        raise type(e)(f"Could not import the solution: {e}")
    # run the solution with test values
    print(f"EXECUTING: {problem_name} | {solution_function_name}")
    example_total_time = 0
    results = []
    for values, answer in examples:
        result = None
        try:
            example_start = time()
            result = solution.__getattribute__(solution_function_name)(
                *deepcopy(values)
            )
            example_total_time = time() - example_start
            valid = result == answer
            if valid:
                print(
                    f"SUCCEEDED: Time: {example_total_time:.2f}ms | "
                    f"Arguments: {values} | Result: {result}"
                )
            else:
                print(
                    f"INCORRECT EXAMPLE: Time: {example_total_time:.2f}ms | "
                    f"Arguments: {values} | Result: {result} | Expected: {answer}"
                )
            results.append((valid, example_total_time))
        except Exception as e:
            print(
                f"ERROR IN EXAMPLE: "
                f"Arguments: {values} | Expected: {answer} | ERROR: {format_exc()}"
            )
            results.append((None, 0))
    print(
        f"FINISHED: Ran {len(examples)} examples in "
        f"{sum([t for r, t in results]):.2f}ms | "
        f"Succeeded {len([r for r, t in results if r == True])} | ",
        f"Failed {len([r for r, t in results if r == False])} | ",
        f"Error {len([r for r, t in results if r is None])}",
    )
