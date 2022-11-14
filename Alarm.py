import datetime
from playsound import playsound
alarm_time = input("Set time alarm time(Format HH:MM:SS and use 24hour format): \n")
message = input("Set the message you want to for alarm: ")
time = alarm_time.split(":")
alarm_hour = time[0]
alarm_minute = time[1]
alarm_second = time[2]
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%X")
    current_time = current_time.split(":")
    current_hour = current_time[0]
    current_minute = current_time[1]
    current_second = current_time[2]
    if (current_hour==alarm_hour):
        if (current_minute==alarm_minute):
            if (current_second==alarm_second):
                print(message)
                playsound("d:\Python\learning\1.m4a")
                break