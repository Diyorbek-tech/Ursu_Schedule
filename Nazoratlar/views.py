from datetime import datetime

from django.shortcuts import render
from decouple import config
import requests


def nazoratlarview(request, deportment, year, group):
    Exams = {}

    url = f"https://student.urdu.uz/rest/v1/data/exam-list?_faculty={deportment}&_group={group}"

    payload = {
    }
    headers = {
        'Authorization': config('API_KEY'),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    count = 0
    for i in response.json()["data"]["items"]:
        utc_time = datetime.utcfromtimestamp(float(i["examDate"])).strftime("%Y-%m-%d")
        Exams[f"{count}"] = {
            "fan": i["subject"]['name'],
            "semester": i["semester"]['name'],
            "type": i["examType"]["name"],
            "oqituvchi": i["employee"]['name'],
            "xona": i["auditorium"]['name'],
            "boshlash": i["lessonPair"]['start_time'],
            "tugash": i["lessonPair"]['end_time'],
            "date": str(utc_time),
        }
        count += 1


    return render(request, 'nazoratlar.html', {"exams": Exams})
