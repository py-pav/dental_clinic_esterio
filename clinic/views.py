from django.shortcuts import render

from .models import Doctor, Promotion, Review, Service

# Статические данные вместо БД
SERVICES_DATA = [
    Service("Имплантация", "Современная имплантация зубов", "fa-tooth"),
    Service("Отбеливание", "Профессиональное отбеливание", "fa-star"),
    Service("Лечение кариеса", "Качественное лечение", "fa-medkit"),
    Service("Протезирование", "Съемное и несъемное протезирование", "fa-teeth"),
]

DOCTORS_DATA = [
    Doctor(
        name="Иванова Мария Петровна",
        position="Главный врач",
        category="Высшая категория",
        experience="15 лет",
        bio="Опытный специалист в области стоматологии",
        education="МГМСУ им. Евдокимова",
        qualifications="Курсы повышения квалификации 2023",
        photo="doctors/doctor1.jpg"
    ),
    # Добавьте других врачей по аналогии
]

PROMOTIONS_DATA = [
    Promotion(
        title="Скидка на имплантацию 20%",
        description="Специальное предложение на имплантацию зубов",
        image="promotions/promo1.jpg",
        start_date="2024-01-01",
        end_date="2024-12-31"
    ),
    # Добавьте другие акции
]

REVIEWS_DATA = [
    Review(
        author="Анна С.",
        text="Отличный сервис, профессиональные врачи!",
        photo="reviews/review1.jpg",
        created_at="2024-01-15"
    ),
    # Добавьте другие отзывы
]


def index(request):
    context = {
        'services': SERVICES_DATA[:4],
        'promotions': PROMOTIONS_DATA[:3],
        'reviews': REVIEWS_DATA[:3],
    }
    return render(request, 'clinic/index.html', context)


def about(request):
    return render(request, 'clinic/about.html')


def services(request):
    return render(request, 'clinic/services.html', {'services': SERVICES_DATA})


def doctors(request):
    return render(request, 'clinic/doctors.html', {'doctors': DOCTORS_DATA})


def promotions(request):
    return render(request, 'clinic/promotions.html', {'promotions': PROMOTIONS_DATA})


def reviews(request):
    return render(request, 'clinic/reviews.html', {'reviews': REVIEWS_DATA})


def contacts(request):
    return render(request, 'clinic/contacts.html')
