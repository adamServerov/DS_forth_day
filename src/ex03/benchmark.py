import sys
import timeit
from functools import reduce


class BenchmarkError(Exception):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]}"


class FunctionNameError(BenchmarkError):
    pass


class NumberCallsError(BenchmarkError):
    pass


class NumberForSumError(BenchmarkError):
    pass


def measure_time(func):
    def wrapper(number, repetitions):
        time = timeit.timeit(lambda: func(number), number=repetitions)
        return time
    return wrapper


@measure_time
def func_loop(number):
    res = 0
    for i in range(1, number+1):
        res += i * i
    # print(res)
    return res


@measure_time
def func_reduce(number):
    numbers = range(1, number+1)
    res = reduce(lambda x, y: x + y * y, numbers)
    # print(res)
    return res


def check_command(command):
    if len(command) != 4:
        raise BenchmarkError(
            'Not correct len of command. Use <func_name> '
            '<number_of_calls> <number_for_sum>'
        )
    *_, func_name, measure_number, sum_number = command
    correct_funcs = ['loop', 'reduce']
    if func_name.lower() not in correct_funcs:
        raise FunctionNameError(
            f'func_name <{func_name}> not exist. Use correct one of loop, '
            'or reduce')
    try:
        measure_number = int(measure_number)
    except ValueError:
        raise NumberCallsError(
            f'Your input number of calls: <{measure_number}> is not digit'
        )
    try:
        sum_number = int(sum_number)
    except ValueError:
        raise NumberForSumError(
            f'Your input input sum number: <{sum_number}> is not digit'
        )
    if measure_number <= 0:
        raise NumberCallsError(
            f'Your input number of calls {measure_number} < 1. '
            'Input please positive number'
        )
    if sum_number <= 0:
        raise NumberForSumError(
            f'Your input sum number {sum_number} < 1. '
            'Input please positive number and not zero'
        )

    return func_name, measure_number, sum_number


def main():
    command = sys.argv
    try:
        func_name, measure_number, sum_number = check_command(command)
        result_time = None
        if func_name == 'loop':
            result_time = func_loop(sum_number, measure_number)
        else:
            result_time = func_reduce(sum_number, measure_number)

        print(f'{result_time:.14f}')
    except BenchmarkError as e:
        print(e)


if __name__ == '__main__':
    main()
