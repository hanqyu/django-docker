from django.urls import path

from . import views

urlpatterns = [
    path('', views.AccessHistoryAPIView.as_view(), name='index'),
]