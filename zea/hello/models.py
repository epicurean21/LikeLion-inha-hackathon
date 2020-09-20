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
    DESIGN = "디자인"
    VIDEO = "영상 및 사진"
    CONSERTING = "컨설팅"
    IT = "IT 및 프로그래밍"
    CATEGORY_CHOICES = (
        (DESIGN, "디자인"),
        (VIDEO, "영상 및 사진"),
        (CONSERTING, "컨설팅"),
        (IT, "IT 및 프로그래밍"),
    ) # 파이썬에서 상수를 사용하고 싶을 때 관용적으로 대문자로 작성 
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=DESIGN,
    )
 

    def __str__(self):
        return self.title

    