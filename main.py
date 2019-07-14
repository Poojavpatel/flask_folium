from flask import Flask
from celery import Celery
from flask_celery import make_celery

app=Flask(__name__)
app.config['celery_broker_url'] = 'ampq://localhost//'

celery = make_celery(app)








if __name__ == '__main__':
    app.run(debug=True)