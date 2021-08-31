#!bin/usr/python

from copy import deepcopy
from sys import argv
from traceback import format_exc

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
    for values, answer in examples:
        result = None
        try:
            result = solution.__getattribute__(solution_function_name)(
                *deepcopy(values)
            )
            assert result == answer
            print(f"SUCCEEDED: Arguments: {values} | Result: {result}")
        except AssertionError as e:
            print(
                f"INCORRECT EXAMPLE: Arguments: {values} | Result: {result} | Expected: {answer}"
            )
        except Exception as e:
            print(
                f"ERROR IN EXAMPLE: Arguments: {values} | Expected: {answer} | ERROR: {format_exc()}"
            )
    print(
        f"FINISHED: Ran {len(examples)} examples",
    )
