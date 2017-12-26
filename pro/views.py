from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)


def home1(request):
    context = locals()
    template = 'home1.html'
    return render(request,template,context)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)


@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request,template,context)