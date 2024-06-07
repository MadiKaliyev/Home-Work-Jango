from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Email')
    children = models.ManyToManyField('Child', through='ParentChild', related_name='parents')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Child(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    favorite_toy = models.CharField(max_length=50, verbose_name='Любимая игрушка')

    def __str__(self):
        return self.name

class ParentChild(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    relation = models.CharField(max_length=50, verbose_name='Тип родства')  # Например, 'биологический', 'приемный'

    class Meta:
        unique_together = ('parent', 'child')

    def __str__(self):
        return f'{self.parent} - {self.child}'

class IceCream(models.Model):
    flavor = models.CharField(max_length=50, verbose_name='Вкус')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.flavor

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=100, verbose_name='Местоположение')
    name = models.CharField(max_length=50, verbose_name='Название')
    ice_creams = models.ManyToManyField(IceCream, through='IceCreamKioskIceCream')

    def __str__(self):
        return self.name

class IceCreamKioskIceCream(models.Model):
    kiosk = models.ForeignKey(IceCreamKiosk, on_delete=models.CASCADE, verbose_name='Киоск')
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE, verbose_name='Мороженое')
    quantity = models.IntegerField(verbose_name='Количество мороженого в киоске')

    def __str__(self):
        return f'{self.kiosk.name} - {self.ice_cream.flavor}'
