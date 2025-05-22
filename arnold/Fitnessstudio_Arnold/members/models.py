from django.db import models

class Member(models.Model):
    ABONEMENT_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    abonement = models.CharField(max_length=10, choices=ABONEMENT_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Employee(models.Model):
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('trainer', 'Trainer'),
        ('accountant', 'Accountant'),
        ('hr', 'HR'),
        ('other', 'Other'),
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.position}"