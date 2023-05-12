trip = "Route 57 - Hospital Corner to Exeter - Monday / Friday"
times = "0515 0530 0603 0633 0703 0733 0813 0830 0840 0855 0925 0940 0953 1008 1027 1043 1058 1113 1128 1143 1158 1213 1228 1243 1258 1313 1328 1343 1358 1413 1428 1443 1458 1528 1553 1557 1614 1630 1635 1651 1710 1725 1755 1805 1822 1845 1855 1902 1912 1916 1940 1954 2004 2020 2034 2104 2204 2304 2345 0004"
# minutes_to_add = -6 #sic

# Split the input string into individual times
time_list = times.split()

# Subtract 6 minutes from each time and format the output
result = [f"{int(time[:2]):02d}{int(time[2:])-6:02d}" for time in time_list]

# Join the updated times with space-forward slash-space ("/")
updated_times = " / ".join(result)

print(trip)
print(updated_times)

# times = ''.join(['0515 0530 0603 0633 0703 0733 0813 0830 0840 0855 0925 0940 0953 1008 1027 1043 1058 1113 1128 1143',
#                  ' 1158 1213 1228 1243 1258 1313 1328 1343 1358 1413 1428 1443 1458 1528 1553 1557 1614 1630 1635 1651',
#                  ' 1710 1725 1755 1805 1822 1845 1855 1902 1912 1916 1940 1954 2004 2020 2034 2104 2204 2304 2345 0004'])