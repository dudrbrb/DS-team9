from django.db import models
from django.contrib.postgres.fields import ArrayField


class Major1(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=10, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/list/major/{self.slug}/'
    

class Major2(Major1):
    pass
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/list/tag/{self.slug}/'
    

class Member(models.Model):
    # DB col을 생성
    # 회원 이름
    member_name = models.CharField(max_length=10)

    # 회원 아이디
    member_id = models.CharField(max_length=20)

    # 회원 비밀번호
    member_password = models.IntegerField()

    # 회원 생년월일
    member_birthday = models.IntegerField()

    # 회원 학번
    member_studentNumber = models.IntegerField()

    # 회원의 제1전공 ManyToManyField 사용
    member_major_1 = models.ManyToManyField(Major1, related_name='+')

    # 회원의 제2전공
    member_major_2 = models.ManyToManyField(Major2, related_name='+')

    # 회원 취향 해시 목록
    member_hash = models.ManyToManyField(Tag, blank=True)


    # # 회원과 매칭된 회원(pk) 목록
    
    member_friends = ArrayField(models.IntegerField(),  null=True)

    # # 회원을 like한 회원(pk) 목록
    member_liked = ArrayField(models.IntegerField(),  null=True)

    # # 회원이 like한 회원(pk) 목록
    member_like = ArrayField(models.IntegerField(),  null=True)

    # 회원 공개구친 여부
    member_open = models.BooleanField()

    # 프로필 이미지
    prof_image = models.ImageField(upload_to='images/profile/%Y/%m/%d/', blank=True)
    
    # 배경 이미지
    back_image = models.ImageField(upload_to='images/background/%Y/%m/%d/', blank=True)


    # 데이터 생성 시 현재 시간 자동 기입 True
    create_at = models.DateTimeField(auto_now_add=True)

    # 데이터 수정 시 수정 시간 자동 기입
    update_at = models.DateTimeField(auto_now=True)

    # admin에서 표시될 제목
    def __str__(self):
        return f'[{self.pk}] {self.name} ({self.id})'
    
    # 상세페이지 링크 (마이페이지)
    def get_absolute_url(self):
        return f'/mypage/{self.pk}/'
