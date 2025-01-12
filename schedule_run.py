import schedule
import time
import tmp

schedule.every(86400).seconds.do(tmp.job)

while True:
    schedule.run_pending()
    time.sleep(1)
