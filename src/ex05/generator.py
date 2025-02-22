import sys
import resource


class InputCommandError(Exception):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]}"


def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


def check_command(command):
    if len(command) != 2:
        raise InputCommandError(
            'Not correct len of command. '
            f'Use python3 {command[0]} <path_to_file>'
        )
    return command[1]


if __name__ == '__main__':
    command = sys.argv
    try:
        file_path = check_command(command)
        # line_count = 0 # для подсчета строк
        for line in read_file_generator(file_path):
            # line_count += 1 # для подсчета строк
            pass

        # print(f"Total Lines = {line_count}") # для подсчета строк
        usage = resource.getrusage(resource.RUSAGE_SELF)
        print(f"Peak Memory Usage = {usage.ru_maxrss / (1024 ** 2):.3f} GB")
        print(
            'User Mode Time + System Mode Time = '
            f'{usage.ru_utime + usage.ru_stime:.2f}s'
        )
    except InputCommandError as e:
        print(e)
    except FileNotFoundError as e:
        print(f'{e.__class__.__name__}: {e}')
