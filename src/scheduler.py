from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger


scheduler = AsyncIOScheduler()


def start_scheduler():
    from src.main import run_pipeline

    scheduler.add_job(run_pipeline, "cron", hour=8, minute=0, id="morning")
    scheduler.add_job(run_pipeline, "cron", hour=12, minute=0, id="noon")
    scheduler.add_job(run_pipeline, "cron", hour=18, minute=0, id="evening")
    scheduler.start()
    logger.info("Scheduler started: daily runs at 08:00, 12:00, 18:00")
