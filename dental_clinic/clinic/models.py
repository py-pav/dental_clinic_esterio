from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    icon = models.CharField(max_length=50, verbose_name="Иконка", help_text="Имя класса Font Awesome")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО врача")
    position = models.CharField(max_length=100, verbose_name="Должность")
    category = models.CharField(max_length=50, verbose_name="Категория")
    experience = models.CharField(max_length=50, verbose_name="Стаж")
    bio = models.TextField(verbose_name="Биография")
    education = models.TextField(verbose_name="Образование")
    qualifications = models.TextField(verbose_name="Повышение квалификации")
    photo = models.ImageField(upload_to='doctors/', verbose_name="Фотография")

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание акции")
    image = models.ImageField(upload_to='promotions/', verbose_name="Изображение")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор отзыва")
    text = models.TextField(verbose_name="Текст отзыва")
    photo = models.ImageField(upload_to='reviews/', verbose_name="Фотография автора")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author}"
