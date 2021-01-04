# Generated by Django 3.1.2 on 2021-01-04 11:10

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('upd', models.BooleanField(blank=True, default=False)),
                ('lenta', models.BooleanField(blank=True, default=False)),
                ('simple', models.BooleanField(blank=True, default=True)),
                ('slug', models.SlugField(default=None, max_length=160, unique=True)),
                ('img', models.ImageField(null=True, upload_to='pm')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='pm')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainpage.article')),
            ],
        ),
    ]