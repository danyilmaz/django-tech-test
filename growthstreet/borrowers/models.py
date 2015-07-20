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
    name = models.CharField(max_length=255, verbose_name='Company name')
    address = models.TextField()
    registered_number = models.CharField(max_length=8, verbose_name='Registered company number')
    sector = models.CharField(choices=SECTOR_CHOICES, max_length=2)


class Borrower(models.Model):
    user = models.OneToOneField(User)
    phonenumber = PhoneNumberField()
    borrow_amount = models.IntegerField(verbose_name='Amount to borrow')
    loan_days = models.IntegerField(verbose_name='How many days would you like the loan for')
    loan_reason = models.TextField(verbose_name='Why do you want the loan?')
    company = models.ManyToManyField(Company)
