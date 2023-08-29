from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'root/index.html', context= {'name':'Roham_Naeimi_site'})



def about(request):
    return render(request,'root/about.html')


def contact(request):
    return render(request,'root/contact.html')

def course_details(request):
    return render(request,'root/course-details.html')


def courses(request):
    return render(request,'root/courses.html')

def trainers(request):
    return render(request,'root/trainers.html')