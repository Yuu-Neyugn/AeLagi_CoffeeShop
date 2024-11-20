# Generated by Django 4.0 on 2024-11-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Chủ đề')),
                ('content', models.TextField(verbose_name='Nội dung')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us_images/', verbose_name='Hình ảnh')),
            ],
            options={
                'verbose_name_plural': 'Giới thiệu (About us)',
            },
        ),
    ]