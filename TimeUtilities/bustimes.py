# Bard version
trip = "Route 57 - Hospital Corner - direction Brixington - Sunday and Bank holiday"
original_times = ''.join(['0839 0909 0942 1014 1044 1114 1144 1214 1244 1314 1344 1414 1444 1513 1542 1612 1642 1712 1742 1812',
#                 ' 1132 1147 1202 1217 1232 1247 1302 1317 1332 1347 1402 1417 1432 1447 1502 1516 1534 1555 1610 1630',
                 ' 1837 1934 2034 2134 2234 2334'])

minutes_to_add = +3 #sic - todo - add test for positive minutes

# Split the input string into individual times
time_list = original_times.split()

# Subtract n minutes from each time and format the output
result = []
for time in time_list:
    hour = int(time[:2])
    minute = int(time[2:])
    minute += minutes_to_add
    if minute < 0:
        minute += 60
        hour -= 1
        if hour < 0:
            hour += 24
    if minute >= 60:
        minute = minute%60
        hour += 1
    result.append(f"{hour:02d}{minute:02d}")
print(trip)
# Join the updated times with space-forward slash-space ("/")
updated_times = " / ".join(result)
print(updated_times)


