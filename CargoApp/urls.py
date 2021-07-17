from django.urls import path
from CargoApp import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView
app_name='CargoApp'



urlpatterns=[


	path('',views.index,name='index'),
	path('Home/<int:id>/',views.Home,name='Home'),
	path('Register/',views.Register,name='Register'),
	path('Login',views.Login,name='Login'),
	path('Booking/<int:id>/',views.Booking,name='Booking'),
	path('UserProfile/<int:id>/',views.UserProfile,name='UserProfile'),
	path('UserLogout/<int:id>/',views.UserLogout,name='UserLogout'),
	path('UserDelete/<int:id>/',views.UserDelete,name='UserDelete'),
	path('ChangePassword/<int:id>/',views.ChangePassword,name="ChangePassword"),
	path('UserFeedback/<int:id>/',views.UserFeedback,name="UserFeedback"),
	path('UserOrder/<int:Cargotb_id>/',views.UserOrder,name='UserOrder'),
	path('service/',views.service,name="service"),
	path('OnlinePayment/<int:id>/',views.OnlinePayment,name='OnlinePayment'),
	path('Pricing/',views.Pricing,name='Pricing'),
	path('contact/',views.contact,name='contact'),
	path('About/',views.About,name="About"),
	path('FinalPayment/<int:id>/',views.FinalPayment,name='FinalPayment'),
	path('Edit/<int:id>/',views.Edit,name='Edit'),
	path('login',views.login,name='login'),
	path('UserNotifications/<int:Cargotb_id>/',views.UserNotifications,name='UserNotifications'),
	path('Branches/',views.Branches,name='Branches'),
	path('NotificationsDelete/<int:Cargotb_id>/',views.NotificationsDelete,name='NotificationsDelete'),
	path('OrderDelete/<int:Cargotb_id>/',views.OrderDelete,name='OrderDelete'),
	
	
	
	






]