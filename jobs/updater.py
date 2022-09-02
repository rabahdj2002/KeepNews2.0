from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import getNews, keepAlive


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getNews, 'interval', hours=1)
    scheduler.add_job(keepAlive, 'interval', minutes=1)
    scheduler.start()

