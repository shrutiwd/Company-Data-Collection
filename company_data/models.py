from django.db import models

# Create your models here.
class Company(models.Model):  
    exchange = models.CharField(max_length=3)  
    symbol = models.CharField(max_length=5)  
    short_name = models.CharField(max_length=100)  
    long_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits = 10,decimal_places=2)
    market_cap = models.BigIntegerField()
    ebitda = models.BigIntegerField()
    revenue_growth = models.DecimalField(max_digits = 10,decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    country = models.CharField(max_length=100)
    fulltime_employees = models.IntegerField(blank=True, null=True)
    long_business_summary = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits = 10,decimal_places=2)
    