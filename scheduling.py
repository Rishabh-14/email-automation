import schedule
import time

def my_job():
    print("Job is running...")

# Schedule the job to run every minute
schedule.every(1).minutes.do(my_job)

while True:
    schedule.run_pending()
    time.sleep(1)
