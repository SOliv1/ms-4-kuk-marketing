from django.shortcuts import render


def index(request):
    """ view to return the about page """

    return render(request, 'services/about.html')



