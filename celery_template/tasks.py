import time
from celery import Celery

app = Celery('queue')
app.config_from_object('config')


@app.task
def hello(name: str):
    time.sleep(1)
    return f'hello, {name}'
