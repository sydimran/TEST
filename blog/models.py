from django.db import models

# Create your models here.

class laptop(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=64, decimal_places=2)
    Purchase_date = models.DateTimeField()