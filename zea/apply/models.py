from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MerchandiserApply(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null = True)
    email = models.EmailField(max_length=254)
    contact = models.TextField(max_length=20, null = True)
    applyContent = models.TextField(max_length=512, null = True)
    #title = models.TextField(default='', null = True)
    #file = models.FileField(null=True)


class StudentApply(models.Model):
    name = models.CharField(max_length = 50, null = True)
    email = models.EmailField(max_length=254)
    contact = models.TextField(max_length=20, null = True)
    school = models.TextField(max_length= 20)
    grade = models.IntegerField(default=1)
    department = models.TextField(max_length = 20)
    applyContent = models.TextField(max_length = 512)
    subject = models.TextField(max_length = 30)

    