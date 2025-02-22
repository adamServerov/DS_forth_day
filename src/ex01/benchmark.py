import timeit


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
def filter_gmails_loop(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


@measure_time
def filter_gmails_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


@measure_time
def filter_gmails_map(emails):
    res = map(
        lambda email: email if email.endswith('@gmail.com') else None,
        emails
    )
    return res


def match_result(time_res, loop_time, comprehension_time):
    if time_res == loop_time:
        return 'a loop'
    if time_res == comprehension_time:
        return 'a list comprehension'
    return 'a map'


def main():
    number = 5
    MEASURE_NUMBER = 90000000
    # MEASURE_NUMBER = 100000
    emails = get_emails(number)
    loop_time = filter_gmails_loop(emails, MEASURE_NUMBER)
    comprehension_time = filter_gmails_comprehension(emails, MEASURE_NUMBER)
    map_time = filter_gmails_map(emails, MEASURE_NUMBER)

    time_result = sorted([loop_time, comprehension_time, map_time])
    quiqe_time = match_result(time_result[0], loop_time, comprehension_time)

    print(f'it is better to use {quiqe_time}')
    print(
        f'{time_result[0]:.14f} vs {time_result[1]:.14f} '
        f'vs {time_result[2]:.14f}'
    )


if __name__ == '__main__':
    main()
