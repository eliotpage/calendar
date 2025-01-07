def init(year):
    import json
    f = open('calendar.json')

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        month_lengths.insert(1, 29)
        

    current_year = []

    for index, month in enumerate(month_lengths):
        days = []
        for day in range(month):
            days.append({f'{day+1}/{index+1}':[]})
        current_year.append(days)

    json.dump(current_year, f)
    f.close()