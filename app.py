from flask import Flask
from celery import Celery

# Инициализация Flask приложения
app = Flask(__name__)


# Инициализация Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery


# Загрузка конфигурации Celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

# Импорт вьюшек после инициализации app и celery
import views
