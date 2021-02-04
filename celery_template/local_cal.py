from tasks import hello


def hello_call():
    r = hello.delay(name='celery')
    while not r.ready():
        print('hello task is not ready.')

    print(r)
