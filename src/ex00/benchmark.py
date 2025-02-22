import timeit


def get_emails(number):
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
    ]
    return emails * number


def filter_gmails_loop(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails


def filter_gmails_comprehension(emails):
    gmails = [email for email in emails if email.endswith('@gmail.com')]
    return gmails


def main():
    number = 5
    emails = get_emails(number)

    MEASURE_NUMBER = 90000000
    # MEASURE_NUMBER = 20

    loop_time = timeit.timeit(
        lambda: filter_gmails_loop(emails), number=MEASURE_NUMBER
    )
    comprehension_time = timeit.timeit(
        lambda: filter_gmails_comprehension(emails), number=MEASURE_NUMBER
    )

    if comprehension_time <= loop_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")
    min_time = min(loop_time, comprehension_time)
    max_time = max(loop_time, comprehension_time)
    print(f'{min_time:.14f} vs {max_time:.14f}')


if __name__ == '__main__':
    main()
