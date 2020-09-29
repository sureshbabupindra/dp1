from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('abc/', views.abc, name='blog-abc'),
    path('InstData/', views.InstData, name='blog-InstData'),
    path('Inst/', views.Inst, name='blog-Inst'),
    path('GetInstataneousData/', views.GetInstataneousData, name='blog-GetInvDaysData'),
    path('GetInvDaysData/', views.GetInvDaysData, name='blog-GetInvDaysData'),
    path('GetInvMonthData/', views.GetInvMonthData, name='blog-GetInvMonthData'),
]