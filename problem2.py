import sys
from datetime import datetime


def timed_output(original_write):
    def my_write(string_text: str) -> None:
        if string_text == '\n':
            modified_text = string_text
        else:
            timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]: ')
            modified_text = timestamp + string_text
        original_write(modified_text)

    def decorator(func):
        def wrapper(*args, **kwargs):
            original_stdout_write = sys.stdout.write
            sys.stdout.write = my_write
            result = func(*args, **kwargs)
            sys.stdout.write = original_stdout_write
            return result

        return wrapper

    return decorator


@timed_output(sys.stdout.write)
def print_greeting(name):
    print(f'приветик, {name}!!')


if __name__ == '__main__':
    print_greeting('лизочка')
