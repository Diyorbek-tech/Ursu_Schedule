from datetime import datetime

from django import template

register = template.Library()


@register.filter
def get_curriculum(educationFormcode: int, curriculum_list: list):
    curriculum_list.reverse()
    curriculums = []
    try:
        if educationFormcode == 15:
            for i in curriculum_list:
                if i['educationForm']['code'] == str(educationFormcode) or i['educationForm']['code'] == 18 or \
                        i['educationForm']['code'] == 19:
                    curriculums.append(i)
        else:
            for i in curriculum_list:
                if i['educationForm']['code'] == str(educationFormcode):
                    curriculums.append(i)

    except ValueError:
        pass
    finally:
        return curriculums


@register.filter
def get_group(obj, group_list):
    groups = []
    try:
        for i in group_list:
            if i['_curriculum'] == obj:
                groups.append(i)
    except ValueError:
        pass
    return groups


@register.filter()
def get_week_day(li: list):
    try:
        if len(li) >= 1:
            unix_date = li[0]['lesson_date']
            week_days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
            dt_object = datetime.fromtimestamp(int(unix_date))
            human_date = int(dt_object.strftime("%w"))
            today = int(datetime.now().weekday()) + 1
            if today == human_date:
                a = week_days[human_date - 1]
                week_days.remove(a)
                week_days.insert(today - 1, "1" + a)
            return week_days[human_date - 1]
    except ValueError:
        pass
