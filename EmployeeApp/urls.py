from django.urls import path
from EmployeeApp import views
from django.conf.urls import url
app_name='EmployeeApp'



urlpatterns=[

    path('EmployeeIndex/<int:id>/',views.EmployeeIndex,name='EmployeeIndex'),
    path('EmployeeLogin/',views.EmployeeLogin,name='EmployeeLogin'),
    path('EmployeeProfile/<int:id>/',views.EmployeeProfile,name='EmployeeProfile'),
    path('EmployeeLogOut/<int:id>/',views.EmployeeLogOut,name='EmployeeLogOut'),
    path('EmployeeRegister/<int:id>/',views.EmployeeRegister,name='EmployeeRegister'),
    path('ViewTransaction/<int:id>/',views.ViewTransaction,name='ViewTransaction'),





]