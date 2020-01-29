from flask import Flask
from random import randint
from datetime import datetime

from tasks.tasks import BackgroundProcessTask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dotask')
def do_task():
    first_number = randint(0, 7 ** 7)
    second_number = randint(0, 7 ** 7)
    answer = BackgroundProcessTask().delay(first_number, second_number)
    return f'{datetime.now()} Adding {first_number} and {second_number} = {answer.get()}'


if __name__ == '__main__':
    app.run()
