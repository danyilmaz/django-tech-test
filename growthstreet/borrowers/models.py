from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    RETAIL = 'RE'
    PROFESSIONAL_SERVICES = 'PS'
    FOOD_AND_DRINK = 'FD'
    ENTERTAINMENT = 'EN'
    SECTOR_CHOICES = (
        (RETAIL, 'Retail'),
        (PROFESSIONAL_SERVICES, 'Professional Services'),
        (FOOD_AND_DRINK, 'Food and Drink'),
        (ENTERTAINMENT, 'Entertainment')
    )
    name = models.CharField(max_length=255)
    address = models.TextField()
    registered_number = models.CharField(max_length=8)
    sector = models.CharField(choices=SECTOR_CHOICES, max_length=2)


class Borrower(models.Model):
    user = models.OneToOneField(User)
    phonenumber = PhoneNumberField()
    borrow_amount = models.IntegerField()
    loan_days = models.IntegerField()
    loan_reason = models.TextField()
    company = models.ManyToManyField(Company)
