from django.db import models


class CustomPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ім`я')
    second_name = models.CharField(max_length=100, verbose_name='Прізвище')
    email = models.EmailField(verbose_name='Електрона почта', unique=True)

    def __str__(self):
        return f'{self.name} {self.second_name}'


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва команди')
    person = models.ManyToManyField(CustomPerson, blank=True, null=True)

    def __str__(self):
        return self.name
