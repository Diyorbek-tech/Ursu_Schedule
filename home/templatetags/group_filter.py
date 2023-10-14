from datetime import datetime

import requests
from django import template

register = template.Library()


@register.filter
def get_group(obj,group_list):


    print(group_list)
    groups = []
    url = f"https://student.urdu.uz/rest/v1/data/group-list?limit=50&_curriculum={obj}"
    payload = {
    }
    headers = {
        'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
        'Content-Type': 'application/json'
    }
    response2 = requests.request("GET", url, headers=headers, data=payload)
    response2 = response2.json()['data']['items']
    for i in response2:
        groups.append(i)
    return groups


@register.filter()
def get_week_day(li):
    unix_date = li[0]['lesson_date']
    print(unix_date)
    week_days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]

    try:
        dt_object = datetime.fromtimestamp(int(unix_date))
        human_date = int(dt_object.strftime("%w"))
        today = int(datetime.now().weekday()) + 1
        if today == human_date:
            a = week_days[human_date - 1]
            print(a)
            week_days.remove(a)
            print(week_days)
            week_days.insert(today-1,"1"+a)
            print(week_days)
        return week_days[human_date - 1]
    except ValueError:
        pass
