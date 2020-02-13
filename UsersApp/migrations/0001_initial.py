# Generated by Django 2.2 on 2020-01-01 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('QuestionsApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.SmallIntegerField()),
                ('address', models.CharField(choices=[('T', 'Tehran'), ('O', 'Other')], max_length=100)),
                ('questions', models.ManyToManyField(to='QuestionsApp.Question')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.Profile')),
                ('que', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsApp.Question')),
            ],
        ),
    ]