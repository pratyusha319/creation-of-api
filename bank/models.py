from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=49)
    id=models.BigIntegerField(primary_key=True,)
    
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id=models.ForeignKey(Bank,on_delete=models.CASCADE,null=False)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
   
