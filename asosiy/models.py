from django.db import models
from django.contrib.auth.models import User


class Muallif(models.Model):
    ism=models.CharField(max_length=25)
    yosh=models.IntegerField()
    kasb=models.CharField(max_length=25)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
class Maqola(models.Model):
    sarlavha=models.CharField(max_length=60)
    sana=models.DateField()
    mavzu=models.CharField(max_length=60)
    matn=models.TextField()
    mualif_fk=models.ForeignKey(Muallif,on_delete=models.CASCADE)

