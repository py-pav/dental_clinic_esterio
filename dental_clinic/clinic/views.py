from django.shortcuts import render

from .models import Doctor, Promotion, Review, Service


def index(request):
    services = Service.objects.all()[:4]
    promotions = Promotion.objects.all()[:3]
    reviews = Review.objects.all()[:3]

    context = {
        'services': services,
        'promotions': promotions,
        'reviews': reviews,
    }
    return render(request, 'clinic/index.html', context)


def about(request):
    return render(request, 'clinic/about.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'clinic/services.html', {'services': services})


def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'clinic/doctors.html', {'doctors': doctors})


def promotions(request):
    promotions = Promotion.objects.all()
    return render(request, 'clinic/promotions.html', {'promotions': promotions})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'clinic/reviews.html', {'reviews': reviews})


def contacts(request):
    return render(request, 'clinic/contacts.html')
