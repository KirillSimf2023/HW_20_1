from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):

    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    phot = models.ImageField(upload_to='photo/', **NULLABLE, verbose_name='Изображение (превью)')
    # category = models.CharField(max_length=100, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    prise = models.FloatField(**NULLABLE, default=0, verbose_name='Цена за покупку')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания')
    date_changes = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

