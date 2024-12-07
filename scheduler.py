#creating a funciton to be run on a specific time
import sched
import time

def schedule_function (start_time, function, priority = 1, *args):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(start_time, priority, function, argument=args)
    scheduler.run()

# calling the shceduler function
schedule_function(time.time() + 5, print, 1, "Hello World!!")