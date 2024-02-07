from django.db import models

# Create your models here.
class ExcelData(models.Model):
    ID_user = models.IntegerField()
    Company_name = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    price = models.FloatField()
    tulov = models.FloatField()
    foyda = models.FloatField()
    chiqim = models.FloatField()
    product0 = models.CharField(max_length=100)
    firma = models.CharField(max_length=100)
    foiz = models.FloatField(null=True)

    def __str__(self):
        return f'{self.ID_user} - {self.Company_name}'