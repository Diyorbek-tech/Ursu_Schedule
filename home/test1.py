# import requests
#
# url = f"https://student.urdu.uz/rest/v1/data/department-list"
#
# payload = {}
# headers = {
#     'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
#     'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# pageCount = response.json()['data']['pagination']['pageCount']
# for i in response.json()["data"]["items"]:
#     for j in  range(pageCount):
#         print(i['name'])
# import datetime
#
# year= datetime.datetime.now()
#
# year=year.year-2
#
#
# print(year)
import datetime
import time

import requests

# kurs=2
# year = datetime.datetime.now().year - kurs
# url = f"https://student.urdu.uz/rest/v1/data/curriculum-list/?_education_year={year}"
# payload = {
# }
# headers = {
#     'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
#     'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
#
# response=response.json()['data']['items']
#
# print(response)

# faculty=2
# group=1970
#
#
# url = f"https://student.urdu.uz/rest/v1/data/schedule-list?_faculty={faculty}&_group={group}"
# payload = {
# }
# headers = {
#     'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
#     'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
#
# response = response.text
# print(response)
#
# today = datetime()
#
# print(datetime.datetime.now().isoweekday())
#
# print(today)
#
# unix_vaqt = time.mktime(today.timetuple())
# print(unix_vaqt)

#
# for i in range(len(response)):
#     url = f"https://student.urdu.uz/rest/v1/data/group-list?_department={deportment}&_curriculum={response[i]['id']}"
#     response2 = requests.request("GET", url, headers=headers, data=payload)
#     response2 = response2.json()['data']['items']
#     print(response2)




# url = f"https://student.urdu.uz/rest/v1/data/group-list?_department={deportment}&_curriculum={cur}"
# payload = {
# }
# headers = {
#     'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
#     'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
#
# response = response.json()['data']['items']
#
# print(response[0]['name'])


# import time
#
# # Joriy vaqtni olish
# joriy_vaqt = time.time()
# print(joriy_vaqt)
# # Unix vaqtga o'tkazish
# haftaning_boshi_unix = joriy_vaqt - (joriy_vaqt % 604800)  # 604800 sekund 1 haftaga teng
#
# print(haftaning_boshi_unix)


#

#
# from datetime import datetime
#
# today = datetime.now()
# m=today.day-today.weekday()
# monday = datetime.strptime(str(today.replace(day=m,hour=5,minute=0,microsecond=0,second=0)), "%Y-%m-%d %H:%M:%S").timestamp()
# s=m+5
# saturday=datetime.strptime(str(today.replace(day=s,hour=5,minute=0,microsecond=0,second=0)), "%Y-%m-%d %H:%M:%S").timestamp()
#
# print(int(monday),int(saturday))
# print('1696809600')

from datetime import datetime

# Unix timestamp (in seconds)
unix_timestamp = 1634082053  # Replace with your timestamp

# Convert Unix timestamp to a datetime object
dt_object = datetime.fromtimestamp(unix_timestamp)

# Format the datetime object as a string
human_date = dt_object.strftime("%u")  # Adjust the format as needed
print(human_date)

#
# deportment=2
# year=1
# now = datetime.datetime.now()
# ye = now.year - year
# if now.month >= 9 and now.month <= 12:
#     ye = now.year - year + 1
#
# url = f"https://student.urdu.uz/rest/v1/data/curriculum-list/?_department={deportment}&_education_year={ye}"
# payload = {
# }
# headers = {
#     'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
#     'Content-Type': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# response = response.json()['data']['items']
# print(response)