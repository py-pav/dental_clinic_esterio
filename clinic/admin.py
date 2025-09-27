from django.contrib import admin

from .models import Doctor, Promotion, Review, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']
