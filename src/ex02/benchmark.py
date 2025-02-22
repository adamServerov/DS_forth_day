import sys
import timeit


class BenchmarkError(Exception):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]}"


class NameFilterError(BenchmarkError):
    pass


class NumberCallsError(BenchmarkError):
    pass


def get_emails(number):
    base_emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
    ]
    return base_emails * number


def measure_time(func):
    def wrapper(emails, repetitions):
        time = timeit.timeit(lambda: func(emails), number=repetitions)
        return time
    return wrapper


@measure_time
def filter_gmails_loop(emails: list) -> list:
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


@measure_time
def filter_gmails_comprehension(emails: list) -> list:
    return [email for email in emails if email.endswith('@gmail.com')]


@measure_time
def filter_gmails_map(emails: list):
    gmails = map(
        lambda email: email if email.endswith('@gmail.com') else None,
        emails
    )
    return gmails


@measure_time
def filter_gmails_filter(emails: list):
    gmails = filter(lambda email: email.endswith('@gmail.com'), emails)
    # print(list(res))
    return gmails


def check_command(command):
    if len(command) != 3:
        raise BenchmarkError(
            'Not correct len of command. Use <filter_name> <number_of_calls>'
        )
    *_, filter_name, measure_number = command
    correct_filters = ['map', 'filter', 'list_comprehension', 'loop']
    if filter_name.lower() not in correct_filters:
        raise NameFilterError(
            f'filter_name <{filter_name}> not exist. Use correct one of map, '
            'filter, list_comprehension, loop')
    try:
        measure_number = int(measure_number)
    except ValueError:
        raise NumberCallsError(
            f'Your input number of calls: <{measure_number}> '
            'is not digit'
        )
    if measure_number <= 0:
        raise NumberCallsError(
            f'Your input number of calls:  <{measure_number}> is less than 1. '
            'Please use positive number.'
        )
    return filter_name.lower(), measure_number


def main():
    command = sys.argv
    number = 5
    emails = get_emails(number)
    try:
        filter_name, measure_number = check_command(command)
        result_time = None
        match filter_name:
            case 'loop':
                result_time = filter_gmails_loop(emails, measure_number)
            case 'map':
                result_time = filter_gmails_map(emails, measure_number)
            case 'list_comprehension':
                result_time = filter_gmails_comprehension(
                    emails, measure_number
                )
            case 'filter':
                result_time = filter_gmails_filter(emails, measure_number)
        print(f'{result_time:.14f}')
    except BenchmarkError as e:
        print(e)


if __name__ == '__main__':
    main()
