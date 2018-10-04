from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class Branches(models.Model):
    name = models.CharField('Название филиала:', max_length=500)
    address = models.CharField('Адрес филиала:', max_length=500)
    phone = models.CharField('Номер телефона:', max_length=25, default='',)
    coordinates = models.CharField('Координаты', max_length=50, default=None,
                                   help_text='Введите гео-координаты филиала вформате:60.0520376,30.334460.Взять в google')
    is_active = models.BooleanField('Активен:', default=True)
    description = models.CharField('Комментарий:', max_length=500, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Price(models.Model):
    name = models.CharField('Название курса:', max_length=500)
    price = models.CharField('Цена курса:', max_length=500)
    image = models.ImageField('Изображение', upload_to='price/',)
    is_active = models.BooleanField('Активен:', default=True)
    description = models.CharField('Описание курса:', max_length=500, blank=True, null=True, )

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Цену'
        verbose_name_plural = 'Цены'


class Tagline(models.Model):
    phrase = models.CharField("Начало фразы на главной странице:", max_length=300)
    tag = models.CharField('Главный тег', max_length=25, help_text='Главный теглайн')
    end_phrase = models.CharField("Конец фразы на главной странице:", max_length=300, default=None, )
    is_active = models.BooleanField('Активен', default=True)
    image = models.ImageField('Изображение', upload_to='slider/',)

    def __str__(self):
        phrases = self.phrase + ' ' + self.tag + ' ' + self.end_phrase
        return '%s' % phrases

    class Meta:
        verbose_name = 'Теглайн'
        verbose_name_plural = 'Теглайны'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=300,)
    text = RichTextField('Текст', default=None)
    data_news = models.DateTimeField('Дата', default=timezone.now)
    is_active = models.BooleanField('Активен:', default=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Teachers(models.Model):
    full_name = models.CharField('Фамилия Имя:', max_length=250,)
    phone = models.CharField('Номер телефона:', max_length=25, blank=True, null=True,)
    avatar = models.ImageField('Аватар', upload_to='teachers/',)
    car_model = models.CharField('Марка автомобиля', max_length=30, blank=True, null=True)

    def __str__(self):
        return '%s' % self.full_name

    class Meta:
        verbose_name = 'Предподователь'
        verbose_name_plural = 'Предподователи'


