# Generated by Django 2.2 on 2020-01-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestUser', '0002_profile_second_tokenkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_second',
            name='questions',
        ),
        migrations.AddField(
            model_name='profile_second',
            name='questions',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
