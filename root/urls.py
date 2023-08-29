from django.urls import path
from .views import *

app_name = 'root'
urlpatterns = [
    path('',home, name= 'home'),
    path('about',about, name= 'about'),
    path('contact',contact, name= 'contact'),
    path('course-details',course_details, name= 'course-details'),
    path('courses',courses, name= 'courses'),
    path('trainers',trainers, name= 'trainers'),

]