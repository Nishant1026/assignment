import time
from datetime import datetime

# Store jobs from user input
scheduled_jobs = []

def get_user_input():
    print("\n Schedule a new job:")
    job_type = input("Enter job type (hourly/daily/weekly): ").strip().lower()
    message = input("Enter message to print: ")

    try:
        if job_type == "hourly":
            minute = int(input("At which minute of every hour? (0-59): "))
            if not (0 <= minute <= 59):
                raise ValueError("Minute must be between 0 and 59.")
            job = {"type": "hourly", "minute": minute, "message": message}

        elif job_type == "daily":
            hour = int(input("Enter hour of day (0-23): "))
            minute = int(input("Enter minute of hour (0-59): "))
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Hour must be 0-23 and Minute must be 0-59.")
            job = {"type": "daily", "hour": hour, "minute": minute, "message": message}

        elif job_type == "weekly":
            day_of_week = int(input("Enter day of week (0=Monday, 6=Sunday): "))
            hour = int(input("Enter hour (0-23): "))
            minute = int(input("Enter minute (0-59): "))
            if not (0 <= day_of_week <= 6 and 0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Invalid day/hour/minute values.")
            job = {
                "type": "weekly",
                "day_of_week": day_of_week,
                "hour": hour,
                "minute": minute,
                "message": message
            }

        else:
            print(" Invalid job type. Try again.\n")
            return

        scheduled_jobs.append(job)
        print(" Job scheduled successfully!")
        print(" Current Jobs List:", scheduled_jobs)

    except ValueError as ve:
        print(f" Input Error: {ve}")

def run_job(job):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} - {job['message']}")

def check_jobs():
    while True:
        now = datetime.now()
        for job in scheduled_jobs:
            if job["type"] == "hourly":
                if now.minute == job["minute"] and now.second == 0:
                    run_job(job)

            elif job["type"] == "daily":
                if now.hour == job["hour"] and now.minute == job["minute"] and now.second == 0:
                    run_job(job)

            elif job["type"] == "weekly":
                if (now.weekday() == job["day_of_week"]
                    and now.hour == job["hour"]
                    and now.minute == job["minute"]
                    and now.second == 0):
                    run_job(job)

        # Debug print to show it's checking
        print(f" Checking time: {now.strftime('%H:%M:%S')} | Jobs: {len(scheduled_jobs)}")
        time.sleep(1)

if __name__ == "__main__":
    print(" Welcome to the Job Scheduler!")
    while True:
        get_user_input()
        more = input(" Add more jobs? (y/n): ").strip().lower()
        if more != 'y':
            break

    print("\n Job Scheduler started... Monitoring jobs in real time.\n")
    check_jobs()
