from django.urls import path

from .views import (
    VacancyHeatMap,
    VacancyProcentHeatMap,
    VipuskHeatMap,
    VipuskProcentHeatMap,

    ProficitDeficitHeatMap,

    RegionDetailed,
)

urlpatterns = [
    path('heat/vacansy/', VacancyHeatMap.as_view()),
    path('heat/vacansyproc/', VacancyProcentHeatMap.as_view()),
    path('heat/vipusk/', VipuskHeatMap.as_view()),
    path('heat/vipuskproc/', VipuskProcentHeatMap.as_view()),

    path('heat/tendency/', ProficitDeficitHeatMap.as_view()),
    
    path('regions/', RegionDetailed.as_view()),
]
