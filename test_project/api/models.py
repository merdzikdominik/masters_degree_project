from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Annual(models.Model):

    dateFrom = models.DateField()
    dateTo = models.DateField()
    daysOfAnnualLeave = models.CharField(
        max_length=10, 
        validators=[
            RegexValidator(
                    regex=r'^\d{2}$',
                    message='Numer telefonu musi składać się z dwóch cyfr.',
                    code='invalid_phone_number'
            )
        ]
    )
    annualType = models.CharField(max_length=50)
    submitTime = models.DateTimeField(auto_now_add=True)