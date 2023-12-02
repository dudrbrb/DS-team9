# Generated by Django 4.2.7 on 2023-12-02 07:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=20)),
                ('studentID', models.IntegerField()),
                ('birth', models.DateField(null=True)),
                ('tel', models.CharField(max_length=20)),
                ('major1', models.CharField(choices=[('국어국문학전공', '국어국문학전공'), ('일어일문학전공', '일어일문학전공'), ('중어중문학전공', '중어중문학전공'), ('영어영문학전공', '영어영문학전공'), ('불어불문학전공', '불어불문학전공'), ('독어독문학전공', '독어독문학전공'), ('스페인어전공', '스페인어전공'), ('사학전공', '사학전공'), ('철학전공', '철학전공'), ('미술사학전공', '미술사학전공'), ('경영학전공', '경영학전공'), ('회계학전공', '회계학전공'), ('국제통상학전공', '국제통상학전공'), ('법학전공', '법학전공'), ('문헌정보학전공', '문헌정보학전공'), ('사회학전공', '사회학전공'), ('심리학전공', '심리학전공'), ('아동가족학전공', '아동가족학전공'), ('사회복지학전공', '사회복지학전공'), ('정치외교학전공', '정치외교학전공'), ('의상디자인전공', '의상디자인전공'), ('유아교육과', '유아교육과'), ('디지털소프트웨어공학부', '디지털소프트웨어공학부'), ('컴퓨터공학전공', '컴퓨터공학전공'), ('IT미디어공학전공', 'IT미디어공학전공'), ('사이버보안전공', '사이버보안전공'), ('소프트웨어전공', '소프트웨어전공'), ('바이오공학전공', '바이오공학전공'), ('수학전공', '수학전공'), ('정보통계학전공', '정보통계학전공'), ('화학전공', '화학전공'), ('식품영양학전공', '식품영양학전공'), ('생활체육학전공', '생활체육학전공'), ('동양화전공', '동양화전공'), ('서양화전공', '서양화전공'), ('실내디자인전공', '실내디자인전공'), ('시각디자인전공', '시각디자인전공'), ('텍스타일디자인전공', '텍스타일디자인전공'), ('한국학전공', '한국학전공'), ('한국어교육전공', '한국어교육전공'), ('가상현실융합학과', '가상현실융합학과'), ('데이터사이언스학과', '데이터사이언스학과')], max_length=20)),
                ('major2', models.CharField(choices=[('국어국문학전공', '국어국문학전공'), ('일어일문학전공', '일어일문학전공'), ('중어중문학전공', '중어중문학전공'), ('영어영문학전공', '영어영문학전공'), ('불어불문학전공', '불어불문학전공'), ('독어독문학전공', '독어독문학전공'), ('스페인어전공', '스페인어전공'), ('사학전공', '사학전공'), ('철학전공', '철학전공'), ('미술사학전공', '미술사학전공'), ('경영학전공', '경영학전공'), ('회계학전공', '회계학전공'), ('국제통상학전공', '국제통상학전공'), ('법학전공', '법학전공'), ('문헌정보학전공', '문헌정보학전공'), ('사회학전공', '사회학전공'), ('심리학전공', '심리학전공'), ('아동가족학전공', '아동가족학전공'), ('사회복지학전공', '사회복지학전공'), ('정치외교학전공', '정치외교학전공'), ('의상디자인전공', '의상디자인전공'), ('유아교육과', '유아교육과'), ('디지털소프트웨어공학부', '디지털소프트웨어공학부'), ('컴퓨터공학전공', '컴퓨터공학전공'), ('IT미디어공학전공', 'IT미디어공학전공'), ('사이버보안전공', '사이버보안전공'), ('소프트웨어전공', '소프트웨어전공'), ('바이오공학전공', '바이오공학전공'), ('수학전공', '수학전공'), ('정보통계학전공', '정보통계학전공'), ('화학전공', '화학전공'), ('식품영양학전공', '식품영양학전공'), ('생활체육학전공', '생활체육학전공'), ('동양화전공', '동양화전공'), ('서양화전공', '서양화전공'), ('실내디자인전공', '실내디자인전공'), ('시각디자인전공', '시각디자인전공'), ('텍스타일디자인전공', '텍스타일디자인전공'), ('한국학전공', '한국학전공'), ('한국어교육전공', '한국어교육전공'), ('가상현실융합학과', '가상현실융합학과'), ('데이터사이언스학과', '데이터사이언스학과')], max_length=20, null=True)),
                ('open_profile', models.BooleanField()),
                ('prof_image', models.ImageField(blank=True, upload_to='images/profile/%Y/%m/%d/')),
                ('back_image', models.ImageField(blank=True, upload_to='images/background/%Y/%m/%d/')),
                ('friends', models.TextField(blank=True)),
                ('liked', models.TextField(blank=True)),
                ('like', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Major1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(allow_unicode=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major2',
            fields=[
                ('major1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.major1')),
            ],
            bases=('app.major1',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, to='app.tag')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(blank=True, to='app.tag'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
