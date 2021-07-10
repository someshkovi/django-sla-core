from django.urls import include, path

from . import views

app_name = 'storage'
urlpatterns = [

    path('', views.StorageSummaryView , name='StorageSummaryView'),
    # path('<int:id>', views.detail, name='detail'),
    # path('chart/<str:obj>/', views.slaAchievedChart, name='slaAchievedChart'),
    # # path('chart/', views.slaAchievedChart, name='slaAchievedChart'),
    # path('zingChart/', views.slaChartView, name='zingChart'),
]
