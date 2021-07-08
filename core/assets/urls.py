from django.urls import  path

from . import views

app_name = 'assets'
urlpatterns = [
    # path('', views.index_view , name='index'),
    path('', views.IndexView.as_view() , name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
