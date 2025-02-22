import random
import timeit
from collections import Counter


def measure_time(func):
    def wrapper(data):
        start_time = timeit.default_timer()
        func_result = func(data)
        time_duration = timeit.default_timer() - start_time
        return time_duration, func_result
    return wrapper


def get_random_list():
    RANDOM_VALUES = 1_000_000
    return [random.randint(0, 100) for _ in range(RANDOM_VALUES)]


@measure_time
def my_function(data):
    dict_res = {}
    for num in data:
        dict_res[num] = dict_res.get(num, 0) + 1
    return dict_res


@measure_time
def get_top_10(data):
    top_ten = sorted(data.items(), key=lambda item: -item[1])[:10]
    # print(top_ten)
    return top_ten


@measure_time
def count_with_counter(data):
    res = Counter(data)
    # print(res)
    return res


@measure_time
def top_10_with_counter(data):
    # top_ten = Counter(data).most_common(10)
    top_ten = data.most_common(10)
    # print(top_ten)
    return top_ten


def main():
    random_list = get_random_list()

    my_dict_time, my_dict_res = my_function(random_list)
    my_top_time, my_top_res = get_top_10(my_dict_res)

    counter_dict_time, counter_dict_res = count_with_counter(random_list)
    counter_top_time, counter_top_res = top_10_with_counter(counter_dict_res)

    print(f'my function: {my_dict_time:.7f}')
    print(f'Counter: {counter_dict_time:.7f}')
    print(f'my top: {my_top_time:.7f}')
    print(f"Counter's top: {counter_top_time:.7f}")

    assert my_dict_res == counter_dict_res, "Error: dict results not equal!"
    assert my_top_res == counter_top_res, "Error: Top 10 results do not equal!"


if __name__ == '__main__':
    main()
