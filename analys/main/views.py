from django.shortcuts import render

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
from .models import (

)
"""
class VacancyHeatMap(APIView):
    """Вакансии по регионам с hh"""
    
    renderer_classes = [JSONRenderer]

    def get(self, request):
        data = {
            'Россия':104694,
            'Москва':35815,
            'Санкт-Петербург':12981,
            'Новосибирская область':3642,
            'Свердловская область':3529,
            'Краснодарский край':3403,
            'Республика Татарстан':3344,
            'Московская область':2760,
            'Нижегородская область':2728,
            'Ростовская область':2495,
            'Самарская область':2227,
            'Воронежская область':1989,
            'Пермский край':1581,
            'Челябинская область':1414,
            'Республика Башкортостан':1409,
            'Саратовская область':1105,
            'Красноярский край':1095,
            'Волгоградская область':969,
            'Приморский край':811,
            'Томская область':809,
            'Удмуртская Республика':807,
            'Ярославская область':807,
            'Омская область':800,
            'Тюменская область':788,
            'Иркутская область':780,
            'Ульяновская область':744,
            'Кемеровская область':739,
            'Тульская область':709,
            'Алтайский край':666,
            'Ставропольский край':646,
            'Республика Крым':574,
            'Калининградская область':567,
            'Тверская область':554,
            'Пензенская область':527,
            'Владимирская область':525,
            'Рязанская область':514,
            'Хабаровский край':501,
            'Белгородская область':497,
            'Калужская область':491,
            'Чувашская Республика':480,
            'Кировская область':471,
            'Оренбургская область':449,
            'Вологодская область':428,
            'Ханты-Мансийский АО - Югра':364,
            'Липецкая область':356,
            'Ивановская область':341,
            'Курская область':331,
            'Харьковская область':315,
            'Ленинградская область':303,
            'Смоленская область':290,
            'Брянская область':287,
            'Республика Марий Эл':267,
            'Тамбовская область':258,
            'Орловская область':256,
            'Костромская область':239,
            'Республика Мордовия':224,
            'Архангельская область':218,
            'Астраханская область':205,
            'Республика Дагестан':182,
            'Курганская область':180,
            'Амурская область':163,
            'Новгородская область':162,
            'Мурманская область':162,
            'Ямало-Ненецкий АО':162,
            'Республика Карелия':157,
            'Республика Коми':153,
            'Псковская область':141,
            'Республика Бурятия':141,
            'Республика Саха (Якутия)':119,
            'Забайкальский край':111,
            'Республика Хакасия':110,
            'Сахалинская область':89,
            'Камчатский край':78,
            'Кабардино-Балкарская республика':71,
            'Республика Северная Осетия-Алания':68,
            'Чеченская республика':55,
            'Карачаево-Черкесская Республика':50,
            'Республика Адыгея':48,
            'Республика Калмыкия':48,
            'Республика Тыва':40,
            'Магаданская область':33,
            'Республика Алтай':21,
            'Республика Ингушетия':19,
            'Еврейская АО':17,
            'Севастополь':0
            }
        return Response(data=data)

class VipuskHeatMap(APIView):
    """Список по выпускникам"""

    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        data = {
            'Ростовская область': 1315,
            'Республика Башкоргостан': 1269,
            'Сарская область': 1121,
            'Новосибирская область': 958,
            'Воронеж область': 931,
            'Республика Татарстан ': 867,
            'Свердловская область': 840,
            'Челябинская область': 114,
            'Пензенская область': 732,
            'Нижегородский регион': 678,
            'Саратовская область': 626,
            'Краснодарский край': 522,
            'Алтайский край': 545,
            'Пермский край ': 460,
            'Омская область': 448,
            'Республика Карелия ': 444,
            'Курская область': 439,
            'Томская область': 399,
            'Приморский край': 353,
            'Брянская область': 339,
            'Иркутская область': 326,
            'Оренбургская область': 326,
            'Ставропольский край': 319,
            'Республика Дагестан': 317,
            'Орловская область': 310,
            'Республика Бурятия': 280,
            'Кемеровская область': 221,
            'Владимирская область': 277,
            'Тамбовская область': 275,
            'Удмурская республика': 266,
            'Севастопольский регион ': 251,
            'Тульская область': 250,
            'Волгоградская область': 237,
            'Архангельская область': 226,
            'Республика Марий Эл': 221,
            'Республика крым': 220,
            'Ярославская область': 217,
            'Республика Кабардино-Балкария ': 207,
            'Ивановская область': 182,
            'Республика Мордовия': 182,
            'Республика Адыгея': 175,
            'Тюменская область': 169,
            'Астраханская область': 164,
            'Белгородская область': 152,
            'Хабаровский край': 147,
            'Вологодская область': 42,
            'Самарская область': 136,
            'Ульяновская область': 128,
            'Республика Саха': 127,
            'Хабаровкий край': 116,
            'Костромская область': 111,
            'Республикаа Карачаево-Черкесия ': 206,
            'Псковская область': 96,
            'Республика Коми': 125,
            'Тверская область': 93,
            'Ханты-Мансийский Автономный округ': 111,
            'Амурская область': 83,
            'Забайкальский край': 68,
            'Липецкая область': 64,
            'Республика Северная Осетия - Аланяи ': 61,
            'Курганская область': 60,
            'Калужская область': 57,
            'Республика Ингушетия ': 55,
            'Еврейская автономная область': 52,
            'Рязанская область': 46,
            'Новгородская область': 28,
            'Сахалинская область': 20,
            'Магаданская область': 18,
            'Камчатский край': 13,
            'Республика Тыва ': 12
        }
        return Response(data=data)
