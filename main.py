import time
import os 
import json
from setup import init

year = 2025

months = ['January', 'Februrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Event:
        def __init__(self, date, time):
            self.date = date
            self.time = time

def update(day, month, event_time, name):
    f = open('calendar.txt', 'w')
    calendar = json.loads(f.read())
    selected = calendar[month-1][day-1]
    new = (list(selected.values())[0])
    new.append({event_time:name})
    calendar[month-1].remove(selected)
    calendar[month-1].insert(day, {f"{day}/{month}":new})
    json.dump(calendar, f)
    f.close()
    print(f"Added {name} at {event_time} on {day}/{month}.")
    time.sleep(3)
    os.system('clear')
    


if __name__ == "__main__":
    print(f"Current time: {time.ctime()}\n")
    while True:
        valid = True
        new_event = input("Enter new event title, 'exit' to save calendar, or 'reset' to reset the calendar: ")
        if new_event.lower() == 'exit':
            f = open('calendar.txt')
            calendar = json.loads(f.read())
            f.close()
            os.system('clear')
            print("Current calendar:\n")
            for i, month in enumerate(months):
                print(f'\n{month}')
                for day in calendar[i]:
                    if len(list(day.values())[0]) > 0:
                        print(f"{list(day.keys())[0]}: {list(day.values())[0]}")
            break
        elif new_event.lower() == 'reset':
            init(year)
            os.system('clear')
            break
        else:
            date = input("Enter date of event in the format (day)/(month): ")
            try:
                day = int(date.split('/')[0])
                month = int(date.split('/')[1])
                event_time = input("Enter time of event in format (hours):(minutes): ")
                try:
                    hours = int(event_time.split(':')[0])
                    minutes = int(event_time.split(':')[1])
                except:
                    print("Invalid format.")
                    time.sleep(2)
                    os.system('clear')
                    valid = False
            except:
                print("Invalid format.")
                time.sleep(2)
                os.system('clear')
                valid = False
        
        if valid:
            update(day, month, event_time, new_event)
