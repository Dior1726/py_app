from django.db import models

class News(models.Model):
    name = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=250, blank=True)
    date = models.DateTimeField('Дата создание', auto_now_add=True)
    sum = models.IntegerField('Цена', default=0)
    language = models.CharField('Язык', default='KZ', max_length=50)
    category = models.ForeignKey('Category', verbose_name='Вид', on_delete=models.CASCADE)
    subCategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, verbose_name='Предмет')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class SubCategory(models.Model):
    name = models.CharField('Название', max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Category(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
