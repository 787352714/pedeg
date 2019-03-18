from django.urls import path

from . import views

urlpatterns = [
    path('', views.articalindex, name='artical index'),
    path('<int:id>/', views.articalcontain, name='artical contain'),
]