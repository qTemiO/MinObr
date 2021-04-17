from django.urls import path

from .views import (
    VacancyHeatMap,
    VacancyProcentHeatMap,
    VipuskHeatMap,
    VipuskProcentHeatMap,

    ProficitDeficitHeatMap,

    RegionDetailed,

    FirstYear,
    SecondYear,
    ThirdYear,
    FourthYear,
    FifthYear,
    SixYear,
    SeventhYear,
    EigthYear,
    NinethYear,
    TenthYear,
)

urlpatterns = [
    path('heat/vacansy/', VacancyHeatMap.as_view()),
    path('heat/vacansyproc/', VacancyProcentHeatMap.as_view()),
    path('heat/vipusk/', VipuskHeatMap.as_view()),
    path('heat/vipuskproc/', VipuskProcentHeatMap.as_view()),

    path('heat/tendency/', ProficitDeficitHeatMap.as_view()),
    
    path('regions/', RegionDetailed.as_view()),

    path('y1/', FirstYear.as_view()),
    path('y2/', SecondYear.as_view()),
    path('y3/', ThirdYear.as_view()),
    path('y4/', FourthYear.as_view()),
    path('y5/', FifthYear.as_view()),
    path('y6/', SixYear.as_view()),
    path('y7/', SeventhYear.as_view()),
    path('y8/', EigthYear.as_view()),
    path('y9/', NinethYear.as_view()),
    path('y10/', TenthYear.as_view()),
]
