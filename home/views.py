from django.shortcuts import render
import requests

from datetime import datetime


# Create your views here.


def facultiesview(request):
    Faculties = []
    url = f"https://student.urdu.uz/rest/v1/data/department-list/?_structure_type=11"

    payload = {
    }
    headers = {
        'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # pageCount = response.json()['data']['pagination']['pageCount']
    for i in response.json()["data"]["items"]:
        if i['id'] not in [77, 8, 7, 6]:
            Faculties.append(i)

    return render(request, 'Faculties.html', {"flist": reversed(Faculties)})


def homeview(request):
    context = {
        'date': datetime.now().strftime("%d-%m-%Y"),
    }
    return render(request, 'index.html', context)


def coursesview(request, parent):
    kurslar = [1, 2, 3, 4, 5]
    if parent == 76:
        kurslar = [1, 2]
    context = {
        'id': parent,
        "kurslar": kurslar,
    }
    return render(request, 'courses.html', context)


def curriculumview(request, deportment, year):
    groups = []
    now = datetime.now()
    ye = now.year - year
    if now.month >= 9 and now.month <= 12:
        ye = now.year - year + 1

    url = f"https://student.urdu.uz/rest/v1/data/curriculum-list/?limit=50&_department={deportment}&_education_year={ye}"
    payload = {
    }
    headers = {
        'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()['data']['items']


    url2 = f"https://student.urdu.uz/rest/v1/data/group-list?limit=500&_department={deportment}"

    response2 = requests.request("GET", url2, headers=headers, data=payload)
    response2 = response2.json()['data']['items']


    context = {
        'year': year,
        'dep': deportment,
        "curriculum_list": reversed(response),
        "groups_list": reversed(response2),

    }

    return render(request, 'curriculum.html', context)


def get_daily_schedule(response):
    schedule_list = []
    date_list = []

    lesson_day_by = []
    datetime_obj = ""
    try:

        lesson_date = response[0]['lesson_date']
    except Exception as e:
        print(str(e))
    for i in response:
        datetime_obj = datetime.fromtimestamp(i['lesson_date']).strftime('%Y-%m-%d')
        if i['lesson_date'] != lesson_date:
            schedule_list.append(lesson_day_by.copy())
            lesson_day_by.clear()
            date_list.append(datetime_obj)
        lesson_day_by.append(i)

        lesson_date = i['lesson_date']
    else:
        schedule_list.append(lesson_day_by.copy())
        date_list.append(datetime_obj)

    return schedule_list


def scheduleview(request, deportment, year, group):
    today = datetime.now()
    m = today.day - today.weekday()
    monday = datetime.strptime(str(today.replace(day=m, hour=5, minute=0, microsecond=0, second=0)),
                               "%Y-%m-%d %H:%M:%S").timestamp()
    s = m + 5
    saturday = datetime.strptime(str(today.replace(day=s, hour=5, minute=0, microsecond=0, second=0)),
                                 "%Y-%m-%d %H:%M:%S").timestamp()

    nextmonday = datetime.strptime(str(today.replace(day=m + 7, hour=5, minute=0, microsecond=0, second=0)),
                                   "%Y-%m-%d %H:%M:%S").timestamp()
    nextsaturday = datetime.strptime(str(today.replace(day=s + 7, hour=5, minute=0, microsecond=0, second=0)),
                                     "%Y-%m-%d %H:%M:%S").timestamp()

    url = f"https://student.urdu.uz/rest/v1/data/schedule-list?_faculty={deportment}&_group={group}&lesson_date_from={monday}&lesson_date_to={saturday}"
    url2 = f"https://student.urdu.uz/rest/v1/data/schedule-list?_faculty={deportment}&_group={group}&lesson_date_from={nextmonday}&lesson_date_to={nextsaturday}"
    payload = {
    }
    headers = {
        'Authorization': 'Bearer t9n6KJ9sgXhyI9A8cqXxOhuUlK6V5eHV',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    responsenext = requests.request("GET", url2, headers=headers, data=payload)

    response = response.json()['data']['items']
    responsenext = responsenext.json()['data']['items']

    context = {

        "schedule_list": get_daily_schedule(response),
        "schedule_next_list": get_daily_schedule(responsenext)
    }

    return render(request, 'schedule.html', context)

#    filterlar    id:   77,8,7,6
