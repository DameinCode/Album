from django.db import models

# Create your models here.


class Company (models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField(default='')
    address = models.TextField(default='')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        # ordering = ('name',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Vacancy (models.Model):
    name = models.CharField(max_length=200)
    salary = models.FloatField(default=0)
    description = models.TextField(default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='vacancies')

    # tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.salary}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'description': self.description
        }