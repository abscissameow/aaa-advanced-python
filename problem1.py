import sys
from datetime import datetime


def my_write(string_text: str) -> None:
    if string_text == '\n':
        modified_text = string_text
    else:
        timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]: ')
        modified_text = timestamp + string_text
        original_write(modified_text)


if __name__ == '__main__':
    original_write = sys.stdout.write
    print('подменяем!')
    sys.stdout.write = my_write
    print('мяу мяу')
    sys.stdout.write = original_write
    print('\nвозвращаем..')
    print('мяу мяу')
