# 指定 Broker
broker_url = f'amqp://user_name:password@localhost:5672//'
# 指定 Backend
result_backend = f'redis://localhost:6379'

# 指定时区，默认是 UTC
timezone = 'Asia/Shanghai'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['pickle', 'json', 'msgpack', 'application/json']
worker_send_task_events = True
