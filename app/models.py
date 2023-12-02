from django.db import models
from django.contrib.auth.models import AbstractUser

class Major1(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, allow_unicode=True)

    def __str__(self):
        return self.name

class Major2(Major1):
    pass

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    major = [
        ('국어국문학전공', '국어국문학전공'),
        ('일어일문학전공', '일어일문학전공'),
        ('중어중문학전공', '중어중문학전공'),
        ('영어영문학전공', '영어영문학전공'),
        ('불어불문학전공', '불어불문학전공'),
        ('독어독문학전공', '독어독문학전공'),
        ('스페인어전공', '스페인어전공'),
        ('사학전공', '사학전공'),
        ('철학전공', '철학전공'),
        ('미술사학전공', '미술사학전공'),
        ('경영학전공', '경영학전공'),
        ('회계학전공', '회계학전공'),
        ('국제통상학전공', '국제통상학전공'),
        ('법학전공', '법학전공'),
        ('문헌정보학전공', '문헌정보학전공'),
        ('사회학전공', '사회학전공'),
        ('심리학전공', '심리학전공'),
        ('아동가족학전공', '아동가족학전공'),
        ('사회복지학전공', '사회복지학전공'),
        ('정치외교학전공', '정치외교학전공'),
        ('의상디자인전공', '의상디자인전공'),
        ('유아교육과', '유아교육과'),
        ('디지털소프트웨어공학부', '디지털소프트웨어공학부'),
        ('컴퓨터공학전공', '컴퓨터공학전공'),
        ('IT미디어공학전공', 'IT미디어공학전공'),
        ('사이버보안전공', '사이버보안전공'),
        ('소프트웨어전공', '소프트웨어전공'),
        ('바이오공학전공', '바이오공학전공'),
        ('수학전공', '수학전공'),
        ('정보통계학전공', '정보통계학전공'),
        ('화학전공', '화학전공'),
        ('식품영양학전공', '식품영양학전공'),
        ('생활체육학전공', '생활체육학전공'),
        ('동양화전공', '동양화전공'),
        ('서양화전공', '서양화전공'),
        ('실내디자인전공', '실내디자인전공'),
        ('시각디자인전공', '시각디자인전공'),
        ('텍스타일디자인전공', '텍스타일디자인전공'),
        ('한국학전공', '한국학전공'),
        ('한국어교육전공', '한국어교육전공'),
        ('가상현실융합학과', '가상현실융합학과'),
        ('데이터사이언스학과', '데이터사이언스학과'),
    ]


    name = models.CharField(max_length=20, name="name")
    studentID = models.IntegerField(name="studentID")
    birth = models.DateField(null=True, name="birth")
    tel = models.CharField(max_length=20, name="tel")
    major1 = models.CharField(max_length=20, choices=major)
    major2 = models.CharField(max_length=20, choices=major, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    open_profile = models.BooleanField()
    prof_image = models.ImageField(upload_to='images/profile/%Y/%m/%d/', blank=True)
    back_image = models.ImageField(upload_to='images/background/%Y/%m/%d/', blank=True)
    
    friends = models.TextField(blank=True)
    liked = models.TextField(blank=True)
    like = models.TextField(blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['name', 'studentID', 'birth', 'tel', 'open_profile']

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/list/{self.pk}/'
