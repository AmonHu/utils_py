from celery import Celery


app = Celery('queue')
app.config_from_object('config')


def _on_completed(task_id, result):
    print(task_id + ' done. ' + result)


def _on_state_changed(task_info):
    print(task_info)


def hello_call():
    r = app.send_task(name='hello', args='celery')
    r.get(on_message=_on_state_changed, callback=_on_completed)


if __name__ == '__main__':
    hello_call()
