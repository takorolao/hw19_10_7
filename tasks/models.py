from django.db import models

class IceCream(models.Model):
    flavor = models.CharField(max_length=100, help_text='Вкус мороженого')
    description = models.TextField(help_text='Описание мороженого')
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text='Цена')

    def __str__(self):
        return self.flavor

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name