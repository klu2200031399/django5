from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', NewHomePage, name='new_home'),
    path('travel/',Travel,name='travel'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print'),
    path('otp/',randomcall1,name="randomcall1"),
    path('otplogic/',randomcall,name="randomcall"),
    path('get_date/',get_date,name='get_date'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('car/',car,name='car'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('signup/',signup,name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('login/',login, name='login'),
    path('login1/', login1, name='login1'),
    path('logout/', logout, name='logout'),
    path('Feedback/',Feedback,name='Feedback'),





]
