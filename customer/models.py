from django.db import models

class CustomerInfo(models.Model):
    name = models.CharField(max_length=25)
    customerId = models.CharField(max_length=10)
    cardNumber = models.CharField(max_length = 16)
    email = models.CharField(max_length=50)

def _str_(self):
    return '%s' % (self.name)