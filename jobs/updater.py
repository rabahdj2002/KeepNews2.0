from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import getNews


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getNews, 'interval', hours=1)
    scheduler.start()
