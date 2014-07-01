from datetime import datetime, timedelta
from time import sleep

second = timedelta(seconds=1)
day = timedelta(days=1)

class Increment:
    def __init__(self):
        self.last_second_count = 0
        self.last_day_count = 0
        self.seconds_now = datetime.now()
        self.days_now = datetime.now()
        
    def increment(self):
        now = datetime.now()

        if (now - self.seconds_now) >= second:
            self.last_second_count = 1
            self.seconds_now = now
        else:
            self.last_second_count += 1

        if (now - self.days_now) >= day:
            self.last_day_count = 1
            self.days_now = now
        else:
            self.last_day_count += 1
        

    def get_events_last_second(self):
        return self.last_second_count

    def get_events_last_day(self):
        return self.last_day_count

i = Increment()

for j in range(100):
    sleep(0.01)
    i.increment()

print i.get_events_last_day()
print i.get_events_last_second()
