import datetime
import time
import os

alarm_time = input("Enter the alarm time (HH:MM): ")
alarm_song = input("Enter the path to the alarm song: ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        os.startfile(alarm_song)
        print("Wake up! Alarm song is playing...")
        break
    else:
        time.sleep(1)

snooze_time = input("Press 's' to snooze or 'x' to turn off the alarm: ")
if snooze_time == "s":
    snooze_time = int(input("Enter snooze time in minutes: "))
    time.sleep(snooze_time*60)
    os.startfile(alarm_song)
    print("Wake up! Alarm song is playing...")
elif snooze_time == "x":
    print("Alarm turned off.")
