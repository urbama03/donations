from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

ORG_CHOICES = (
    ('A', 'fundacja'),
    ('B', 'organizacja pozarządowa'),
    ('C', 'zbiórka lokalna'),
    ('D', 'domyślnie fundacja')
)

class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=ORG_CHOICES, max_length=1)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateTimeField()
    pick_up_time = models.TimeField(auto_now=False, auto_now_add=False)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)