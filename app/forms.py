from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Tag

major = [
    ('선택', '선택'),
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


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(label="이름", widget=forms.TextInput(attrs={'placeholder': '본명을 입력해주세요'}))
    username = forms.CharField(label="ID", widget=forms.TextInput(attrs={'placeholder': '로그인 시 사용할 ID를 입력해주세요'}))
    password1 = forms.CharField(label="비밀번호", widget=forms.TextInput(attrs={'placeholder': '로그인 시 사용할 비밀번호를 입력하세요', 'type':'password'}))
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.TextInput(attrs={'placeholder': '비밀번호 확인을 위해 입력해주세요', 'type':'password'}))
    email = forms.EmailField(label="이메일", widget=forms.TextInput(attrs={'placeholder': 'duksae@duksung.ac.kr'}))
    studentID = forms.IntegerField(label="학번",  widget=forms.TextInput(attrs={'placeholder': '20230000'}))
    birth = forms.DateField(label="생년월일", widget=DateInput)
    tel = forms.CharField(label="연락처",  widget=forms.TextInput(attrs={'placeholder': '010-XXXX-XXXX'}))
    major1 = forms.ChoiceField(label="제1전공", choices=major)
    major2 = forms.ChoiceField(label="제2전공", choices=major)
    # hash = forms.ModelMultipleChoiceField(label="취향 선택 ",queryset=Tag.objects.filter(project=1),widget=forms.SelectMultiple())
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False  # Optional, depending on your requirements
    )
    prof_image = forms.ImageField(
        label="프로필 이미지",
        widget=forms.FileInput()
    )
    back_image = forms.ImageField(
        label="배경 이미지",
        widget=forms.FileInput()
    )
    # create_at = forms.DateTimeField(auto_now_add=True)
    # update_at = forms.DateTimeField(auto_now=True)
    open_profile = forms.BooleanField(label="프로필 공개 여부", required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("name", "username", "password1", "password2","birth", "tel", "email", "studentID",  "major1","major2", "tag", "prof_image", "back_image", "open_profile")

    def get_user(self):
        return get_user_model().objects.get(username=self.cleaned_data['username'])

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

