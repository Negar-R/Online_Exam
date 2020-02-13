from django.db import models
from django.contrib.auth.models import User
from QuestionsApp.models import Question

# Create your models here.


class Profile_Second(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    address = models.CharField(max_length = 50 , null = True)
    tokenKey = models.CharField(max_length = 200 , null = True)

    questions = models.CharField(max_length=100 , null = True)


    def __str__(self):
        return self.user.username
    