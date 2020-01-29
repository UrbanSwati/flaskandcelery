# from celery.task import Task # Deprecated
from celery.app.task import Task
from datetime import datetime


class BackgroundProcessTask(Task):
    """
    set ignore_result to True if you don't need the result 
    This will return None on .get() of the task result
    """
    
    name = "background.tasks.add"
    routing_key = "background.tasks.add"
    ignore_result = False
    default_retry_delay = 60  # 1 minute.
    max_retries = 5
    serializer = 'pickle'

    def run(self, first_number, second_number, **kwargs):
        answer = first_number + second_number
        print(f'Done with task at {datetime.now()} : {first_number} + {second_number} = {answer}')
        return answer
