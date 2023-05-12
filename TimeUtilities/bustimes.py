trip = "Route 57 - Hospital Corner to Exeter - Monday / Friday"
original_times = ''.join(['0515 0530 0603 0633 0703 0733 0813 0830 0840 0855 0925 0940 0953 1008 1027 1043 1058 1113 1128 1143',
                 ' 1158 1213 1228 1243 1258 1313 1328 1343 1358 1413 1428 1443 1458 1528 1553 1557 1614 1630 1635 1651',
                 ' 1710 1725 1755 1805 1822 1845 1855 1902 1912 1916 1940 1954 2004 2020 2034 2104 2204 2304 2345 0004'])

minutes_to_add = -6 #sic - todo - add test for positive minutes

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
    result.append(f"{hour:02d}{minute:02d}")
print(trip)
# Join the updated times with space-forward slash-space ("/")
updated_times = " / ".join(result)
print(updated_times)

# sample of expected result given above original_times and minutes_to_add values
# 0509 / 0524 / 0557 / 0627 / 0657 / 0727 / 0807 / 0824 / 0834 / 0849 / 0919 / 0934 / 0947 / 1002 / 
# 1021 / 1037 / 1052 / 1107 / 1122 / 1137 / 1152 / 1207 / 1222 / 1237 / 1252 / 1307
