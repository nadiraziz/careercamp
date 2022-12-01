from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):

    courses = Courses.objects.all()
    faculties = Faculties.objects.all()
    students_response = StudentSayAboutUs.objects.all()
    posters = Poster.objects.all()
    context = {

        'courses': courses,
        'faculties': faculties,
        'students_response': students_response,
        'posters': posters
    }
    return render(request, 'index.html', context=context)


def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'courses.html', context=context)


def about(request):
    academy_details = AcademyDetails.objects.latest('id')
    students_response = StudentSayAboutUs.objects.all()

    context = {
        'academy': academy_details,
        'students_response': students_response,
    }
    return render(request, 'about.html', context=context)


def teams(request):
    return render(request, 'teams.html')


def contact(request):
    return render(request, 'contact.html')
