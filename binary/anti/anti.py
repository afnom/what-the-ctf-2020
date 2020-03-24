import os
import sys
import re


def main():
    print("Welcome to the anti-flag shell!")
    print("still in development, expect bugs")
    print()

    while True:
        print('$ ', end='')
        sys.stdout.flush()

        line = input()
        parts = line.split()
        if len(parts) == 0:
            continue

        if run(parts[0], *parts[1:]):
            break

    sys.stdout.flush()


ERROR_COMMAND = print


def run(command, *args):
    if command == 'ls':
        ls(*args, chunks=['DIRECTORIES', 20 * '-'])
        return False
    elif command == 'cat':
        cat(*args)
        return True
    elif command == 'error':
        global ERROR_COMMAND
        if re.match('^[a-zA-Z\.]*$', args[0]):
            ERROR_COMMAND = eval(args[0])
        else:
            print('ERROR: invalid error handler')
        return False


def ls(*args, chunks=[]):
    directories = ' '.join(os.listdir())
    chunks.append(directories)

    for chunk in chunks:
        print(chunk)


def cat(filename, *args, chunks=[]):
    try:
        with open(filename) as target:
            chunks.append(target.read())
    except FileNotFoundError:
        pass

    if 'flag' in filename:
        return ERROR_COMMAND('ERROR: permissions denied')

    for chunk in chunks:
        print(chunk)


if __name__ == "__main__":
    main()
