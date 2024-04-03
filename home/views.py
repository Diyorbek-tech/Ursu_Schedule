import json

from django.shortcuts import render
import requests

from datetime import datetime, timedelta

# Create your views here.
from decouple import config

Faculties = []
url = f"https://student.urdu.uz/rest/v1/data/department-list/?_structure_type=11"
payload = {
}
headers = {
    'Authorization': config('API_KEY'),
    'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)

for i in response.json()["data"]["items"]:
    if i['id'] not in [77, 8, 7, 6]:
        Faculties.append(i)


def get_fac_name(id):
    for i in Faculties:
        if i['id'] == id:
            return i['name']


def get_group_name(id):
    url2 = f"https://student.urdu.uz/rest/v1/data/group-list/?id={id}"
    group = requests.request("GET", url2, headers=headers, data=payload).json()["data"]["items"]
    return group[0]['name']


def facultiesview(request):
    return render(request, 'Faculties.html', {"flist": reversed(Faculties)})


def homeview(request):
    context = {
        'date': datetime.now().strftime("%d-%m-%Y"),
    }
    return render(request, 'index.html', context)


def coursesview(request, parent):
    name = get_fac_name(parent)

    kurslar = [1, 2, 3, 4, 5]
    if parent == 76:
        kurslar = [1, 2]
    context = {
        'id': parent,
        "kurslar": kurslar,
        'f_name': name
    }
    return render(request, 'courses.html', context)


def curriculumview(request, deportment, year):
    fname = get_fac_name(deportment)
    k_name = f"{year}-Kurs"

    groups = []
    now = datetime.now()
    ye = now.year - year
    if now.month >= 9 and now.month <= 12:
        ye = now.year - year + 1

    url = f"https://student.urdu.uz/rest/v1/data/curriculum-list/?limit=50&_department={deportment}&_education_year={ye}"
    payload = {
    }
    headers = {
        'Authorization': config('API_KEY'),
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
        "curriculum_list": response,
        "groups_list": response2,
        'fname': fname,
        'k_name': k_name,

    }

    return render(request, 'curriculum.html', context)


def get_daily_schedule(response):
    global lesson_date
    schedule_list = []

    dates = [i['lesson_date'] for i in response]
    dates = set(dates)
    dates = list(dates)
    dates.sort()
    try:
        for day in dates:
            todays_lesson = [i for i in response if i['lesson_date'] == day]
            todays_lesson.sort(key=lambda i: i['lessonPair']['code'])
            schedule_list.append(todays_lesson)
        return schedule_list
    except Exception as e:
        return []
    # try:
    #
    #     lesson_date = response[0]['lesson_date']
    # except Exception as e:
    #     print(str(e))
    # for i in response:
    #     datetime_obj = datetime.fromtimestamp(i['lesson_date']).strftime('%Y-%m-%d')
    #     todays_lesson = [i for j in i]
    #     if i['lesson_date'] != lesson_date:
    #         schedule_list.append(lesson_day_by.copy())
    #         lesson_day_by.clear()
    #         date_list.append(datetime_obj)
    #     lesson_day_by.append(i)
    #
    #     lesson_date = i['lesson_date']
    #     print(lesson_day_by)
    # else:
    #     schedule_list.append(lesson_day_by.copy())
    #     date_list.append(datetime_obj)
    #     print(schedule_list)

    # return schedule_list


def scheduleview(request, deportment, year, group):
    fname = get_fac_name(deportment)
    k_name = f"{year}-Kurs"
    getgrname = get_group_name(group)

    today = datetime.now()

    current_monday = today - timedelta(days=(today.weekday() - 0) % 7)

    current_saturday = today + timedelta(days=(5 - today.weekday() + 7) % 7)

    next_monday = current_monday + timedelta(days=7)

    next_saturday = current_saturday + timedelta(days=7)

    monday = datetime.strptime(
        str(current_monday.replace(day=current_monday.day, hour=5, minute=0, second=0, microsecond=0)),
        "%Y-%m-%d %H:%M:%S").timestamp()

    saturday = datetime.strptime(
        str(current_saturday.replace(day=current_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
        "%Y-%m-%d %H:%M:%S").timestamp()

    nextmonday = datetime.strptime(
        str(next_monday.replace(day=next_monday.day, hour=5, minute=0, microsecond=0, second=0)),
        "%Y-%m-%d %H:%M:%S").timestamp()
    nextsaturday = datetime.strptime(
        str(next_saturday.replace(day=next_saturday.day, hour=5, minute=0, microsecond=0, second=0)),
        "%Y-%m-%d %H:%M:%S").timestamp()

    url = f"https://student.urdu.uz/rest/v1/data/schedule-list?_faculty={deportment}&_group={group}&lesson_date_from={monday}&lesson_date_to={saturday}"
    url2 = f"https://student.urdu.uz/rest/v1/data/schedule-list?_faculty={deportment}&_group={group}&lesson_date_from={nextmonday}&lesson_date_to={nextsaturday}"
    payload = {
    }
    headers = {
        'Authorization': config('API_KEY'),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    responsenext = requests.request("GET", url2, headers=headers, data=payload)

    response = response.json()['data']['items']
    responsenext = responsenext.json()['data']['items']

    context = {

        "schedule_list": get_daily_schedule(response),
        "schedule_next_list": get_daily_schedule(responsenext),
        'fname': fname,
        'k_name': k_name,
        'g_name': getgrname,
    }

    return render(request, 'schedule.html', context)


def get_exams_data(data, type_code):
    dict_response = {}
    count = 0

    for i in data:

        utc_time = datetime.utcfromtimestamp(float(i["examDate"])).strftime("%Y-%m-%d")
        fan = i["subject"]["name"]

        if i["finalExamType"]["code"] == str(type_code) and i["examType"]["code"] == "12":
            dict_response[str(count)] = {
                "fan": fan,
                "date": str(utc_time),
                "boshlash": i["lessonPair"]["start_time"],
                "xona": i["auditorium"]["name"],
                "oqituvchi": i["employee"]["name"],
            }

            for value in data:
                fan2 = value["subject"]["name"]
                if fan2 == fan and value["examType"]["code"] == "13":
                    utc_time2 = datetime.utcfromtimestamp(float(value["examDate"])).strftime("%Y-%m-%d")
                    dict_response[str(count)].update({
                        "date2": str(utc_time2),
                        "boshlash2": value["lessonPair"]["start_time"],
                        "xona2": value["auditorium"]["name"],
                        "oqituvchi2": value["employee"]["name"]
                    })
        count += 1
    print(json.dumps(dict_response))
    return dict_response


def nazoratlarview(request, deportment, year, group):
    fname = get_fac_name(deportment)
    k_name = f"{year}-Kurs"
    getgrname = get_group_name(group)

    url1 = f"https://student.urdu.uz/rest/v1/data/exam-list?_faculty={deportment}&_group={group}"

    response1 = requests.request("GET", url1, headers=headers, data=payload).json()['data']['items']

    context = {
        'asosiyq': get_exams_data(response1, 11),
        'ikkinchiq': get_exams_data(response1, 12),
        'uchunchiq': get_exams_data(response1, 13),
        'fname': fname,
        'k_name': k_name,
        'g_name': getgrname,
    }

    return render(request, 'nazoratlar.html', context)
