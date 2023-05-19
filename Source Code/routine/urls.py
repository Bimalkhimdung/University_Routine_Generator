from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('computer_batch', views.computerBatch, name='computer_batch'),

    path('addComputer_first', views.computerData_first, name='addComputerfirst'),
    path('addComputer_second', views.computerData_second, name='addComputersecond'),
    path('addComputer_third', views.computerData_third, name='addComputerthird'),
    path('addComputer_fourth', views.computerData_fourth, name='addComputerfourth'),


    path('generate_routine', views.generate_routine, name='generate_routine'),
    path('view_routine', views.view_routine, name='view_routine'),
    path('view_routine/computer_first', views.view_routine_computerFirst, name='view_routine_computerFirst'),
    path('view_routine/computer_second', views.view_routine_computerSecond, name='view_routine_computerSecond'),
    path('view_routine/computer_third', views.view_routine_computerThird, name='view_routine_computerThird'),
    path('view_routine/computer_fourth', views.view_routine_computerFourth, name='view_routine_computerFourth'),
   
    path('teacher_routine', views.generate_teacher_routine, name='teacher_routine'),

    #authentication
    path('login/', auth_views.LoginView.as_view
    (template_name='routine/login.html', authentication_form=LoginForm),
    name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),

    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    
    path('about_us', views.aboutus, name='about_us'),
]
