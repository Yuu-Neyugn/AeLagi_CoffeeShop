# Generated by Django 4.0 on 2024-11-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_ourteam_email_alter_ourteam_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourteam',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='ourteam',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='ourteam',
            name='twitter',
        ),
        migrations.AddField(
            model_name='ourteam',
            name='social',
            field=models.URLField(blank=True, null=True, verbose_name='Social'),
        ),
    ]
