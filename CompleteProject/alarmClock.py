import datetime

def alarm_clock():
    alarm_time = input("Enter time (H:S): ")
    message = input("Enter any message: ")

    
    print(f"⏰ Alarm set for {alarm_time}...")


    while True:

      now = datetime.datetime.now().strftime("%H:%M")

      if now == alarm_time:
        print(f"🔔 {message}")
        break


alarm_clock()