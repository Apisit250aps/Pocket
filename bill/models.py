from django.db import models

# Create your models here.

class Bill(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    type = models.IntegerField(choices=(
        (1, "Income"),
        (2, "Expand")
    ))
    remark = models.TextField(default="-")
    date = models.DateTimeField(auto_now=True)