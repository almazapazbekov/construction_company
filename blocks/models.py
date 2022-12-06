from django.db import models


class Block(models.Model):
    number = models.IntegerField(verbose_name='Номер блока')
    price_per_meter = models.FloatField(verbose_name='Цена за метр')
    number_of_porches = models.IntegerField(verbose_name='Кол-во подъездов')
    number_of_floors = models.IntegerField(verbose_name='Количество этажей')
    number_of_flats_per_floor = models.IntegerField(verbose_name='Кол-во квартир на этаже')

    def get_flats(self):
        return Flats.objects.filter(block__id=self.id)

    def __str__(self):
        return str(self.number)


class Flats(models.Model):
    full_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='ФИО владельца')
    sale_date = models.DateField(null=True, blank=True, verbose_name='Дата продажи')

    status = models.CharField(max_length=30, choices=(
        ('Выкуп', 'Выкуп'),
        ('Выкуп не до конца', 'Выкуп не до конца'),
        ('Расторгнуто', 'Расторгнуто'),
        ('Не продано', 'Не продано')
    ), verbose_name='Статус выкупа')
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    area = models.IntegerField(verbose_name='Общая площать кв.м')

    def __str__(self):
        return str(self.full_name)
