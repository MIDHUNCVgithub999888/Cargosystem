from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView
app_name='AdminApp'



urlpatterns=[


      path('AdminIndex/',views.AdminIndex,name='AdminIndex'),
      path('AdminRegister/',views.AdminRegister,name="AdminRegister"),
      path('login',LoginView.as_view(),name='login_url'),
      path('AddEmployee/',views.AddEmployee,name='AddEmployee'),
      path('ViewEmployee/',views.ViewEmployee,name="ViewEmployee"),
      path('OrderDetails/',views.OrderDetails,name="OrderDetails"),
      path('PaymentDetails/',views.PaymentDetails,name="PaymentDetails"),
      path('AdminBranches/',views.AdminBranches,name="AdminBranches"),
      path('AdminProfile/',views.AdminProfile,name='AdminProfile'),
      path('user_change_pass/',views.user_change_pass,name='user_change_pass'),
      path('ManageBranch/',views.ManageBranch,name='ManageBranch'),
      path('AdminDelete/<int:id>/',views.AdminDelete,name="AdminDelete"),
      path('Notifications/<int:id>/',views.Notifications,name="Notifications"),
      path('OrderDelete/<int:id>/',views.OrderDelete,name='OrderDelete'),
      path('ViewCustomers/',views.ViewCustomers,name='ViewCustomers'),
      path('Feedback/',views.Feedback,name='Feedback'),
     
      
      

]