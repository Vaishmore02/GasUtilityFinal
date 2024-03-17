# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import random

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user profile information as needed

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('gas_refills', 'Gas Refills'),
        ('gas_conflicts', 'Gas Conflicts'),
        ('bill_payment', 'Bill Payment'),
        # Add other service types as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100, choices=SERVICE_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    status = models.CharField(max_length=50, default='Pending')
    token = token = random.randint(10000, 99999)  #models.CharField(max_length=20)  # You might generate this automatically

    def __str__(self):
        return f"{self.service_type} - {self.status} - Token No: {self.token}"