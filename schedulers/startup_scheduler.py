# from datetime import datetime

# from apscheduler.schedulers.background import BackgroundScheduler


# class StartupScheduler:

#     def __init__(self, startup_service):

#         self.startup_service = startup_service

#         self.scheduler = BackgroundScheduler(
#             timezone="Asia/Kolkata"
#         )

#     def start(self):

#         self.scheduler.add_job(
#             self.startup_service.run_automation,
#             trigger="interval",
#             hours=7,
#             id="startup_automation",
#             replace_existing=True,
#             max_instances=1,
#             coalesce=True,
#             next_run_time=datetime.now(self.scheduler.timezone)
#         )

#         self.scheduler.start()

#         print("Startly AI scheduler started")

#     def shutdown(self):

#         if self.scheduler.running:
#             self.scheduler.shutdown()
#             print("Scheduler stopped")




from datetime import datetime
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

logger = logging.getLogger(__name__)


class StartupScheduler:

    def __init__(self, startup_service):

        self.startup_service = startup_service

        self.scheduler = AsyncIOScheduler(
            timezone=ZoneInfo("Asia/Kolkata")
        )

    # Run automation
    async def _run_automation(self):

        try:
            print("========== STARTLY AI STARTED ==========")

            await self.startup_service.run_automation()

            print("========== STARTLY AI COMPLETED ==========")

        except Exception:
            logger.exception("Startup automation failed")

    # Start scheduler
    def start(self):

        if self.scheduler.running:
            print("Scheduler is already running")
            return

        self.scheduler.add_job(
            self._run_automation,
            trigger="interval",
            hours=7,
            id="startup_automation",
            replace_existing=True,
            max_instances=1,
            coalesce=True,
            next_run_time=datetime.now(
                ZoneInfo("Asia/Kolkata")
            )
        )

        self.scheduler.start()

        print("Startly AI scheduler started")

    # Stop scheduler
    def shutdown(self):

        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)
            print("Scheduler stopped")
