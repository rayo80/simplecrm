from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add additional fields in here
    class Meta:
        db_table = 'users'

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales_representative = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=255)
    interaction_date = models.DateTimeField()

    class Meta:
        db_table = 'interactions'

    def __str__(self):
        return f"{self.interaction_type} with {self.customer}"
