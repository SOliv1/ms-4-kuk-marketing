from django.shortcuts import render


def services(request):
    """ A view to all services page """

    return render(request, '/services.html')


def about(request):
    """ view to return the about page """

    return render(request, 'services/about.html')


def our_brands(request):
    """ A view to our_brands page """

    return render(request, 'services/our_brands.html')


def contact_us(request):
    """ A view to all services page """

    return render(request, 'services/contact_us.html')
