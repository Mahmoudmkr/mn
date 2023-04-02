from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Status(models.IntegerChoices):
    PENDING=1, 'pending'
    COMPLETED=2, 'completed'
    POSTPONED=3, 'postponed'
    CANCELED=4, 'canceled'

class Customer(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.description