from django.shortcuts import render
from utils.projects.factory import make_projects


def home(request):
    return render(request, 'home/pages/home.html', context={
        'projects': [make_projects() for _ in range(2)],
    })


def home_projects(request):
    return render(request, 'home/pages/projects.html', context={
        'projects': [make_projects() for _ in range(3)],
    })


def projects(request, id):
    return render(request, 'home/pages/project-view.html', context={
        'project': make_projects(),
        'is_detail_page': True,
    })


def home_about(request):
    return render(request, 'home/pages/about.html', context={
        'projects': [make_projects() for _ in range(3)],
        'is_about_page': True
    })
