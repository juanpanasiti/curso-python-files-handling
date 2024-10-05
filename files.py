from utils import get_now

FILE_NAME = 'messages.txt'


def write_messages() -> None:
    # file = open('test.txt', 'w')
    # # TODO trabajar con el archivo
    # file.close()
    with open(FILE_NAME, 'a') as file:
        while True:
            message = input('Escriba un mensaje: ')
            if not message:
                break
            file.write(f'{get_now()} - {message}\n')


def read_messages() -> None:
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(line, end='')
