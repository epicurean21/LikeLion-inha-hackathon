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

    STORE = "업체"
    STUDENT = "학생"
    OTHERS = "기타"
    CATEGORY_CHOICES = (
        (STORE, "업체"),
        (STUDENT, "학생"),
        (OTHERS, "기타"),
    ) # 파이썬에서 상수를 사용하고 싶을 때 관용적으로 대문자로 작성 
    category2 = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=STORE,
    )
 




class StuApply (models.Model):
    namestore = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    email = models.EmailField(max_length=200 )
    major = models.CharField(max_length=200)
    phonenum = models.CharField(max_length=200)
    grade = models.IntegerField()
    account = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    STORE = "업체"
    STUDENT = "학생"
    OTHERS = "기타"
    CATEGORY_CHOICES = (
        (STORE, "업체"),
        (STUDENT, "학생"),
        (OTHERS, "기타"),
    ) # 파이썬에서 상수를 사용하고 싶을 때 관용적으로 대문자로 작성 
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=STORE,
    )
 
