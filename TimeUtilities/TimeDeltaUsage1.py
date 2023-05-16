def apply_delta_to_times(times, minutes_interval):
    import datetime
    updated_times = ""

    times_list = times.split()

    # Add the time interval to each datetime object.
    for time in times_list:
        new_time = datetime.datetime.strptime(
            time, "%H%M") + datetime.timedelta(minutes=minutes_interval)

        # Format the new datetime object and print it out.
        if new_time.hour == 24:
            new_time = datetime.datetime(
                new_time.year, new_time.month, new_time.day, 0, new_time.minute)
        updated_times += " / " + new_time.strftime("%H:%M")
    return updated_times

# entry point

times = "0515 0530 0603 0633 0703 0733 1228 1243 1258 1635 1651 1710 1725 1755 2004 2020 2034 2104 2204 2304 2345 0004"
minutes_interval = -6
updated_times = apply_delta_to_times(times, minutes_interval)
print(updated_times)
