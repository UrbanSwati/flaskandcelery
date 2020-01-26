## Broker settings.
broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'

# List of modules to import when the Celery worker starts.
imports = ('tasks.tasks',)

task_queues = {
    'background.tasks.add': {
        'exchange': 'background.tasks.add',
        'routing_key': 'background.tasks.add',
    }
}

task_routes = {
    'background.tasks.add': {
        'queue': 'background.tasks.add',
        'routing_key': 'background.tasks.add'
    }
}

# task_queues = {
#     'background.tasks.add': {
#         'exchange': 'background.tasks.add',
#         'routing_key': 'background.tasks.add',
#     },
# }