from datetime import datetime, timedelta

# # Get the current date
# today = datetime.now()
#
# current_monday = today - timedelta(days=(today.weekday() - 0) % 7)
#
# current_saturday = today + timedelta(days=(5 - today.weekday() + 7) % 7)
#
# next_monday = current_monday + timedelta(days=7)
#
# next_saturday = current_saturday + timedelta(days=7)
#
# monday = datetime.strptime(str(today.replace(day=current_monday.day, hour=5, minute=0, microsecond=0, second=0)),
#                                "%Y-%m-%d %H:%M:%S").timestamp()
#
# current_monday_str = current_monday.strftime("%Y-%m-%d")
# current_saturday_str = current_saturday.strftime("%Y-%m-%d")
# next_monday_str = next_monday.strftime("%Y-%m-%d")
# next_saturday_str = next_saturday.strftime("%Y-%m-%d")
#
# # Print the dates
# print("This week's Monday:", current_monday_str)
# print("This week's Saturday:", current_saturday_str)
# print("Next week's Monday:", next_monday_str)
# print("Next week's Saturday:", next_saturday_str)
#
#
# monday = datetime.strptime(str(today.replace(day=current_monday.day, hour=5, minute=0, microsecond=0, second=0)),
#                            "%Y-%m-%d %H:%M:%S").timestamp()
# saturday = datetime.strptime(str(today.replace(day=current_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
#                              "%Y-%m-%d %H:%M:%S").timestamp()
#
#
# nextmonday = datetime.strptime(str(today.replace(day=next_monday.day, hour=5, minute=0, microsecond=0, second=0)),
#                                "%Y-%m-%d %H:%M:%S").timestamp()
# nextsaturday = datetime.strptime(str(today.replace(day=next_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
#                                  "%Y-%m-%d %H:%M:%S").timestamp()
#
# print(nextmonday)
# print(nextsaturday)
# print(monday)
# print(saturday)
#


# today = datetime.now()
#
# current_monday = today - timedelta(days=(today.weekday() - 0) % 7)
#
# current_saturday = today + timedelta(days=(5 - today.weekday() + 7) % 7)
#
# next_monday = current_monday + timedelta(days=7)
#
# next_saturday = current_saturday + timedelta(days=7)
#
# monday = datetime.strptime(str(current_monday.replace(day=current_monday.day, hour=5, minute=0, second=0, microsecond=0)),
#                            "%Y-%m-%d %H:%M:%S").timestamp()
#
# saturday = datetime.strptime(str(current_saturday.replace(day=current_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
#                              "%Y-%m-%d %H:%M:%S").timestamp()
#
# nextmonday = datetime.strptime(str(next_monday.replace(day=next_monday.day, hour=5, minute=0, microsecond=0, second=0)),
#                                "%Y-%m-%d %H:%M:%S").timestamp()
# nextsaturday = datetime.strptime(str(next_saturday.replace(day=next_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
#                                  "%Y-%m-%d %H:%M:%S").timestamp()

today = datetime.now()  # Replace this with your preferred method of getting the current date


utc_time = datetime.utcfromtimestamp(float('1701388800')).strftime("%Y-%m-%d")
print(utc_time)