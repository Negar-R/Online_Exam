# Generated by Django 2.2 on 2020-01-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0003_question_profile_is_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_profile',
            name='is_correct',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
