# Generated by Django 4.1.5 on 2023-11-20 08:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
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
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=10)),
                ('member_id', models.CharField(max_length=20)),
                ('member_password', models.IntegerField()),
                ('member_birthday', models.IntegerField()),
                ('member_studentNumber', models.IntegerField()),
                ('member_friends', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('member_liked', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('member_like', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('member_open', models.BooleanField()),
                ('prof_image', models.ImageField(blank=True, upload_to='images/profile/%Y/%m/%d/')),
                ('back_image', models.ImageField(blank=True, upload_to='images/background/%Y/%m/%d/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('member_hash', models.ManyToManyField(blank=True, to='app.tag')),
                ('member_major_1', models.ManyToManyField(related_name='+', to='app.major1')),
                ('member_major_2', models.ManyToManyField(related_name='+', to='app.major2')),
            ],
        ),
    ]
