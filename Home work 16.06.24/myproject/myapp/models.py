# myapp/models.py
from django.db import models
from .validators import validate_non_negative

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_non_negative]
    )
    stock = models.PositiveIntegerField(validators=[validate_non_negative])

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_id_and_name(self):
        return f'ID: {self.id}, Name: {self.name}'

    @classmethod
    def sum_prices(cls):
        return cls.objects.aggregate(total=models.Sum('price'))['total'] or 0

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[validate_non_negative])

    def __str__(self):
        return f'{self.name} - {self.age}'

    def get_id_and_name(self):
        return f'ID: {self.id}, Name: {self.name}'

    @classmethod
    def sum_ages(cls):
        return cls.objects.aggregate(total=models.Sum('age'))['total'] or 0
