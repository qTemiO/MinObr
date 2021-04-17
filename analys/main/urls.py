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

    FirstNumYear,
    SecondNumYear,
    ThirdNumYear,
    FourNumYear,
    FiveNumYear,
    SixNumYear,
    SevenNumYear,
    EigthNumYear,
    NineNumYear,
    TenNumYear,
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
    
    path('ny1/', FirstNumYear.as_view()),
    path('ny2/', SecondNumYear.as_view()),
    path('ny3/', ThirdNumYear.as_view()),
    path('ny4/', FourNumYear.as_view()),
    path('ny5/', FiveNumYear.as_view()),
    path('ny6/', SixNumYear.as_view()),
    path('ny7/', SevenNumYear.as_view()),
    path('ny8/', EigthNumYear.as_view()),
    path('ny9/', NineNumYear.as_view()),
    path('ny10/', TenNumYear.as_view()),
]
