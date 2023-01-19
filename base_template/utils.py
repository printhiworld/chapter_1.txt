import json
from datetime import datetime


def load_raspisanie():
    """
    загружает данные из файла  json
    :return: list
    """
    with open('data2.json', 'r', encoding='utf-8') as raspisanie:
        data = json.load(raspisanie)
        return data


def search_by_lesson(lesson):
    """
    ищет дисциплины по вхождению слова в название
    :param lesson: str
    :return:
    """
    days_with_lesson = []
    for day in load_raspisanie():
        if day['discipline'].find(lesson) >= 0:
            days_with_lesson.append(day)
    return days_with_lesson



def next_day():
    """
    находит расписание на определенный день
    :return: дшые
    """
    data = load_raspisanie()
    days_next_lesson = []
    day_now = datetime.weekday(datetime.now())
    day_after = day_now + 1
    if day_after == 0:
        for day in data:
            if day['day_week'] == 'пн':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_after == 1:
        for day in data:
            if day['day_week'] == 'вт':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_after == 2:
        for day in data:
            if day['day_week'] == 'ср':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_after == 3:
        for day in data:
            if day['day_week'] == 'чт':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_after == 4:
        for day in data:
            if day['day_week'] == 'пт':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_after == 5:
        for day in data:
            if day['day_week'] == 'сб':
                days_next_lesson.append(day)
        return days_next_lesson
    elif day_now == 6:
        for day in data:
            if day['day_week'] == 'пн':
                days_next_lesson.append(day)
        return days_next_lesson





