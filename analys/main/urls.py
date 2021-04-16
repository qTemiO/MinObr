from django.urls import path

from .views import (
    VacancyHeatMap,
    VipuskHeatMap,
)

urlpatterns = [
    path('heat/vacansy/', VacancyHeatMap.as_view()),
    path('heat/vipusk/', VipuskHeatMap.as_view()),
]
