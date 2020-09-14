from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    name = models.TextField()
    spot = models.TextField()
    date = models.DateField(blank=True)
    pay = models.IntegerField()


    def __str__(self):
        return self.title
