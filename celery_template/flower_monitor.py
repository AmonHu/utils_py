from os import system
from config import broker_url


def start_flower():
    system(f'celery flower --broker={broker_url}')


if __name__ == '__main__':
    start_flower()
